#include <stdio.h>
#include <stdlib.h>


int main(void) {
    
}

void print_intro() {
    printf(
    "box codes go from top left to bottom right, \n
    each box code is 9 digits.\n
    here is an example\n 
       | 4 |   ||\n
       |   |   ||\n
     1 | 2 | 5 ||\n
    assume this is the top left box in a sudoku 3x3 grid \n
    the box code for this box would be 000040125 \n
    each box code is 9 characters long, if input correctly \n
    a grid matching the one you input will be displayed upon entry of the 9th box code. \n
    ")
}