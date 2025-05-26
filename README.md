# n-queen-problem

this project solves the classic N-Queens-Problem using three different methods:
    1. Backtracking
    2. Constraint Satisfaction Problem (CSP) with:
        2.1. forward checking
        2.2. MRV (minimum remaining values)
    3. Genetic algorithm 


# Features:
**Fast and Efficient**  
- CSP solver provides solutions quickly even for large n.
- The genetic algorithm processes at a slow speed with input values ​​greater than 20. The larger the number we enter, the slower the processing speed. Especially when we enter a number greater than 50, the slower the processing speed.
**Smart Search**  
Uses MRV heuristic and forward checking to reduce backtracking.
**User Interface**  
- Input is handled via a simple Tkinter GUI.  
- The chessboard visualization is displayed using Matplotlib.
**Customizable**  
- Easily switch between algorithms and change board size.


# Requirements:
- Python 3.10+
- numpy
- matplotlib

# Installation:
```pip install numpy matplotlib```


# How to Run:
run the firstPage.py to open the input window:
```python firstPage.py```
choose the algorithm and enter N (the number of queens).
the solution will be shown.
