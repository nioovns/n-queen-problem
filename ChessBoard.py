# import matplotlib.pyplot as plt
# import numpy as np


# class ChessBoard:
#     def __init__(self, n, queens):
#         self.n = n
#         self.queens = queens
#         self.draw_board(queens)

#     def draw_board(self, queens):
#         board = np.add.outer(range(self.n), range(self.n)) % 2
#         plt.imshow(board, cmap="binary_r")

#         # drawing queens with red dots
#         for row, col in enumerate(queens):
#             plt.plot(col - 1 , row, 'ro', markersize=20) 
#         plt.xticks([])
#         plt.yticks([])
#         plt.title(f"{self.n}-Queens Solution")
#         plt.show()

import matplotlib.pyplot as plt
import numpy as np


class ChessBoard:
    def __init__(self, n, queens):
        self.n = n
        self.queens = queens
        self.draw_board(queens)

    def draw_board(self, queens):
        board = np.add.outer(range(self.n), range(self.n)) % 2
        plt.imshow(board, cmap="binary_r")

        # drawing queens with red dots
        for row, col in enumerate(queens):
            # plt.plot(col - 1 , row, 'ro', markersize=20) 
            plt.text(col - 1.28, row + 0.25, u'\u265B', fontsize=40, color='red', zorder=10)
        plt.xticks([])
        plt.yticks([])
        plt.title(f"{self.n}-Queens Solution")
        plt.show()