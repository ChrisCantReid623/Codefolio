"""
File: maze_solver.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: This program will read a map up from a file, build a tree to
         represent the maze, and then search through the tree to find the
         path from the start to the end.
"""


def main():
    try:
        map_file_name = input()
        maze_file = open(map_file_name, 'r')
        maze_lines = error_checker(maze_file)
        if not maze_lines:
            return
    except FileNotFoundError:
        print('ERROR: Could not open file: NO_SUCH_FILE')
        return

    cells, start_pt, end_pt = generate_cells(maze_lines)
    maze_tree = create_tree(set(cells), set(), start_pt)
    path = [start_pt] + dump_solution(maze_tree, end_pt)

    command_handler(maze_lines, cells, maze_tree, start_pt, end_pt, path)


def error_checker(maze):
    """ Combines lines of txt file into single line. Iterates each character
    checking for specific parameters. Ends program and reports errors when
    identified.

    Parameters:
        maze: the maze file
    """
    lines = maze.readlines()
    combined = ''.join(lines)
    start_here = 'S'
    exit_here = 'E'
    char_restrictions = [' ', '\n', '#', start_here, exit_here]

    for char in combined:
        if char not in char_restrictions:
            print('ERROR: Invalid character in the map')
            return
    if combined.count(start_here) == 0 or combined.count(exit_here) == 0:
        print('ERROR: Every map needs exactly one START and exactly one END '
              'position')
        return
    elif combined.count(start_here) > 1:
        print('ERROR: The map has more than one START position')
        return
    elif combined.count(exit_here) > 1:
        print('ERROR: The map has more than one END position')
        return
    return lines


def command_handler(maze_lines, cells, maze_tree, start_pt, end_pt, path):
    """ Performs a variety of data processing sub-functions based on specific
     user command input.

     Parameters:
         maze_lines: the lines from the maze txt file
         cells: a list, contains (x,y) coordinates of the walkable maze spaces
         maze_tree: the tree representation of the maze
         start_pt: the (x,y) coord of the start point
         end_pt: the (x,y) coord of the end point
         path: the (x,y) solution sequence from the starting point to the end
    """
    command = input()
    if command == 'dumpCells':
        print('DUMPING OUT ALL CELLS FROM THE MAZE:')
        dump_cells(cells, start_pt, end_pt)
    elif command == 'dumpTree':
        print('DUMPING OUT THE TREE THAT REPRESENTS THE MAZE:')
        dump_tree(maze_tree)
    elif command == 'dumpSolution':
        print('PATH OF THE SOLUTION:')
        for item in path:
            print(f'  {item}')
    elif command == 'dumpSize':
        print('MAP SIZE:')
        dump_size(cells)
    elif command == '':
        print('SOLUTION:')
        print_solution(path, maze_lines)
    else:
        print('ERROR: Unrecognized command NOT_A_VALID_COMMAND')


def generate_cells(maze_lines):
    """ Generates the (x,y) coordinate pair locations of every walkable
    cell in the maze.

    Parameters:
        maze_lines: a list, contains the lines of the maze txt file
    """
    coordinates = []
    start = None
    end = None

    y_val = 0
    for line in maze_lines:
        x_val = 0
        for cell in line:
            if cell == 'S':
                start = x_val, y_val
            elif cell == 'E':
                end = x_val, y_val
            if cell != ' ' and cell != '\n':
                coordinates.append((x_val, y_val))
                x_val += 1
            else:
                x_val += 1
        y_val += 1
    return coordinates, start, end


def dump_cells(cells, start, end):
    """ Displays the coordinate pairs of every cell.

    Parameters:
        cells: a list, contains the (x,y) coord pairs
        start: the (x,y) coord of the start of the maze
        end: the (x,y) coord of the exit of the maze
    """
    for coord in sorted(cells):
        if coord == start:
            print(f'  {coord}    START')
        elif coord == end:
            print(f'  {coord}    END')
        else:
            print(f'  {coord}')


class MazeNode:
    """ Represents a walkable location in the maze. The constructor determines
    the stores the value field, represent by tuples containing (x,y)
    coordinate pairs. The children field is a list containing pointers to
    child nodes. """
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_pointer(self, val):
        """ Adds a pointer to the list containing pointers to 'child' nodes

        Parameters:
            val: the value stored in the node
        """
        self.children.append(val)


def create_tree(cells, handled, maze_root):
    """ Recursively creates a tree representation of the maze where the
     start of the maze is the root of the tree. Adjacent nodes are stored
     as children nodes.

     Parameters:
         cells: a list, contains the (x,y) coordinate pairs of the maze
                locations
         handled: a set, used to store values for nodes already created
         maze_root: initiated as the start point (x,y)
     """
    root = MazeNode(maze_root)
    handled.add(maze_root)

    up = (root.val[0]), (root.val[1] - 1)
    down = (root.val[0]), (root.val[1] + 1)
    left = (root.val[0] - 1), (root.val[1])
    right = (root.val[0] + 1), (root.val[1])

    # North/Up Pointer
    if up in cells and up not in handled and up is not None:
        root.add_pointer(create_tree(cells, handled, up))
    else:
        root.add_pointer(None)
    # South/Down Pointer
    if down in cells and down not in handled and down is not None:
        root.add_pointer(create_tree(cells, handled, down))
    else:
        root.add_pointer(None)
    # West/Left Pointer
    if left in cells and left not in handled and left is not None:
        root.add_pointer(create_tree(cells, handled, left))
    else:
        root.add_pointer(None)
    # East/ Right Pointer
    if right in cells and right not in handled and right is not None:
        root.add_pointer(create_tree(cells, handled, right))
    else:
        root.add_pointer(None)

    return root


def dump_tree(maze_tree, indent=""):
    """ Prints out tree node values in pre-order.

    Parameters:
        maze_tree: the 'root' of the tree containing the (x,y) coordinates of
                    the maze
        indent: string used to separate output
    """
    print(f'  {indent}{maze_tree.val}')
    if maze_tree is None:
        return
    else:
        for child in maze_tree.children:
            if child is not None:
                dump_tree(child, indent + '| ')


def dump_solution(root, end_point):
    """ Traverses the maze tree, searching for the endpoint. Recursively
    creates a list containing the node values on the backtracking to the
    start node.

    Parameters:
         root: references the root of the maze tree
         end_point: the value contained in the maze exit
     """
    if root is None:
        return None
    elif root.val == end_point:
        return []
    else:
        for child in root.children:
            answer = dump_solution(child, end_point)
            if answer is not None:
                return [child.val] + answer
    return


def dump_size(cells):
    """ Outputs the width and height of the maze maxtrix.

     Parameters:
         cells: a list, contains the (x,y) coordinate pairs of the maze
                locations
     """
    x_vals = set()
    y_vals = set()
    for cell in cells:
        x_vals.add(cell[0])
        y_vals.add(cell[1])

    print(f'  wid: {max(x_vals) + 1}')
    print(f'  hei: {max(y_vals) + 1}')


def print_solution(path, lines):
    """ Identifies the maze solution by replacing the maze characters with
     periods.

     Parameters:
         path: the (x,y) solution sequence from the starting point to the end
         lines: the lines of the maze txt file to be modified
         """
    path = path[1:-1]

    two_d_array = []

    y_val = 0
    for line in lines:
        cells = []
        x_val = 0
        for cell in line:
            if (x_val, y_val) in path:
                cells.append('.')
                x_val += 1
            else:
                cells.append(cell)
                x_val += 1
        two_d_array.append(''.join(cells))
        y_val += 1

    for lines in two_d_array:
        print(lines, end='')


main()
