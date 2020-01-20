"""
Test suite for N-Queens Solution
"""

import poc_simpletest
from n_queens import N_Queens


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

    suite.run_test(game.place_queen((1, 0)), False, "Test#2 place_queen() on occupied row.")
    suite.run_test(game.place_queen((2, 0)), True, "Test#3 place_queen() on unoccupied row.")

    suite.run_test(str(game), """[0, 0, 0, 0, 0]
[0, 0, 0, 0, 1]
[1, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
""", "Test#4 added queen at (2, 0)")

    # Test check_cols
    suite.run_test(game.place_queen((0, 4)), False, "Test#5 place_queen() on occupied column.")
    suite.run_test(game.place_queen((0, 1)), True, "Test#6 place_queen() on unoccupied column.")

    suite.run_test(str(game), """[0, 1, 0, 0, 0]
[0, 0, 0, 0, 1]
[1, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
""", "Test#7 added queen at (0, 1)")

    # Test check_diagonals()

    suite.run_test(game.place_queen((4, 1)), False, "Test#8 place_queen() on occupied diagonal.")
    suite.run_test(game.place_queen((4, 3)), True, "Test#9 place_queen() on unoccupied diagonal.")

    suite.run_test(str(game), """[0, 1, 0, 0, 0]
[0, 0, 0, 0, 1]
[1, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 1, 0]
""", "Test#10 added queen at (4, 3)")

    suite.report_results()


run_suite(N_Queens)
