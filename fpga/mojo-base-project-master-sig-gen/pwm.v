`timescale 1ns / 1ps

module pwm(
  input clk,
  output osc_pad_out,
  input [15:0] dutycycle
);
  parameter period = 2048;
  reg [12:0] p_counter = 0;
  reg onoff_a = 0;
  always @(posedge clk) p_counter <= (p_counter > period*2)?0:p_counter+1;
  //always @(posedge clk) onoff_a <= (p_counter > dutycycle && dutycycle > 0)?1:0;
  always @(posedge clk) onoff_a <= (p_counter < dutycycle && dutycycle > 0)?1:0;
  assign osc_pad_out = onoff_a;

endmodule
