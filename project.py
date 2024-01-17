import emoji
import inflect
import random
import argparse

# Class represents an m row x n column game board grid for two players with randomly assigned chip colors at start
# Limit size represents the number of chips chained together in a single row, column, or diagnoal to form a win
# Game board grid size can range from 1 x 1 up to 24 x 10; users can override the limit size and the number of rows and columns
# By default, the class instantiates a classic 6 x 7 "Connect 4" game board with limit 4
# The game board itself has no embedded "game logic"; the limit size is only used to ensure that a winner can be produced
# Valid player moves/plays are automatic tracked

class GameBoard:

    # Shuffle from valid emoji circle colors and pop two entries to assign to the two players
    random.shuffle(PLAYER_COLORS := ["red", "orange", "yellow", "green", "blue", "purple", "brown"])
    PLAYER_A = (1, PLAYER_COLORS.pop())
    PLAYER_B = (2, PLAYER_COLORS.pop())

    # Define game board row constraints and defaults
    MIN_ROWS = 1
    MAX_ROWS = 24
    DEFAULT_ROWS = 6

    # Define game board column constraints and defaults
    MIN_COLS = 1
    MAX_COLS = 10
    DEFAULT_COLS = 7

    # Define game board default limit size
    DEFAULT_LIMIT = 4

    # Initialize game board with user-defined row, column, and limit sizes, or use default
    # As it is easier to operate the game board using cartesian coordinates, row indexes are created in reverse
    # (e.g., row 6 is the top-most row, and row 1 is the bottom-most row, with columns 1 thru 7 going left to right)
    def __init__(self, **kwargs):

        # Board is constructed as a dict of lists, with rows as dict keys, and lists sized to game board columns
        self.board = {}

        # Moves history is constructed as a linear list
        self.moves = []

        # Do the assignment of rows, columns, and limit, using defaults if no arguments provided
        self.rows = kwargs.get("rows", GameBoard.DEFAULT_ROWS)
        self.cols = kwargs.get("cols", GameBoard.DEFAULT_COLS)
        self.limit = kwargs.get("limit", GameBoard.DEFAULT_LIMIT)
        for i in reversed(range(0, self.rows)):
            self.board[i+1] = [ None for _ in range(self.cols) ]

    # Generate the output string to render the game header, grid header, and game board grid
    # Function utlizes the emoji library to generate empty space (white circles) and player moves (colored circles)
    def __str__(self):
        # Clear the screen
        print(end="\033c", flush=True)

        # Render the game header to output string
        s = f"-- Connect {self._limit} --\n\n"

        # Render the grid header to output string
        for i in range(1, self._cols + 1):
            s += emoji.emojize(f":{inflect.engine().number_to_words(i)}:", language='alias') + " "
        s += f"\n{emoji.emojize(":red_triangle_pointed_down:", language='alias') * self._cols}\n"

        # Render the grid to output string
        for r, c in self._board.items():
            for i in c:
                s += self.__draw_cell(i)
            s += "\n"

        # Return the output string
        return s

    # Define the rows property for the game board
    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, rows):
        if rows is None or rows not in range(GameBoard.MIN_ROWS, GameBoard.MAX_ROWS+1): rows = GameBoard.DEFAULT_ROWS
        self._rows = rows

    # Define the cols property for the game board
    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, cols):
        if cols is None or cols not in range(GameBoard.MIN_COLS, GameBoard.MAX_COLS+1): cols = GameBoard.DEFAULT_COLS
        self._cols = cols

    # Define the limit property for the game board
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        if limit is None: limit = GameBoard.DEFAULT_LIMIT
        if not self.is_valid_location(limit, limit): limit = max(self._rows, self._cols)
        self._limit = limit

    # Define the board property for the game board
    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    # Define the moves property for the game board
    @property
    def moves(self):
        return self._moves

    @moves.setter
    def moves(self, moves):
        self._moves = moves

    # Function checks the validity of a grid coordinate given its row and column position
    def is_valid_location(self, c, r):
        return (1 <= c <= self._cols and 1 <= r <= self._rows)

    # Function checks whether an object is a game board player; this is used to check the state of a grid coordinate
    def is_valid_player(self, p):
        return (p in (GameBoard.PLAYER_A, GameBoard.PLAYER_B))

    # Function gets the state of a grid coordinate given its row and column position
    def get_player(self, c, r):
        if self.is_valid_location(c, r): return self._board[r][c-1]

    # Function sets the state of a grid coordinate given its row and column position
    # If the coordinate is valid (i.e., open and not played), assign the state and add the move to the history
    def set_player(self, c, r, p):
        if self.is_valid_location(c, r) and self.is_valid_player(p):
            self._board[r][c-1] = p
            self._moves.append({"c": c, "r": r, "player": p})

    # Function returns the next player given the history of moves
    def next_turn(self):
        return GameBoard.PLAYER_A if (len(self._moves) + 1) % 2 == GameBoard.PLAYER_A[0] else GameBoard.PLAYER_B

    # Function returns the last move played from the history
    def get_lastmove(self):
        return self._moves[-1] if len(self._moves) >= 1 else None

    # Function returns the output string of a player
    def draw_player(self, p):
        if self.is_valid_player(p): return emoji.emojize(f":{p[1]}_circle:", language='alias')

    # Function returns the output string of a cell (default) or a player
    def __draw_cell(self, p):
        return self.draw_player(p) if self.is_valid_player(p) else emoji.emojize(":white_circle:", language='alias')

# Function returns the "chains" of adjacent chips to inspect to inspect for a win, given a starting coordinate
# Function emulates how a real person would play Connect-4 e.g. do I have a row, column, or diagonal of chips to inspect
# The logic that dictates how many chips make a win (i.e., limit size) is defined outside as part of the game board itself
# To ease understanding, the "chains" are expressed as cardinal directions, with South ("S") pointing down
# Thus, given a starting coordinate and the board's grid and limit sizes, this function only builds up valid chains to inspect
def get_chains(gb: GameBoard, c: int, r: int):
    chains = dict()
    if r >= gb.limit: chains["S"] = [(0,-1), set()]
    if c >= gb.limit: chains["W"] = [(-1,0), set()]
    if c >= gb.limit and gb.rows - r + 1 >= gb.limit: chains["NW"] = [(-1,1), set()]
    if c >= gb.limit and r >= gb.limit: chains["SW"] = [(-1,-1), set()]
    if gb.cols - c + 1 >= gb.limit: chains["E"] = [(1,0), set()]
    if gb.cols - c + 1 >= gb.limit and gb.rows - r + 1 >= gb.limit: chains["NE"] = [(1,1), set()]
    if gb.cols - c + 1 >= gb.limit and r >= gb.limit: chains["SE"] = [(1,-1), set()]
    return chains

# Function returns the winning player on the game board, or None if none could be found
# Function emulates how a real person would play Connect-4 e.g., do I have a winning row, column, or diagonal given my moves
# Function only targets the player's current and previous moves, ignoring the other player, and ignores cells not yet in play
def find_winner(gb: GameBoard):
    found = False
    for move in gb.moves[gb.get_lastmove()["player"][0]-1::2]:
        chains = get_chains(gb, move["c"], move["r"])
        for i in range(0, gb.limit):
            p = None
            for direction in list(chains.keys()):
                p = gb.get_player(move["c"]+i*chains[direction][0][0], move["r"]+i*chains[direction][0][1])
                if gb.is_valid_player(p):
                    chains[direction][1].add(p[1])
                else:
                    del chains[direction]
        for direction in list(chains.keys()):
            if len(chains[direction][1]) == 1:
                found = True
                break
        if found: break
    return gb.get_lastmove()["player"] if found else None

# Function returns a bool based on whether or not a play (i.e., dropping a chip in a valid column) has been successful
# Function emulates how a real person would play Connect-4 e.g., I can drop a chip in a column where there's still space
def drop_chip(gb: GameBoard, c: int, **kwargs):
    p = kwargs.get("p", gb.next_turn())
    if not gb.is_valid_location(c, 1) or not gb.is_valid_player(p): return False
    for r in range(1, gb.rows+1):
        if not gb.is_valid_player(gb.get_player(c, r)):
            gb.set_player(c, r, p)
            break
        elif r == gb.rows and gb.is_valid_player(gb.get_player(c, r)):
            return False
    return True

# Main function instantiates the Connect-4 gameboard to default or user-specific grid and limit sizes parsed by argparse
# Function emulates the bare minimum a person does to play Connect-4, i.e.:
# 1. I will drop one of my chips in one of the columns on the game board
# 2. I will check if my chips have formed any winning row, column, or diagonal
# 3. I win the game if I pass the check, or I will pass the turn to the other player
# Game will continue to prompt user until a valid and numerical column number is entered
# Game will exit if user inputs anything non-numerical
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-r", help="Optional argument to set the number of rows on the game board. Values can range from 1 to 24. Default value is 6.", type=int)
    ap.add_argument("-c", help="Optional argument to set the number of columns on the game board. Values can range from 1 to 10. Default value is 7.", type=int)
    ap.add_argument("-l", help="Optional argument to set the number of chips to form a winning row, column, or diagonal. Values can be any whole greater than 1, but the game will automatically scale it down to the maximum of the nunmber of rows or columns to ensure that the game ensures a possible winner.", type=int)
    args = ap.parse_args()

    gb = GameBoard(rows = args.r, cols = args.c, limit = args.l)
    winner = None
    error = False
    while True:
        try:
            # Render the game board in its current state
            print(gb)

            # Get the column number from the user, and drop a chip in that column
            if not drop_chip(gb, int(input(f"--- Turn {len(gb.moves)+1} ---\n\nDrop {gb.draw_player(gb.next_turn())} in: "))): continue

            # Check if I won, but only after enough moves have been made for any player to have formed a winning row, column, or diagonal
            if (len(gb.moves) >= gb.limit * 2 - 1):
                winner = find_winner(gb)

            # If I am the winner, or if I have reached the maximum plays allowed by the grid, exit the game
            if winner is not None or (len(gb.moves) == gb.rows * gb.cols): break

        except Exception as e:
            # Something went wrong but not implementing boundary cases on key inputs
            error = False
            continue

    # Render the game board in its final state
    print(gb)

    # Render the winner, or tell me that an error has occured and the game exited prematurely
    print(f"-- {gb.draw_player(gb.get_lastmove()["player"])} wins! --\n") if winner is not None else print(f"--- {"Error" if error else "Draw"}! ---\n")

# Boilerplate
if __name__ == "__main__":
    main()
