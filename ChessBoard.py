import matplotlib.pyplot as plt
import numpy as np

class ChessBoard:
    def __init__(self, n, queens):
        self.n = n
        self.queens = queens
        self.draw_board(queens)
         
    def draw_board(self, queens):
        board = np.add.outer(range(self.n), range(self.n)) % 2
        plt.figure(figsize=(5,4.5), dpi=100)
        plt.imshow(board, cmap="binary_r")
        fontSize = 300 // self.n

        # drawing queens
        for row, col in enumerate(queens):
            plt.text(col - 1, row + 0.1, u'\u265B', fontsize=fontSize, color='#933fb8', ha='center', va='center')

        plt.xticks([])
        plt.yticks([])
        plt.title(f"{self.n}-Queens Solution")
        plt.show()