`timescale 1ns / 1ps

module pwm_osc(
  input clk_div,
  input [5:0] pwm_reg,
  input [16:0] osc_reg,
  output pwm_osc_out
);
reg squareWaveOut_reg = 1'b1;
reg [16:0] osc_counter = 1'b1;

begin
always @(posedge clk_div) osc_counter <= (osc_counter >= osc_reg)?1'b0:osc_counter + 1'b1;
always @(posedge clk_div) squareWaveOut_reg <= (osc_counter >= osc_reg * pwm_reg / 16)?1'b0:1'b1;
end

assign pwm_osc_out = squareWaveOut_reg;

endmodule

