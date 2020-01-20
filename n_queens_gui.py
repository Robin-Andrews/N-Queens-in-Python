"""
N-Queens GUI code.
"""

try:
    import simplegui

    queen_image = simplegui.load_image("https://compucademy.co.uk/assets/queen.PNG")
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False
    queen_image = simplegui._load_local_image("queen.PNG")

from square import Square

queen_image_size = (queen_image.get_width(), queen_image.get_height())
FRAME_SIZE = (400, 400)
BOARD_SIZE = 20  # rows/cols


class NQueensGUI:
    """
    GUI for N-Queens game.
    """

    def __init__(self, game):
        """
        Instantiate the GUI for N-Queens game.
        """
        # Game board
        self._game = game
        self._size = game.get_size()

        # Graphical board
        # Do I need separate boards for logical/graphical?
        # padding_left = (FRAME_SIZE[0] - SQUARE_SIZE * BOARD_SIZE) // 2
        # padding_top = (FRAME_SIZE[1] - SQUARE_SIZE * BOARD_SIZE) // 2
        square_size = FRAME_SIZE[0] // self._size
        self._gui_board = []
        for i in range(self._size):
            for j in range(self._size):
                color = "green" if ((i % 2 == 0 and j % 2 == 0) or i % 2 == 1 and j % 2 == 1) else "red"
                self._gui_board.append(Square(square_size, (j * square_size,  i * square_size), color,
                                  False))  # include padding

        # Set up frame
        self.setup_frame()





        # Start new game
        # self.newgame()

    def setup_frame(self):
        """
        Create GUI frame and add handlers.
        """
        self._frame = simplegui.create_frame("N-Queens Game",
                                             FRAME_SIZE[0], FRAME_SIZE[1])
        self._frame.set_canvas_background('White')

        # Set handlers
        self._frame.set_draw_handler(self.draw)
        self._frame.set_mouseclick_handler(self.click)
        # self._frame.add_button("Reset", self.newgame)
        self._label = self._frame.add_label("")

    def start(self):
        """
        Start the GUI.
        """
        self._frame.start()

    # def reset(self):
    #     """
    #     Reset the board
    #     """
    #     self._board = self._game.get_board()
    #     self._label.set_text("")



    def draw(self, canvas):
        """
        Draw handler for GUI.
        """
        for row in self._gui_board:
            for square in self._gui_board:
                square.draw(canvas)

        # Draw the current players' moves
        # for row in range(self._size):
        #     for col in range(self._size):
        #         symbol = self._board.square(row, col)
        #         coords = self.get_coords_from_grid(row, col)
        #         if symbol == provided.PLAYERX:
        #             self.drawx(canvas, coords)
        #         elif symbol == provided.PLAYERO:
        #             self.drawo(canvas, coords)

    def click(pos):
        """
        Removes a queen when clicked
        Adds a queen to a Square if it is a legal move.
        """
        # global squares
        clicked_square_index = None
        for idx, square in enumerate(self._board):
            if square.is_in(pos):
                clicked_square_index = idx

        if clicked_square_index is not None:
            if squares[clicked_square_index].get_has_queen():
                squares[clicked_square_index].set_has_queen(False)
            else:
                squares[clicked_square_index].set_has_queen(True)


    def game_over(self, winner):
        """
        Game over
        """
        # Display winner
        if winner == provided.DRAW:
            self._label.set_text("It's a tie!")
        elif winner == provided.PLAYERX:
            self._label.set_text("X Wins!")
        elif winner == provided.PLAYERO:
            self._label.set_text("O Wins!")

            # Game is no longer in progress
        self._inprogress = False

    def get_coords_from_grid(self, row, col):
        """
        Given a grid position in the form (row, col), returns
        the coordinates on the canvas of the center of the grid.
        """
        # X coordinate = (bar spacing) * (col + 1/2)
        # Y coordinate = height - (bar spacing) * (row + 1/2)
        return (self._bar_spacing * (col + 1.0 / 2.0),  # x
                self._bar_spacing * (row + 1.0 / 2.0))  # y

    def get_grid_from_coords(self, position):
        """
        Given coordinates on a canvas, gets the indices of
        the grid.
        """
        posx, posy = position
        return (posy // self._bar_spacing,  # row
                posx // self._bar_spacing)  # col


def run_gui(game):
    """
    Instantiate and run the GUI
    """
    gui = NQueensGUI(game)
    gui.start()



# def draw(canvas):
#     """
#     Default draw handler for the simplegui frame
#     """
#     for square in squares:
#         square.draw(canvas)
#
#
# def click(pos):
#     """
#     Removes a queen when clicked
#     Adds a queen to a Square if it is a legal move.
#     """
#     global squares
#     clicked_square_index = None
#     for idx, square in enumerate(squares):
#         if square.is_in(pos):
#             clicked_square_index = idx
#
#     if clicked_square_index is not None:
#         if squares[clicked_square_index].get_has_queen():
#             squares[clicked_square_index].set_has_queen(False)
#         else:
#             squares[clicked_square_index].set_has_queen(True)
#
#
# frame = simplegui.create_frame("N Queens", FRAME_SIZE[0], FRAME_SIZE[1])
# frame.set_canvas_background("black")
# frame.set_draw_handler(draw)
# frame.set_mouseclick_handler(click)
#
# # Create a test square
# squares = []
# padding_left = (FRAME_SIZE[0] - SQUARE_SIZE * BOARD_SIZE) // 2
# padding_top = (FRAME_SIZE[1] - SQUARE_SIZE * BOARD_SIZE) // 2
# for i in range(BOARD_SIZE):
#     for j in range(BOARD_SIZE):
#         color = "green" if ((i % 2 == 0 and j % 2 == 0) or i % 2 == 1 and j % 2 == 1) else "red"
#         squares.append(Square(SQUARE_SIZE, (padding_left + j * SQUARE_SIZE, padding_top + i * SQUARE_SIZE), color,
#                               False))  # include padding
#
# frame.start()
