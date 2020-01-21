class Square:
    """
    A class for creating graphical squares.
    """
    def __init__(self, size, pos, color, has_queen=False):
        """
        Class constructor.
        """
        self.size = size
        self.pos = pos
        self.color = color
        self.has_queen = has_queen

    def get_has_queen(self):
        """
        Return True if this square has a queen, else False.
        """
        return self.has_queen

    def set_has_queen(self, val):
        """
        Set the has_queen property for this square.
        """
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

