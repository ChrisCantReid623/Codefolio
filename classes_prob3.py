"""
File: classes_prob3.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Long Project #5, This program models a multi-user dimension matrix.
"""

class Room:
    """ Models a room with four directional exits that allow movement
    between other rooms. Initially contains four directional None pointers.
    """
    def __init__(self):
        """ Sets the default fields for a room. Until the set_name() method
        is called, default room names are an empty string.
        """
        self._name = ''
        self.n = None
        self.s = None
        self.e = None
        self.w = None

    def get_name(self):
        """ Returns the name of the subject room object. """
        return self._name

    def set_name(self, name):
        """ Sets the name of the new room object. """
        self._name = name

    def collapse_room(self):
        """ Reassigns all outward and inward pointing linkages to the subject
        room to None.
        """
        north = self.n
        if north is not None:
            north.s = None
        self.n = None

        south = self.s
        if south is not None:
            south.n = None
        self.s = None

        east = self.e
        if east is not None:
            east.w = None
        self.e = None

        west = self.w
        if west is not None:
            west.e = None
        self.w = None

def scanner(grid, rows, columns, row_index, column_index):
    """ Performs the grid scanning. Modifies the room reference,
    then immediately modifies that directions' adjacent room's reference to
    form a bidirectional linkage.

    --- Parameters ---
    grid: a list, each element represents a room in a matrix map  structure
    rows: the vertical dimension of the matrix
    columns: the horizontal dimension of the matrix
    row_index: index of the current row in the matrix
    column_index: index of the current column, in the current row

    --- Return Values ---
    grid: a list, with the current room's bidirectional routes modified

    """
    #  Scanning North
    if row_index - 1 >= 0:
        grid[row_index][column_index].n = grid[row_index - 1][column_index]
        grid[row_index - 1][column_index].s = grid[row_index][column_index]

    #  Scanning South
    if row_index + 1 < rows:
        grid[row_index][column_index].s = grid[row_index + 1][column_index]
        grid[row_index + 1][column_index].n = grid[row_index][column_index]

    #  Scanning West
    if column_index - 1 >= 0:
        grid[row_index][column_index].w = grid[row_index][column_index - 1]
        grid[row_index][column_index - 1].e = grid[row_index][column_index]

    #  Scanning East
    if column_index + 1 < columns:
        grid[row_index][column_index].e = grid[row_index][column_index + 1]
        grid[row_index][column_index + 1].w = grid[row_index][column_index]

    return grid

def corners(grid, rows, columns, row_index, column_index):
    """ Modifies the outward facing directions to Null on a corner located
    room in the grid.

    --- Parameters ---
    grid: a list, each element represents a room in a matrix map  structure
    rows: the vertical dimension of the matrix
    columns: the horizontal dimension of the matrix
    row_index: index of the current row in the matrix
    column_index: index of the current column, in the current row

    --- Return Values ---
    grid: a list, with the current room's out-of-bounds routes modified
    """
    #  North West Corner
    if row_index == 0 and column_index == 0:
        grid[row_index][column_index].n = None
        grid[row_index][column_index].w = None
    #  North East Corner
    if row_index == 0 and column_index + 1 == columns:
        grid[row_index][column_index].n = None
        grid[row_index][column_index].e = None
    #  South West Corner
    if row_index + 1 == rows and column_index == 0:
        grid[row_index][column_index].w = None
        grid[row_index][column_index].s = None
    #  South East Corner
    if row_index + 1 == rows and column_index + 1 == columns:
        grid[row_index][column_index].e = None
        grid[row_index][column_index].s = None

    return grid

def perimeter(grid, rows, columns, row_index, column_index):
    """ This function traverses the grid structure, ensuring the outward
    facing directions rooms on the perimeter are pointing at None.

    --- Parameters ---
    grid: a list, each element represents a room in a matrix map structure
    rows: the vertical dimension of the matrix
    columns: the horizontal dimension of the matrix
    row_index: index of the current row in the matrix
    column_index: index of the current column, in the current row

    --- Return Values ---
    grid: a list, with the current room's necessary 'walls' modified
    """
    #  Sides
    if column_index == 0:
        grid[row_index][column_index].w = None
    if column_index + 1 == columns:
        grid[row_index][column_index].e = None

    # Top and Bottom
    if row_index == 0:
        grid[row_index][column_index].n = None
    if row_index + 1 == rows:
        grid[row_index][column_index].s = None

    return grid

def link_grid(grid):
    """ Controls the nested loop for traversing each room in the grid.

    --- Parameters ---
    grid: a list, each element represents a room in a matrix map structure,
    no room linkages have been made

    --- Return Values ---
    sw_corner: a pointer to the grid location of room in the south-west corner
    """
    rows = len(grid)
    columns = len(grid[0])

    for row_index in range(rows):
        for column_index in range(columns):
            grid = perimeter(grid, rows, columns, row_index, column_index)
            grid = corners(grid, rows, columns, row_index, column_index)
            grid = scanner(grid, rows, columns, row_index, column_index)

    sw_corner = grid[rows - 1][0]
    return sw_corner

def build_grid(wid, hei):
    """ Creates a 2-dimensional matrix. Each element is a room object. Each
    room maintains four reference pointers. A function is then called to
    create the linkages between rooms objects.

    --- Parameters ---
    wid: the horizontal dimension of the matrix
    hei: the vertical dimension of the matrix

    --- Return Values ---
    sw_corner: a pointer to the grid location of room in the south-west corner
    """
    grid = []

    for row in range(hei):
        row_of_rooms = []
        for column in range(wid):
            new_room = Room()
            new_room.set_name(f'{column}, {row}')
            row_of_rooms.append(new_room)
        grid.append(row_of_rooms)
    sw_room = link_grid(grid)
    return sw_room