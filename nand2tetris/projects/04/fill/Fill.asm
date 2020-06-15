// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(RST_PIX_LOC)
	@16384
	D = A

	@currLoc
	M=D

	//(MAIN_LOOP)

	//check for button press 
	@0				//set flag to jump back to this loop
	D = A
	@loopFlag
	M=D
	
	(BTN_CHECK)
		@currColor
		D = M		//D holds current color before change
		@prevColor	//Store prevColor
		M = D
		@24576
		D = M
		
		
		@CLR_WHITE
		D; JEQ		//if no button pressed, jump to CLR_WHITE

		(CLR_BLACK)
			@currColor
			M=-1
			
			@CLR_DIFF
			0; JMP

		(CLR_WHITE)
			@currColor
			M=0
		
		(CLR_DIFF)
			//TODO: check if currColor changed, jump to FILL_LOOP if changed
//			@currColor
//			A = M - D 	//take diff of curr and prev color
//			D = A
//			@FILL_LOOP
//			D; JNE		//if change happened, goto FILL_LOOP
		
//		@loopFlag
//		D = M
//		@BTN_CHECK
//		D; JEQ

		@FILL_LOOP	//otherwise continue filling
		0; JMP



(FILL_LOOP)		//Fill Screen loop
	@currColor	//hold value of color in D
	D = M
	
	@currLoc
	A=M			//Make A the location of current pixel
	M = D 		//make current pixel color specified by currColor
	
	@currLoc
	MD = M+1	//increment location
	
	@24576
	D = D-A

	@RST_PIX_LOC
	D;JEQ	//start over if currLoc is last location
													//	TODO: add check for button press in this loop
	@1			//set flag to jump back to this loop
	D = A
	@loopFlag
	M=D
	
	@BTN_CHECK
	0; JMP


