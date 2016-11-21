`timescale 1ns / 1ps

module singlePulse(
  input clk,
  output pulse_pad_out,
  input [16:0] duration,
  input trigger
);
  
  reg [16:0] duration_reg = 0;
  reg onoff_a = 0;
  //always @(posedge trigger) duration_reg <= duration;
  //always @(negedge trigger) duration_reg <= duration;
  always @(posedge clk) duration_reg <= (duration_reg > 0)? duration_reg-1 : 0;
  always @(posedge clk) onoff_a <= (duration_reg > 0)?1:0;
  assign pulse_pad_out = onoff_a;

endmodule