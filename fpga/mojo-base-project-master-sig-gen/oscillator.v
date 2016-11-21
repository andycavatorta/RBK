`timescale 1ns / 1ps

module oscillator(
  input clk,
  output osc_pad_out,
  input [16:0] period
);
  reg [24:0] p_counter = 0;
  reg onoff_a = 0;
  always @(posedge clk) p_counter <= (p_counter > period*512)?0:p_counter+1;
  always @(posedge clk) onoff_a <= (p_counter > period *256 && period > 0)?1:0;
  assign osc_pad_out = onoff_a;

endmodule

