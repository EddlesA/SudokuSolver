# SudokuSolver
Background:
I wrote this Sudoklu solver in year 11 (2019). It was a personal project that I undertook as a sort of 'extension' to my Software Design and Development course.
The general idea behind the Sudoku solver was origninally to solve sudokus in any way possible. After some searching I was surprised to find that most sudoku solving programs used an optimised brute force (trial and error) method to solve sudokus. I decided that I wanted to create a set of logical algorithms to solve sudoku's. The solver would only enter a number if it was certain that the number was correct.

About the progam:
* The progam is written in FreeBasic, a weird offcut of basic that is very similar to psudo code -> It was the language that was taught to my class.
* The final source code is a mess. I have had various attempts at neatening this program up. I will have another go at cleaning it up at some point and perhaps translating it to another language. Maybe giving it a GUI and some other nice features
* It was written using example sudoku puzzles from https://www.websudoku.com/ it can solve all difficulties from that website but has mixed success with harder difficulties on other sites.
* The comments on the code are crap.

How it works:
* The sudoku grid is stored in a 5D array. This is to make navigation through the array easier as at times I needed to limit certain functions to a single box row or column in the sudoku grid
