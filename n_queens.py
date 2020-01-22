"""
N-Queens Problem using SimpleGUICS2Pygame
By Robin Andrews - info@compucademy.co.uk
"""

import n_queens_gui

QUEEN = 1
# Fixme: add constant for QUEEN (= 1) and replace throughout code.
BOARD_SIZE = 5


class NQueens:
    def __init__(self, n):
        self._size = n
        self.reset_board()

    def get_size(self):
        """
        Get size of board (square so only one value)
        """
        return self._size

    def reset_new_size(self, value):
        """
        Set size of board (square so only one value).
        """
        self._size = value
        self.reset_board()

    def get_board(self):
        """
        get game board.
        """
        return self._board

    def reset_board(self):
        """
        Restores board to empty.
        """
        self._board = [[0] * self._size for _ in range(self._size)]


    def is_winning_position(self):
        """
        Checks whether all queens are placed by counting them. There should be as many as the board size.
        """
        num_queens = sum(row.count(1) for row in self._board)
        return num_queens >= self._size


    def is_queen(self, pos):
        """
        Check whether given position contains a queen.
        """
        i, j = pos
        return self._board[i][j] == 1

    def place_queen(self, pos):
        """
        Add a queen (represented by 1) at a given (row, col).
        """
        if self.is_legal_move(pos):
            self._board[pos[0]][pos[1]] = 1
            return True  # Return value is useful for GUI - e.g trigger sound.
        return False

    def place_queen_no_checks(self, pos):
        """
        For testing
        """
        self._board[pos[0]][pos[1]] = 1

    def remove_queen(self, pos):
        """
        Set position on board to EMPTY value
        """
        self._board[pos[0]][pos[1]] = 0

    def is_legal_move(self, pos):
        """
        Check if position is on board and there are no clashes with existing queens
        """
        return self.check_row(pos[0]) and self.check_cols(pos[1]) and self.check_diagonals(pos)

    def check_row(self, row_num):
        """
        Check a given row for collisions. Returns True if move is legal
        """
        return not 1 in self._board[row_num]

    def check_cols(self, pos):
        """
        Check columns and return True if move is legal, False otherwise
        """
        legal = True
        for row in self._board:
            if row[pos] == 1:
                legal = False
        return legal

    def check_diagonals(self, pos):
        """
        Check all 4 diagonals from given position in a 2d list separately, to determine
        if there is a collision with another queen.
        Returns True if move is legal, else False.
        """
        num_rows, num_cols = len(self._board), len(self._board[0])
        row_num, col_num = pos

        # Lower-right diagonal from (row_num, col_num)
        i, j = row_num, col_num  # This covers case where spot is already occupied.
        while i < num_rows and j < num_cols:
            if self._board[i][j] == 1:
                return False
            i, j = i + 1, j + 1

        # Upper-left diagonal from (row_num, col_num)
        i, j = row_num - 1, col_num - 1
        while i >= 0 and j >= 0:
            if self._board[i][j] == 1:
                return False
            i, j = i - 1, j - 1

        # Upper-right diagonal from (row_num, col_num)
        i, j = row_num - 1, col_num + 1
        while i >= 0 and j < num_cols:
            if self._board[i][j] == 1:
                return False
            i, j = i - 1, j + 1

        # Lower-left diagonal from (row_num, col_num)
        i, j = row_num + 1, col_num - 1
        while i < num_cols and j >= 0:
            if self._board[i][j] == 1:
                return False
            i, j = i + 1, j - 1

        return True

    def __str__(self):
        res = ""
        for row in self._board:
            res += str(row) + "\n"
        return res


n_queens_gui.run_gui(NQueens(BOARD_SIZE))
