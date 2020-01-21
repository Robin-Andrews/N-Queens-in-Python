# N-Queens

Check out using get_coords_from_grid() and get grid_from_coords() and/or implementing myself

An implementation of the classic N-Queens Problem using  codeskulptor or SimpleGUICS2Pygame

If submitted to Codereview stackexchange, include working codeskulptor URLs including imports. Mention weird bug where running a second time breaks the program in CS, but not the third, fifth time etc.

Add sound effects

Design decision re synchronising logical board and GUI

1: Have two board representations, a logical one and a graphical one and make sure they are always synced. Iterate through
a list of `Square` objects calling the draw method of each in turn within the draw handler.
2: Within the draw handler, draw the squares "from scratch" based on the logical board. Possibly use (imported) helper functions
to achieve this.

Investigation: what size of boards are solvable?








