try:
    import simplegui
    queen_image = simplegui.load_image("https://compucademy.co.uk/assets/queen.PNG")
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    queen_image = simplegui._load_local_image("queen.PNG")
    
queen_image_size = (queen_image.get_width(), queen_image.get_height())
FRAME_SIZE = (400, 400)
SQUARE_SIZE = 40
BOARD_SIZE = 4  # rows/cols



class Square:
    def __init__(self, size, pos, color, has_queen=False):
        self.size = size
        self.pos = pos
        self.color = color
        self.has_queen = has_queen

    def get_has_queen(self):
        return self.has_queen

    def set_has_queen(self, val):
        self.has_queen = val

    def is_in(self, pos):
        """
        Determine whether coordinates are within the area of this Square
        """
        return self.pos[0] < pos[0] < self.pos[0] + self.size and self.pos[1] < pos[1] < self.pos[1] + self.size

    def draw(self, canvas):
        """
        calls canvas.draw_image() to display self on canvas
        """
        points = [(self.pos[0], self.pos[1]), (self.pos[0] + self.size, self.pos[1]),
                  (self.pos[0] + self.size, self.pos[1] + self.size), (self.pos[0], self.pos[1] + self.size)]
        canvas.draw_polygon(points, 1, self.color, self.color)

        if self.has_queen:
            canvas.draw_image(
                queen_image,  # The image source
                (queen_image_size[0] // 2, queen_image_size[1] // 2),  # Position of the center of the source image
                queen_image_size,  # width and height of source
                (self.pos[0] + self.size // 2, self.pos[1] + self.size // 2),
                # Where the center of the image should be drawn on the canvas
                (self.size, self.size)  # Size of how the image should be drawn
            )


def draw(canvas):
    """
    Default draw handler for the simplegui frame
    """
    for square in squares:
        square.draw(canvas)


def click(pos):
    """
    Removes a queen when clicked
    Adds a queen to a Square if it is a legal move.
    """
    global squares
    clicked_square_index = None
    for idx, square in enumerate(squares):
        if square.is_in(pos):
            clicked_square_index = idx

    if clicked_square_index is not None:
        if squares[clicked_square_index].get_has_queen():
            squares[clicked_square_index].set_has_queen(False)
        else:
            squares[clicked_square_index].set_has_queen(True)


frame = simplegui.create_frame("N Queens", FRAME_SIZE[0], FRAME_SIZE[1])
frame.set_canvas_background("black")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# Create a test square
squares = []
padding_left = (FRAME_SIZE[0] - SQUARE_SIZE * BOARD_SIZE) // 2
padding_top = (FRAME_SIZE[1] - SQUARE_SIZE * BOARD_SIZE) // 2
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        color = "green" if ((i % 2 == 0 and j % 2 == 0) or i % 2 == 1 and j % 2 == 1) else "red"
        squares.append(Square(SQUARE_SIZE, (padding_left + j * SQUARE_SIZE, padding_top + i * SQUARE_SIZE), color,
                              False))  # include padding

frame.start()
