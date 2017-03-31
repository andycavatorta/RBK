`timescale 1ns / 1ps

module pwm_osc(
  input clk_div,
  input [7:0] pwm_reg,
  input [27:0] osc_reg,
  input reset,
  output pwm_osc_out
);
reg squareWaveOut_reg = 1'b1;
reg [27:0] osc_counter = 1'b1;
reg toggle = 1'b0;

begin
always @(posedge clk_div) osc_counter <= (osc_counter >= osc_reg || reset == 1)?1'b0:osc_counter + 1'b1;
always @(posedge clk_div) squareWaveOut_reg <= (osc_counter  >= osc_reg * pwm_reg / 32)?1'b0:1'b1;
end


/*
always @(posedge clk_div)
begin
	if (reset == 1)
		begin
		osc_counter <= 1'b0;
		squareWaveOut_reg <= 1'b0;
		end
	else if (osc_counter >= osc_reg)
		osc_counter <= 1'b0;
	else if (osc_counter >= osc_reg * pwm_reg / 32)
		squareWaveOut_reg <= 1'b0;
	else
		begin
		osc_counter <= osc_counter + 1'b1;
		squareWaveOut_reg <= 1'b1;
		end
end
*/


assign pwm_osc_out = squareWaveOut_reg;

endmodule

