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

(TEMP)
    @current
    M=0
(LOOP)
    // See if anything is pressed on the keyboard
    @KBD
    D=M
    @WHITE
    D;JEQ
    // If something is pressed, set fill to black
    @BLACK
    0;JMP

(WHITE)
    // Make sure current isn't greater than total max screen size 
    @current
    D=M
    @8192
    D=D-A
    // if 8192 <= current, then break out 
    @TEMP
    D;JEQ

    // Set the current location to white
    @current
    D=M
    @SCREEN
    A=A+D
    M=0

    // increment the counter
    @current
    M=M+1

    @WHITE
    0;JMP

(BLACK)
    // Make sure current isn't greater than total max screen size 
    @current
    D=M
    @8192
    D=D-A    // if 8192 <= current, then break out 
    @TEMP
    D;JEQ

    // Set the current location to white
    @current
    D=M
    @SCREEN
    A=A+D
    M=-1

    // increment the counter
    @current
    M=M+1

    @BLACK
    0;JMP

    @LOOP
    0;JMP