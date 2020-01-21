board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]


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

    
