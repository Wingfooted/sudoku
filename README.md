# Sudoku Backtrack Algorithm

##Overview

This is a simple implementation of a simple backtrack algorithm in sudoku using recursion in python, capable of solving and finding all sollutions to sudoku puzzles. This project was coded within the span of two hours without internet acsess or external support. 

##Implementation

Critical to the functioning of recusive programs, is the base case and recursive case. To test for the base case the functions of "full board" and "valid board" were made, and each fufil their namesake. 

In the case of the recursive instance the function solve, will run itself, finding a new cell and testing a new algorithm. If the recursive case fails, then there is no output shown with the "display" function, and the end user will not visualize the unsucsessful track. The ramifications of this are explored in performance. 

Consequently, the possible cases for each sudoku board can be visualized as a tree, where each cell of the sudoku board's assumption represents a branch, and each final branch of the tree representing a valid case, as invalid branches are not displayed or kept. 

##Running the Program

To run the program, download the sudoku.py file. Python3 or later is requred to run the program. The user can run the program with python3 sudoku.py. By pressing enter the user will cycle to the next valid sudoku board, utilizing the aformentioned algorithm, with the program reaching termination when all valid boards have been displayed. 

Modifications to the sudoku puzzle can be made within the text editor. 

##Performance

As previously mentioned, the performance of this algorithm is not ideal and stronger algorithms exist. In the worst case scenario the solve function must test all 9 cases for the n^2 board. Meaning that the time complexity is O(9(n^2)). More efficient algorithms can be employed, however this was a demonstration of a simple reccursive sudoku algorithm. 
