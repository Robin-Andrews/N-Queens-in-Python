"""
N-Queens Board Class

(N-Queens Problem using SimpleGUICS2Pygame) # Fixme - right docstring

"""

class N_Queens:
    def __init__(self, n):
        self._board = [[0] * n for _ in range(n)]
        
    def place_queen(self, pos):
        """
        Add a queen (represented by 1) at a given (row, col).
        """
        if self.is_legal_move(pos):
            self._board[pos[0]][pos[1]] = 1
            return True # Maybe remove any return value after testing
        return False
            
    def place_queen_no_checks(self, pos):
        """
        For testing
        """
        self._board[pos[0]][pos[1]] = 1
        
            
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
        collision = False

        # Lower-right diagonal from (row_num, col_num)
        i, j = row_num + 1, col_num + 1
        while i < num_rows and j < num_cols:
            if self._board[i][j] == 1:
                collision = True
            i, j = i + 1, j + 1

        # Upper-left diagonal from (row_num, col_num)
        i, j = row_num - 1, col_num - 1
        while i >= 0 and j >= 0:
            if self._board[i][j] == 1:
                collision = True
            i, j = i - 1, j - 1

        # Upper-right diagonal from (row_num, col_num)
        i, j = row_num - 1, col_num + 1
        while i >= 0 and j < num_cols:
            if self._board[i][j] == 1:
                collision = True
            i, j = i - 1, j + 1

        # Lower-left diagonal from (row_num, col_num)
        i, j = row_num + 1, col_num - 1
        while i < num_cols and j >= 0:
            if self._board[i][j] == 1:
                collision = True
            i, j = i + 1, j - 1

        return not collision


    def __str__(self):
        res = ""
        for row in self._board:
            res += str(row) + "\n"
        return res
          