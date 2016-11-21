`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    21:12:52 06/15/2016 
// Design Name: 
// Module Name:    clock_divider 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module clock_divider( clk ,out_clk );

output out_clk ;
reg out_clk ;

input clk ;
wire clk ;

reg [5:0] m;

initial m = 0;

always @ (posedge (clk)) begin
 if (m<5'b10000)
  m <= m + 1'b1;
 else   
  m <= 0;
end

always @ (m) begin
 if (m<5'b01000)
  out_clk <= 1'b1;
 else
  out_clk <= 1'b0;
end
  

endmodule