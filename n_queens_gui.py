"""
N-Queens GUI code.
"""

try:
    import simplegui

    collision_sound = simplegui.load_sound("https://compucademy.co.uk/assets/buzz3x.mp3")
    success_sound = simplegui.load_sound("https://compucademy.co.uk/assets/treasure-found.mp3")

except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False
    collision_sound = simplegui.load_sound("https://compucademy.co.uk/assets/buzz3x.wav")
    success_sound = simplegui.load_sound("https://compucademy.co.uk/assets/treasure-found.wav")

queen_image = simplegui.load_image("https://compucademy.co.uk/assets/queen.PNG")
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
        self._frame.add_label("Welcome to N-Queens")
        self._frame.add_label("")  # For better spacing.
        msg = "Current board size: " + str(self._size)
        self._size_label = self._frame.add_label(msg)  # For better spacing.
        self._frame.add_label("")  # For better spacing.
        self._frame.add_button("Increase board size", self.increase_board_size)

        self._frame.add_button("Decrease board size", self.decrease_board_size)
        self._frame.add_label("") # For better spacing.
        self._frame.add_button("Reset", self.reset)
        self._frame.add_label("")  # For better spacing.
        self._label = self._frame.add_label("")

    def increase_board_size(self):
        """
        Resets game with board one size larger.
        """
        new_size = self._game.get_size() + 1
        self._game.reset_new_size(new_size)
        self._size = self._game.get_size()
        self._square_size = FRAME_SIZE[0] // self._size
        msg = "Current board size: " + str(self._size)
        self._size_label.set_text(msg)
        self.reset()

    def decrease_board_size(self):
        """
        Resets game with board one size larger.
        """
        if self._game.get_size() > 2:
            new_size = self._game.get_size() - 1
            self._game.reset_new_size(new_size)
            self._size = self._game.get_size()
            self._square_size = FRAME_SIZE[0] // self._size
            msg = "Current board size: " + str(self._size)
            self._size_label.set_text(msg)
            self.reset()


    def start(self):
        """
        Start the GUI.
        """
        self._frame.start()

    def reset(self):
        """
        Reset the board
        """
        self._game.reset_board()
        self._label.set_text("")


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
            if not self._game.place_queen((i, j)):
                collision_sound.play()
                self._label.set_text("Illegal move!")
            else:
                self._label.set_text("")

        if self._game.is_winning_position():
            success_sound.play()
            self._label.set_text("Well done. You have found a solution.")


    def get_grid_from_coords(self, position):
        """
        Given coordinates on a canvas, gets the indices of
        the grid.
        """
        pos_x, pos_y = position
        return (pos_y // self._square_size,  # row
                pos_x // self._square_size)  # col


def run_gui(game):
    """
    Instantiate and run the GUI
    """
    gui = NQueensGUI(game)
    gui.start()
