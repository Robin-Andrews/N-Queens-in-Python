"""
N-Queens Board Class
Console Based
"""

class Board:
    def __init__(self, n):
        self._board = [[0] * n for _ in range(n)]
        
    def place_queen(self, pos):
        """
        Add a queen (represented by 1) at a given (row, col).
        """
        if self.is_legal_move(pos):
            self._board[pos[0]][pos[1]] = 1
            return True # Maybe remove after testing
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
        return self.check_row(pos[0]) and self.check_cols(pos[1])
            
        
    def check_row(self, row_num):
        """
        Check a given row for collisions. Returns True if move is legal
        """
        return not 1 in self._board[row_num]
        
        
    def check_cols(self, pos):
        legal = True
        for row in self._board:
            if row[pos] == 1:
                legal = False
        return legal
            
        
    def check_diagonals(self, pos):
        pass
        
    def __str__(self):
        res = ""
        for row in self._board:
            res += str(row) + "\n"
        return res

if __name__ == "__main__":
    board = Board(5)
    print(board)
    board.place_queen((1, 4))
    print(board)
            