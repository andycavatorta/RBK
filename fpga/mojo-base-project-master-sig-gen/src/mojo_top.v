/* 
modules:
echo
highValOnLEDs
lowValOnLEDs


PWM
oscillator
digialOut

digigalIn
analogIn

*/

module mojo_top(
    // 50MHz clock input
    input clk,
    // Input from reset button (active low)
    //input rst_n,
    // cclk input from AVR, high when AVR is ready
    input cclk,
    // Outputs to the 8 onboard LEDs
    output[7:0]led,
    // AVR SPI connections
    output spi_miso,
    input spi_ss,
    input spi_mosi,
    input spi_sck,
    // AVR ADC channel select
    output [3:0] spi_channel,
    // Serial connections
    input avr_tx, // AVR Tx => FPGA Rx
    output avr_rx, // AVR Rx => FPGA Tx
    input avr_rx_busy, // AVR Rx buffer full
     // parallel communications
     input [23:0] parallel_in,
     // module outputs
    output pwm_osc_00_out,
    output pwm_osc_01_out,
    output pwm_osc_02_out,
    output pwm_osc_03_out,
    output pwm_osc_04_out,
    output pwm_osc_05_out,
    output pwm_osc_06_out,
    output pwm_osc_07_out,
    output pwm_osc_08_out,
    output pwm_osc_09_out,
    output pwm_osc_10_out,
    output pwm_osc_11_out,
    output pwm_osc_12_out,
    output pwm_osc_13_out,
    output digital_osc_14_out,
    output digital_osc_15_out,
    output digital_osc_16_out,
    output digital_osc_17_out,
    output digital_osc_18_out,
    output digital_osc_19_out,
    output digital_osc_20_out,
    output digital_osc_21_out,
    output digital_osc_22_out,
    output digital_osc_23_out
    );

// wire rst = ~rst_n; // make reset active high
// these signals should be high-z when not used
assign spi_miso = 1'bz;
assign avr_rx = 1'bz;
assign spi_channel = 4'bzzzz;
//assign led[7:6] = 2'bz;

// clock divider
//parameter clockDivision_max = 4'b1010;
//parameter clockDivision_mid = 3'b101;
//reg clockDivision_reg;
//wire clk_div;
//always @ (posedge clk) clockDivision_reg <= (clockDivision_reg >= clockDivision_max)?1'b0:clockDivision_reg + 1'b1;
//always @ (posedge clk) clk_div <= (clockDivision_reg > clockDivision_mid)?1'b0:1'b1;

//clock_divider clock_divider_instance(clk,clk_div);

// bit widths for data types
parameter pwmBitWidth = 10;
parameter oscBitWidth = 27;
parameter channelBitWidth = 4;

// temp registers for incoming data
reg [pwmBitWidth:0] incoming_pwm_reg = 0;
reg [oscBitWidth:0] incoming_osc_reg = 0;
reg [channelBitWidth:0] incoming_channel_reg = 0;

assign led[channelBitWidth:0] = incoming_channel_reg;
//assign led[6] = parallel_in[23];
assign led[5] = 1'bz;
assign led[6] = 1'bz;
assign led[7] = parallel_in[0];
//assign led[7:0] = parallel_in[7:0];

reg [pwmBitWidth:0] channel_00_pwm_reg;
reg [pwmBitWidth:0] channel_01_pwm_reg;
reg [pwmBitWidth:0] channel_02_pwm_reg;
reg [pwmBitWidth:0] channel_03_pwm_reg;
reg [pwmBitWidth:0] channel_04_pwm_reg;
reg [pwmBitWidth:0] channel_05_pwm_reg;
reg [pwmBitWidth:0] channel_06_pwm_reg;
reg [pwmBitWidth:0] channel_07_pwm_reg;
reg [pwmBitWidth:0] channel_08_pwm_reg;
reg [pwmBitWidth:0] channel_09_pwm_reg;
reg [pwmBitWidth:0] channel_10_pwm_reg;
reg [pwmBitWidth:0] channel_11_pwm_reg;
reg [pwmBitWidth:0] channel_12_pwm_reg;
reg [pwmBitWidth:0] channel_13_pwm_reg;
reg [pwmBitWidth:0] channel_14_pwm_reg;
reg [pwmBitWidth:0] channel_15_pwm_reg;
reg [pwmBitWidth:0] channel_16_pwm_reg;
reg [pwmBitWidth:0] channel_17_pwm_reg;
reg [pwmBitWidth:0] channel_18_pwm_reg;
reg [pwmBitWidth:0] channel_19_pwm_reg;
reg [pwmBitWidth:0] channel_20_pwm_reg;
reg [pwmBitWidth:0] channel_21_pwm_reg;
reg [pwmBitWidth:0] channel_22_pwm_reg;
reg [pwmBitWidth:0] channel_23_pwm_reg;



reg [oscBitWidth:0] channel_00_osc_reg;
reg [oscBitWidth:0] channel_01_osc_reg;
reg [oscBitWidth:0] channel_02_osc_reg;
reg [oscBitWidth:0] channel_03_osc_reg;
reg [oscBitWidth:0] channel_04_osc_reg;
reg [oscBitWidth:0] channel_05_osc_reg;
reg [oscBitWidth:0] channel_06_osc_reg;
reg [oscBitWidth:0] channel_07_osc_reg;
reg [oscBitWidth:0] channel_08_osc_reg;
reg [oscBitWidth:0] channel_09_osc_reg;
reg [oscBitWidth:0] channel_10_osc_reg;
reg [oscBitWidth:0] channel_11_osc_reg;
reg [oscBitWidth:0] channel_12_osc_reg;
reg [oscBitWidth:0] channel_13_osc_reg;
/*
reg [oscBitWidth:0] channel_14_osc_reg;
reg [oscBitWidth:0] channel_15_osc_reg;
reg [oscBitWidth:0] channel_16_osc_reg;
reg [oscBitWidth:0] channel_17_osc_reg;
reg [oscBitWidth:0] channel_18_osc_reg;
reg [oscBitWidth:0] channel_19_osc_reg;
reg [oscBitWidth:0] channel_20_osc_reg;
reg [oscBitWidth:0] channel_21_osc_reg;
reg [oscBitWidth:0] channel_22_osc_reg;
reg [oscBitWidth:0] channel_23_osc_reg;
*/

/*
reg channel_00_reset;
reg channel_01_reset;
reg channel_02_reset;
reg channel_03_reset;
reg channel_04_reset;
reg channel_05_reset;
reg channel_06_reset;
reg channel_07_reset;
reg channel_08_reset;
reg channel_09_reset;
reg channel_10_reset;
reg channel_11_reset;

pwm_osc pwm_osc_00(clk, channel_00_pwm_reg, channel_00_osc_reg, channel_00_reset, pwm_osc_00_out);
pwm_osc pwm_osc_01(clk, channel_01_pwm_reg, channel_01_osc_reg, channel_01_reset, pwm_osc_01_out);
pwm_osc pwm_osc_02(clk, channel_02_pwm_reg, channel_02_osc_reg, channel_02_reset, pwm_osc_02_out);
pwm_osc pwm_osc_03(clk, channel_03_pwm_reg, channel_03_osc_reg, channel_03_reset, pwm_osc_03_out);
pwm_osc pwm_osc_04(clk, channel_04_pwm_reg, channel_04_osc_reg, channel_04_reset, pwm_osc_04_out);
pwm_osc pwm_osc_05(clk, channel_05_pwm_reg, channel_05_osc_reg, channel_05_reset, pwm_osc_05_out);
pwm_osc pwm_osc_06(clk, channel_06_pwm_reg, channel_06_osc_reg, channel_06_reset, pwm_osc_06_out);
pwm_osc pwm_osc_07(clk, channel_07_pwm_reg, channel_07_osc_reg, channel_07_reset, pwm_osc_07_out);
pwm_osc pwm_osc_08(clk, channel_08_pwm_reg, channel_08_osc_reg, channel_08_reset, pwm_osc_08_out);
pwm_osc pwm_osc_09(clk, channel_09_pwm_reg, channel_09_osc_reg, channel_09_reset, pwm_osc_09_out);
pwm_osc pwm_osc_10(clk, channel_10_pwm_reg, channel_10_osc_reg, channel_10_reset, pwm_osc_10_out);
pwm_osc pwm_osc_11(clk, channel_11_pwm_reg, channel_11_osc_reg, channel_11_reset, pwm_osc_11_out);
*/

pwm_osc pwm_osc_00(clk, channel_00_pwm_reg, channel_00_osc_reg, pwm_osc_00_out);
pwm_osc pwm_osc_01(clk, channel_01_pwm_reg, channel_01_osc_reg, pwm_osc_01_out);
pwm_osc pwm_osc_02(clk, channel_02_pwm_reg, channel_02_osc_reg, pwm_osc_02_out);
pwm_osc pwm_osc_03(clk, channel_03_pwm_reg, channel_03_osc_reg, pwm_osc_03_out);
pwm_osc pwm_osc_04(clk, channel_04_pwm_reg, channel_04_osc_reg, pwm_osc_04_out);
pwm_osc pwm_osc_05(clk, channel_05_pwm_reg, channel_05_osc_reg, pwm_osc_05_out);
pwm_osc pwm_osc_06(clk, channel_06_pwm_reg, channel_06_osc_reg, pwm_osc_06_out);
pwm_osc pwm_osc_07(clk, channel_07_pwm_reg, channel_07_osc_reg, pwm_osc_07_out);
pwm_osc pwm_osc_08(clk, channel_08_pwm_reg, channel_08_osc_reg, pwm_osc_08_out);
pwm_osc pwm_osc_09(clk, channel_09_pwm_reg, channel_09_osc_reg, pwm_osc_09_out);
pwm_osc pwm_osc_10(clk, channel_10_pwm_reg, channel_10_osc_reg, pwm_osc_10_out);
pwm_osc pwm_osc_11(clk, channel_11_pwm_reg, channel_11_osc_reg, pwm_osc_11_out);
pwm_osc pwm_osc_12(clk, channel_12_pwm_reg, channel_12_osc_reg, pwm_osc_12_out);
pwm_osc pwm_osc_13(clk, channel_13_pwm_reg, channel_13_osc_reg, pwm_osc_13_out);

digital_osc digital_osc_14(clk, channel_14_pwm_reg, digital_osc_14_out);
digital_osc digital_osc_15(clk, channel_15_pwm_reg, digital_osc_15_out);
digital_osc digital_osc_16(clk, channel_16_pwm_reg, digital_osc_16_out);
digital_osc digital_osc_17(clk, channel_17_pwm_reg, digital_osc_17_out);
digital_osc digital_osc_18(clk, channel_18_pwm_reg, digital_osc_18_out);
digital_osc digital_osc_19(clk, channel_19_pwm_reg, digital_osc_19_out);
digital_osc digital_osc_20(clk, channel_20_pwm_reg, digital_osc_20_out);
digital_osc digital_osc_21(clk, channel_21_pwm_reg, digital_osc_21_out);
digital_osc digital_osc_22(clk, channel_22_pwm_reg, digital_osc_22_out);
digital_osc digital_osc_23(clk, channel_23_pwm_reg, digital_osc_23_out); 
/*
pwm_osc pwm_osc_14(clk, channel_14_pwm_reg, channel_14_osc_reg, pwm_osc_14_out);
pwm_osc pwm_osc_15(clk, channel_15_pwm_reg, channel_15_osc_reg, pwm_osc_15_out);
pwm_osc pwm_osc_16(clk, channel_16_pwm_reg, channel_16_osc_reg, pwm_osc_16_out);
pwm_osc pwm_osc_17(clk, channel_17_pwm_reg, channel_17_osc_reg, pwm_osc_17_out);
pwm_osc pwm_osc_18(clk, channel_18_pwm_reg, channel_18_osc_reg, pwm_osc_18_out);
pwm_osc pwm_osc_19(clk, channel_19_pwm_reg, channel_19_osc_reg, pwm_osc_19_out);
pwm_osc pwm_osc_20(clk, channel_20_pwm_reg, channel_20_osc_reg, pwm_osc_20_out);
pwm_osc pwm_osc_21(clk, channel_21_pwm_reg, channel_21_osc_reg, pwm_osc_21_out);
pwm_osc pwm_osc_22(clk, channel_22_pwm_reg, channel_22_osc_reg, pwm_osc_22_out);
pwm_osc pwm_osc_23(clk, channel_23_pwm_reg, channel_23_osc_reg, pwm_osc_23_out);
*/


always @(posedge parallel_in[0])
begin
    if (parallel_in[23] == 0) // freq
      begin
        incoming_channel_reg[0] <= parallel_in[22];
        incoming_channel_reg[1] <= parallel_in[21];
        incoming_channel_reg[2] <= parallel_in[20];
        incoming_channel_reg[3] <= parallel_in[19];
        incoming_channel_reg[4] <= parallel_in[18];
        incoming_osc_reg[0] <= parallel_in[17];
        incoming_osc_reg[1] <= parallel_in[16];
        incoming_osc_reg[2] <= parallel_in[15];
        incoming_osc_reg[3] <= parallel_in[14];
        incoming_osc_reg[4] <= parallel_in[13];
        incoming_osc_reg[5] <= parallel_in[12];
        incoming_osc_reg[6] <= parallel_in[11];
        incoming_osc_reg[7] <= parallel_in[10];
        incoming_osc_reg[8] <= parallel_in[9];
        incoming_osc_reg[9] <= parallel_in[8];
        incoming_osc_reg[10] <= parallel_in[7];
        incoming_osc_reg[11] <= parallel_in[6];
        incoming_osc_reg[12] <= parallel_in[5];
        incoming_osc_reg[13] <= parallel_in[4];
        incoming_osc_reg[14] <= parallel_in[3];
        incoming_osc_reg[15] <= parallel_in[2];
        incoming_osc_reg[16] <= parallel_in[1];
/*
		 case(incoming_channel_reg) // which channel
			  5'b00000:
					begin
					channel_00_reset <= 1;
					end
			  5'b00001:
					begin
					channel_01_reset <= 1;
					end
			  5'b00010:
					begin
					channel_02_reset <= 1;
					end
			  5'b00011:
					begin
					channel_03_reset <= 1;
					end
			  5'b00100:
					begin
					channel_04_reset <= 1;
					end
			  5'b00101:
					begin
					channel_05_reset <= 1;
					end
			  5'b00110:
					begin
					channel_06_reset <= 1;
					end
			  5'b00111:
					begin
					channel_07_reset <= 1;
					end
			  5'b01000:
					begin
					channel_08_reset <= 1;
					end
			  5'b01001:
					begin
					channel_09_reset <= 1;
					end
			  5'b01010:
					begin
					channel_10_reset <= 1;
					end
			  5'b01011:
					begin
					channel_11_reset <= 1;
					end
			  endcase
			  */
	   end
    if (parallel_in[23] == 1) // pwm
      begin
        incoming_osc_reg[17] <= parallel_in[22];
        incoming_osc_reg[18] <= parallel_in[21];
        incoming_osc_reg[19] <= parallel_in[20];
        incoming_osc_reg[20] <= parallel_in[19];
        incoming_osc_reg[21] <= parallel_in[18];
        incoming_osc_reg[22] <= parallel_in[17];
        incoming_osc_reg[23] <= parallel_in[16];
        incoming_osc_reg[24] <= parallel_in[15];
        incoming_osc_reg[25] <= parallel_in[14];
        incoming_osc_reg[26] <= parallel_in[13];
        incoming_osc_reg[27] <= parallel_in[12];
        incoming_pwm_reg[0] <= parallel_in[11];
        incoming_pwm_reg[1] <= parallel_in[10];
        incoming_pwm_reg[2] <= parallel_in[9];
        incoming_pwm_reg[3] <= parallel_in[8];
        incoming_pwm_reg[4] <= parallel_in[7];
        incoming_pwm_reg[5] <= parallel_in[6];
        incoming_pwm_reg[6] <= parallel_in[5];
        incoming_pwm_reg[7] <= parallel_in[4];
        incoming_pwm_reg[8] <= parallel_in[3];
        incoming_pwm_reg[9] <= parallel_in[2];
        incoming_pwm_reg[10] <= parallel_in[1];
		 case(incoming_channel_reg) // which channel
			  5'b00000:
					begin
					channel_00_osc_reg <= incoming_osc_reg;
					channel_00_pwm_reg <= incoming_pwm_reg;
					//channel_00_reset <= 0;
					end
			  5'b00001:
					begin
					channel_01_osc_reg <= incoming_osc_reg;
					channel_01_pwm_reg <= incoming_pwm_reg;
					//channel_01_reset <= 0;
					end
			  5'b00010:
					begin
					channel_02_osc_reg <= incoming_osc_reg;
					channel_02_pwm_reg <= incoming_pwm_reg;
					//channel_02_reset <= 0;
					end
			  5'b00011:
					begin
					channel_03_osc_reg <= incoming_osc_reg;
					channel_03_pwm_reg <= incoming_pwm_reg;
					//channel_03_reset <= 0;
					end
			  5'b00100:
					begin
					channel_04_osc_reg <= incoming_osc_reg;
					channel_04_pwm_reg <= incoming_pwm_reg;
					//channel_04_reset <= 0;
					end
			  5'b00101:
					begin
					channel_05_osc_reg <= incoming_osc_reg;
					channel_05_pwm_reg <= incoming_pwm_reg;
					//channel_05_reset <= 0;
					end
			  5'b00110:
					begin
					channel_06_osc_reg <= incoming_osc_reg;
					channel_06_pwm_reg <= incoming_pwm_reg;
					//channel_06_reset <= 0;
					end
			  5'b00111:
					begin
					channel_07_osc_reg <= incoming_osc_reg;
					channel_07_pwm_reg <= incoming_pwm_reg;
					//channel_07_reset <= 0;
					end
			  5'b01000:
					begin
					channel_08_osc_reg <= incoming_osc_reg;
					channel_08_pwm_reg <= incoming_pwm_reg;
					//channel_08_reset <= 0;
					end
			  5'b01001:
					begin
					channel_09_osc_reg <= incoming_osc_reg;
					channel_09_pwm_reg <= incoming_pwm_reg;
					//channel_09_reset <= 0;
					end
			  5'b01010:
					begin
					channel_10_osc_reg <= incoming_osc_reg;
					channel_10_pwm_reg <= incoming_pwm_reg;
					//channel_10_reset <= 0;
					end
			  5'b01011:
					begin
					channel_11_osc_reg <= incoming_osc_reg;
					channel_11_pwm_reg <= incoming_pwm_reg;
					//channel_11_reset <= 0;
					end
			  5'b01100:
					begin
					channel_12_osc_reg <= incoming_osc_reg;
					channel_12_pwm_reg <= incoming_pwm_reg;
					end
			  5'b01101:
					begin
					channel_13_osc_reg <= incoming_osc_reg;
					channel_13_pwm_reg <= incoming_pwm_reg;
					end
			  5'b01110:
					begin
					channel_14_pwm_reg <= incoming_pwm_reg;
					end
			  5'b01111:
					begin
					channel_15_pwm_reg <= incoming_pwm_reg;
					end
			  5'b10000:
					begin
					channel_16_pwm_reg <= incoming_pwm_reg;
					end
			  5'b10001:
					begin
					channel_17_pwm_reg <= incoming_pwm_reg;
					end
			  5'b10010:
					begin
					channel_18_pwm_reg <= incoming_pwm_reg;
					end
			  5'b10011:
					begin
					channel_19_pwm_reg <= incoming_pwm_reg;
					end
			  5'b10100:
					begin
					channel_20_pwm_reg <= incoming_pwm_reg;
					end
			  5'b10101:
					begin
					channel_21_pwm_reg <= incoming_pwm_reg;
					end
			  5'b10110:
					begin
					channel_22_pwm_reg <= incoming_pwm_reg;
					end
			  5'b10111:
					begin
					channel_23_pwm_reg <= incoming_pwm_reg;
					end
				endcase
		end
end

/*
always @(negedge parallel_in[0])
begin
		  channel_00_reset <= 0;
		  channel_01_reset <= 0;
		  channel_02_reset <= 0;
		  channel_03_reset <= 0;
		  channel_04_reset <= 0;
		  channel_05_reset <= 0;
		  channel_06_reset <= 0;
		  channel_07_reset <= 0;
		  channel_08_reset <= 0;
		  channel_09_reset <= 0;
		  channel_10_reset <= 0;
		  channel_11_reset <= 0;
end
*/
/*
always @(posedge parallel_in[0])
begin
    case(incoming_channel_reg) // which channel
        5'b00000:
            begin
            channel_00_osc_reg <= incoming_osc_reg;
				channel_00_pwm_reg <= incoming_pwm_reg;
				channel_00_reset <= 1;
            end
        5'b00001:
            begin
            channel_01_osc_reg <= incoming_osc_reg;
				channel_01_pwm_reg <= incoming_pwm_reg;
				channel_01_reset <= 1;
            end
        5'b00010:
            begin
            channel_02_osc_reg <= incoming_osc_reg;
				channel_02_pwm_reg <= incoming_pwm_reg;
				channel_02_reset <= 1;
            end
        5'b00011:
            begin
            channel_03_osc_reg <= incoming_osc_reg;
				channel_03_pwm_reg <= incoming_pwm_reg;
				channel_03_reset <= 1;
            end
        5'b00100:
            begin
            channel_04_osc_reg <= incoming_osc_reg;
				channel_04_pwm_reg <= incoming_pwm_reg;
				channel_04_reset <= 1;
            end
        5'b00101:
            begin
            channel_05_osc_reg <= incoming_osc_reg;
				channel_05_pwm_reg <= incoming_pwm_reg;
				channel_05_reset <= 1;
            end
        5'b00110:
            begin
            channel_06_osc_reg <= incoming_osc_reg;
				channel_06_pwm_reg <= incoming_pwm_reg;
				channel_06_reset <= 1;
            end
        5'b00111:
            begin
            channel_07_osc_reg <= incoming_osc_reg;
				channel_07_pwm_reg <= incoming_pwm_reg;
				channel_07_reset <= 1;
            end
        5'b01000:
            begin
            channel_08_osc_reg <= incoming_osc_reg;
				channel_08_pwm_reg <= incoming_pwm_reg;
				channel_08_reset <= 1;
            end
        5'b01001:
            begin
            channel_09_osc_reg <= incoming_osc_reg;
				channel_09_pwm_reg <= incoming_pwm_reg;
				channel_09_reset <= 1;
            end
        5'b01010:
            begin
            channel_10_osc_reg <= incoming_osc_reg;
				channel_10_pwm_reg <= incoming_pwm_reg;
				channel_10_reset <= 1;
            end
        5'b01011:
            begin
            channel_11_osc_reg <= incoming_osc_reg;
				channel_11_pwm_reg <= incoming_pwm_reg;
				channel_11_reset <= 1;
            end
        5'b01100:
            begin
            channel_12_osc_reg <= incoming_osc_reg;
            end
        5'b01101:
            begin
            channel_13_osc_reg <= incoming_osc_reg;
            end
        5'b01110:
            begin
            channel_14_osc_reg <= incoming_osc_reg;
            end
        5'b01111:
            begin
            channel_15_osc_reg <= incoming_osc_reg;
            end
        5'b10000:
            begin
            channel_16_osc_reg <= incoming_osc_reg;
            end
        5'b10001:
            begin
            channel_17_osc_reg <= incoming_osc_reg;
            end

        5'b10010:
            begin
            channel_18_osc_reg <= incoming_osc_reg;
            end
        5'b10011:
            begin
            channel_19_osc_reg <= incoming_osc_reg;
            end
        5'b10100:
            begin
            channel_20_osc_reg <= incoming_osc_reg;
            end
        5'b10101:
            begin
            channel_21_osc_reg <= incoming_osc_reg;
            end
        5'b10110:
            begin
            channel_22_osc_reg <= incoming_osc_reg;
            end
        5'b10111:
            begin
            channel_23_osc_reg <= incoming_osc_reg;
            end
    endcase
end
*/

endmodule
