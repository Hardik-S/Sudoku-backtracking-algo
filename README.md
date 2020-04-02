# Sudoku solver (backtracking algorithm)

Sudoku is an ancient logic-based, combinatorial number-placement puzzle. The objective of the game is to fill a 9×9 grid with digits 1 to 9 such that each column, row, and the nine 3×3 subgrids contain all of the digits from 1 to 9 only once.  

Given that Sudoku is effectively a constraint satisfaction problem, a backtracking algorithm is employed to solve this computational problem. It incrementally builds solution candidtates and abandons a canditate once it determines that the candidate cannot be completed to produce a valid solution. It then _backtracks_ to the last viable canditate and continues testing until the board is complete, or until it determines that the puzzle is invalid. 
