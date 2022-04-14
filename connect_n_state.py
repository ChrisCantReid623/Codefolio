"""
File: connect_n_state.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Long Project #, models a Connect-4 variant where the target number of
consecutive pieces and board dimensions can vary.
"""

class Connect_N_State:
    """ Stores information on the status of a current came of Connect N. """
    def __init__(self, wid, hei, target, players):
        """ Constructor sets the default fields for the game. Uses a 2D list
        to track players' moves. """
        self._width = wid
        self._height = hei
        self._target = target
        self._players = players
        self._turn = 0

        self._grid = []
        for i in range(hei):
            column = []
            for j in range(wid):
                column.append('.')
            self._grid.append(column)

    def get_size(self):
        """ Returns the dimensions of the game matrix. """
        return self._width, self._height

    def get_target(self):
        """ Returns the number of tokens needed in a row to win. """
        return self._target

    def get_player_list(self):
        """ Returns the list containing the list of players. """
        return self._players

    def is_board_full(self):
        """ Checks for the existence of a period in the top row of the
        matrix. A full game board will have no confirmed finds.

        ---Return Values--
        True:  the top row has no empty slots
        False: the top row has empty slots
        """
        if '.' in self._grid[0]:
            return False
        else:
            return True

    def is_column_full(self, col):
        """ Checks the top row of the grid at the subject
        column. A full column will not contain a period.

        --- Parameters ---
        col: an integer, the subject column

        --- Return Values ---
        True: the column is full
        False: the column is NOT full
        """
        if 0 <= col <= len(self._grid[0]):
            if self._grid[0][col] == '.':
                return False
            else:
                return True
        else:
            return False

    def get_cell(self, x_val, y_val):
        """ Returns the value at a target given by grid coordinates.

        --- Parameters ---
        y_val: controls the row search
        x_val: controls the column search
        """
        column = x_val
        row = self._height - y_val - 1
        if self._grid[row][column] != '.':
            return self._grid[row][column]
        else:
            return None

    def get_cur_player(self):
        """ Returns the name of the player that will move next. """
        self._turn = self._turn % len(self._players)
        return self._players[self._turn]

    def move(self, col):
        """ Checks first if the chosen row is empty. Iterates the grid,
        replacing the first empty spot in the column with the player's
        token. Each move is then tested for meeting the winning
        requirements. Player turns restart after every player has gone.

         --- Parameters---
        col: an integer, the subject column
         """
        self._turn = self._turn % len(self._players)

        token = self._players[self._turn]

        full_column = self.is_column_full(col)
        if full_column:
            return False
        else:
            if 0 <= col <= len(self._grid[0]):
                for row in self._grid[::-1]:
                    if row[col] == '.':
                        row[col] = token
                        self._turn += 1
                        return True
            else:
                return False

    def print(self):
        """ Displays the current state of the grid. """
        for row in self._grid:
            col_index = 0
            for col in row:
                if col != '.':
                    row[col_index] = col[0]
                col_index += 1
            print(''.join(row))

    def is_game_over(self):
        """ Ends the game if the grid is full. """
        if self.is_board_full():
            return True
        elif self.winning_move():
            return True
        else:
            return False

    def get_winner(self):
        """ Outputs the name of the player that made the winning move. """
        if self.is_board_full():
            return None
        else:
            return str(self.get_cur_player())

    def winning_move(self):
        """ Checks if the last made move results in a win. """
        self._turn = self._turn % len(self._players)
        token = self._players[self._turn]


        if self.horizontal(token) or \
                self.vertical(token) or \
                self.diagonal_pos(token) or \
                self.diagonal_neg(token):
            return True
        else:
            return False

    def horizontal(self, token):
        """ Checks if a winning move was made horizontally. """
        consec = 0

        # Checking for horizontal tiles
        for row in range(len(self._grid)):
            for column in range(len(self._grid[0])):
                found = set()
                for count in range(self._target):
                    if not (row >= 0 and (column + count) < len(self._grid[0])):
                        found = set()
                    if row >= 0 and (column + count) < len(self._grid[0]):
                        if self._grid[row][column + count] == token[0]:

                            consec += 1
                        else:
                            consec = 0
                        found.add(self._grid[row][column + count])
                        #print(found, 'horizontal')
                if len(found) == 1 and '.' not in found:
                    return True
                if consec == self._target:
                    return True
        return False

    def vertical(self, token):
        """ Checks for a win in the vertical direction. """
        consec = 0

        # Checking for vertical tiles
        for row in range(len(self._grid)):
            for column in range(len(self._grid[0])):
                found = set()
                for count in range(self._target):
                    if not (0 <= (row + count) < len(self._grid) and column < len(
                            self._grid[0])):
                        found = set()
                    if 0 <= (row + count) < len(self._grid) and column < len(
                            self._grid[0]):

                        if self._grid[row + count][column] == token[0]:
                            consec += 1
                        else:
                            consec = 0
                        found.add(self._grid[row + count][column])
                #print(found, 'vertical')
                if len(found) == 1 and '.' not in found:
                    return True
                if consec == self._target:
                    return True
        return False

    def diagonal_pos(self, token):
        """ Checks for a win diagonally with a positive slope. """
        consec = 0

        # Check diagonal positive slope (/)
        for row in range(len(self._grid)):
            for column in range(len(self._grid[0])):
                found = set()
                for count in range(self._target):
                    if not (0 <= (row + count) < len(self._grid) and (column + count) < len(self._grid[0])):
                        found = set()
                    if 0 <= (row + count) < len(self._grid) and (column + count) < len(self._grid[0]):
                        if self._grid[row + count][column + count] == token[0]:
                            consec += 1
                        else:
                            consec = 0
                        found.add(self._grid[row + count][column + count])
                        #print(found, 'diag pos')
                if len(found) == 1 and '.' not in found:
                    return True
                if consec == self._target:
                    return True
        return False

    def diagonal_neg(self, token):
        """ Checks for a win diagonally with a negative slope. """
        consec = 0
        #print("NEGATIVE")
        # Check diagonal negative slope (\)
        for row in range(len(self._grid)):
            for column in range(len(self._grid[0])):
                found = set()
                for count in range(self._target):
                    if not (0 <= (row + count) < len(self._grid) and 0 <= (column - count) < len(self._grid[0])):
                        found = set()
                    if 0 <= (row + count) < len(self._grid) and 0 <= (column - count) < len(self._grid[0]):
                        if self._grid[row + count][column - count] == token[0]:
                            #print("      LEFT CHECK")
                            consec += 1
                        else:
                            consec = 0
                        found.add(self._grid[row + count][column - count])
                        #print(found, 'diag neg')
                if len(found) == 1 and '.' not in found:
                    return True
                if consec == self._target:
                    return True
        return False


'''game = Connect_N_State(7,6, 4, ["Red", "Yellow"])

moves = [1,2,1,3,1,3,1]

for x in moves:
    game.move(x)
    game.print()
    print(game.is_game_over())'''

