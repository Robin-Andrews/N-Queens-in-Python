"""
Test suite for N-Queens Solution
"""

import poc_simpletest
from board_class import Board

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    suite = poc_simpletest.TestSuite()    
        
    # create a board
    game = game_class(5)
    
    # Tests
    suite.run_test(str(game), """[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
""", "Test#0 create empty board")

    # Test add_queen before coding illegal moves check
    game.place_queen_no_checks((1, 4))
    
    suite.run_test(str(game), """[0, 0, 0, 0, 0]
[0, 0, 0, 0, 1]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
""", "Test#1 add queen at (1, 4)")

    # Test check_rows
    
    suite.run_test(game.place_queen((1, 3)), False, "Test#2 place_queen() on occupied row.")
    suite.run_test(game.place_queen((2, 3)), True, "Test#3 place_queen() on unoccupied row.")
    
    suite.run_test(str(game), """[0, 0, 0, 0, 0]
[0, 0, 0, 0, 1]
[0, 0, 0, 1, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
""", "Test#4 add queen at (1, 4)")
    
    
    
    # Test check_cols
    suite.run_test(game.place_queen((0, 4)), False, "Test#5 place_queen() on occupied column.")
    suite.run_test(game.place_queen((4, 0)), True, "Test#6 place_queen() on unoccupied column.")
        

    suite.report_results()
    
    
run_suite(Board)
    
    



