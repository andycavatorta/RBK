
module duplex_out(
  input clk,
  input [5:0] mod,
  input [15:0] val,
  input toggle,
  output [12:0] outport
);
  reg [5:0] oldMod = 0;
  reg [15:0] oldVal = 0;
  reg [11:0] outport_reg = 0;
  assign outport[11:0] = outport_reg[11:0];
  always @(posedge toggle or negedge toggle)
		if (toggle == 1'b0)
		//if (oldMod != mod || oldVal[15:0] != val[15:0]) //  
      begin
		//oldMod <= mod;
		//oldVal <= val;
	   outport_reg[1] <= mod[0];
	   outport_reg[2] <= mod[1];
	   outport_reg[3] <= mod[2];
	   outport_reg[4] <= mod[3];
	   outport_reg[5] <= mod[4];
	   outport_reg[6] <= mod[5];
	   outport_reg[7] <= val[0];
	   outport_reg[8] <= val[1];
	   outport_reg[9] <= val[2];
	   outport_reg[10] <= val[3];
	   outport_reg[11] <= val[4];
	   outport_reg[0] <= 0;
		
		// wait x clock cycles
		/*
	   #1000 outport_reg[1] <= val[5];
	   #1000 outport_reg[2] <= val[6];
	   #1000 outport_reg[3] <= val[7];
	   #1000 outport_reg[4] <= val[8];
	   #1000 outport_reg[5] <= val[9];
	   #1000 outport_reg[6] <= val[10];
	   #1000 outport_reg[7] <= val[11];
	   #1000 outport_reg[8] <= val[12];
	   #1000 outport_reg[9] <= val[13];
	   #1000 outport_reg[10] <= val[14];
	   #1000 outport_reg[11] <= val[15];
	   #1000 outport_reg[0] <= 1;
		*/
		end
		else
      begin
		// wait x clock cycles
	   outport_reg[1] <= val[5];
	   outport_reg[2] <= val[6];
	   outport_reg[3] <= val[7];
	   outport_reg[4] <= val[8];
	   outport_reg[5] <= val[9];
	   outport_reg[6] <= val[10];
	   outport_reg[7] <= val[11];
	   outport_reg[8] <= val[12];
	   outport_reg[9] <= val[13];
	   outport_reg[10] <= val[14];
	   outport_reg[11] <= val[15];
	   outport_reg[0] <= 1;
	 end
endmodule