// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@0
D=M  //D = mem[0]

@res
M = 0 //make variable 'res' hold value 0

@1
D=M   //D = mem[1]

@multBy
M = D //Store variable to be decremented in multBy

(LOOP)
	@multBy
	D=M 	//hold value of multBy
	@END	//jump to end if multBy is 0
	D;JEQ
	@multBy
	M=M-1
	@res
	D=M
	@0
	D = D + M
	@res
	M = D
	@LOOP
	0; JMP
	
(END)
@res
D=M
@2
M=D		//set mem[2] = result
	                     