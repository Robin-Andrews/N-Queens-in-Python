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
        print(self._game._board)
        self._size = game.get_size()
        self._square_size = FRAME_SIZE[0] // self._size
        self._gui_board = []  # haven't decided whether this is a good idea.

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

    def get_grid_from_coords(self, position):
        """
        Given coordinates on a canvas, gets the indices of
        the grid.
        """
        posx, posy = position
        return (posy // self._square_size,  # row
                posx // self._square_size)  # col

    def draw(self, canvas):
        """
        Draw handler for GUI.
        """
        board = self._game.get_board()
        dimension = self._size
        size = self._square_size

        # Draw the squares
        for i in range(dimension):
            for j in range(dimension):
                color = "green" if ((i % 2 == 0 and j % 2 == 0) or i % 2 == 1 and j % 2 == 1) else "red"
                points = [(j * size, i * size), ((j + 1) * size, i * size), ((j + 1) * size, (i + 1) * size),
                          (j * size, (i + 1) * size)]
                canvas.draw_polygon(points, 1, color, color)

                if board[i][j] == 1:
                    canvas.draw_image(
                        queen_image,  # The image source
                        (queen_image_size[0] // 2, queen_image_size[1] // 2),
                        # Position of the center of the source image
                        queen_image_size,  # width and height of source
                        ((j * size) + size // 2, (i * size) + size // 2),
                        # Where the center of the image should be drawn on the canvas
                        (size, size)  # Size of how the image should be drawn
                    )

    def click(self, pos):
        """
        Toggles queen if legal position. Otherwise just removes queen.
        """
        i, j = self.get_grid_from_coords(pos)
        if self._game.is_queen((i, j)):
            self._game.remove_queen((i, j))
        else:
            self._game.place_queen((i, j))

    def game_over(self, winner):
        """
        Game over
        """
        pass

        # Game is no longer in progress
        self._inprogress = False


def run_gui(game):
    """
    Instantiate and run the GUI
    """
    gui = NQueensGUI(game)
    gui.start()

