`timescale 1ns / 1ps

module digitalOut(
  input clk,
  output digital_pad_out,
  input [16:0] value
);
  reg onoff_a = 0;
  always @(posedge clk) onoff_a <= (value > 0)?0:1;
  assign digital_pad_out = onoff_a;
endmodule
