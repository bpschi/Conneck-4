# ConnecK 4 (A Variation of the Classic "Connect 4" Board Game)

This is the [Final Project](https://cs50.harvard.edu/python/2022/project/) submission for the [Harvard University](https://en.wikipedia.org/wiki/Harvard_University) online course [CS50P Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/).

#### Video Demo:  <https://youtu.be/WOiIaXku-YE>

## Description

ConnecK 4 is a [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) implementation of the classic board game [Connect 4](https://en.wikipedia.org/wiki/Connect_Four) in which two players, each representing a different color, take turns dropping their colored chips into a vertically-oriented, xy-axis grid game board from the top until a player wins by being the first to form a row, column, or diagonal chain of chips of their own color.

### Background

In the classic [Milton Bradley](https://en.wikipedia.org/wiki/Milton_Bradley_Company) board game Connect 4 from which ConnecK 4 takes inspiration, a *red* player and a *yellow* player compete to be the first to form a four-chip chain on a six-row, seven-column grid. It is a form of [m,n,k-game](https://en.wikipedia.org/wiki/M,n,k-game) where two players take turns placing a chip of their color on an *m-by-n* board and the winner is the first player who gets *k* chips of their own color in a row, column, or diagonal.

### ConnecK 4 Variation

ConnecK 4 *preserves* the same game logic as Connect 4 in that:
+ Two players alternate turns dropping a single chip of their own color into the game board.
+ A player selects a column to drop their chip, and chips can only be dropped from the top of the game board.
+ Columns are filled bottom-up, so a chip occupies the bottom-most row in an empty column, or the next bottom-most row if other chips are already present.
+ The game is won by the player who is first able to form a row, column, or diagonal chain of chips of their own color.
+ The game enters a draw when the game board is full but no player is able to form a row, column, or diagonal chain of chips of their own color.

ConnecK 4 *varies* from the game logic of Connect 4 in that:
+ Users can optionally set the number of rows in the game board from 1 to 24 prior to game start.
+ Users can optionally set the number of columns in the game board from 1 to 10 prior to game start.
+ Users can optionally set the number of chips (limit) that form a winning chain prior to game start, from 1 to the maximum of either the number of rows or the number of columns to ensure that a player has the opportunity to form a winning chain.
+ A color is randomly assigned to each player prior to game start, because red and yellow are boring.

## Implementation and Design Choices

The implementation of ConnecK 4 takes inspiration from how one might model real-world Connect 4 and generalized *m,n,-k-game* game play, while adhering to the basic requirements of the CS50P Final Project:
+ A class called *GameBoard* is implemented inside *project.py* which models and encapsulates a generic *m-by-n* game board absent of any game logic. The *GameBoard* class defines the following:
    + Two players represented as *PLAYER_A* and *PLAYER_B*, each with a randomly-assigned, non-overlapping chip color
    + Game board represented as a grid with *cols* columns and *rows* rows
    + *Limit* count representing the number of same-colored chips that form a winning chain
    + Default values for *rows*, *cols*, and *limit* to represent a classic Connect 4 game board if no overrides are provided
    + History of *moves* representing the sequence of plays made by each player
    + Various functions for *interacting* with the *GameBoard*:
        + *is_valid_location* and *is_valid_player* check for the validity of a coordinate (i.e., is it inside the game board) and the validity of a grid space (i.e., is it occupied by a player, or not yet in play?)

            ```python
            # is the grid coordinate valid and within the bounds of the GameBoard
            def is_valid_location(self, c, r):

            # is player a valid GameBoard player
            def is_valid_player(self, p):
            ```
        + *get_player* and *set_player* handle getting what occupies a specific grid coordinate (i.e., a player, or an open slot) and the inverse action of registering a player's chip and move in the grid coordinate and moves history respectively

            ```python
            # who is at this coordinate
            def get_player(self, c, r):

            # set this coordinate in play by the given player and register their move in the history
            def set_player(self, c, r, p):
            ```
        + *next_turn* and *get_lastmove* are helper functions to get the last move and determine which player has the next turn

            ```python
            # who's turn is it?
            def next_turn(self):

            # what was the last move played?
            def get_lastmove(self):
            ```
        + *draw_player* and *__draw_cell* render a player's chip or an empty cell in the game board

            ```python
            # render a player's chip
            def draw_player(self, p):

            # render a cell that could be empty or occupied by a player
            def __draw_cell(self, p):
            ```
        + *__str__* is overridden to render the *GameBoard* using a combination of ASCII and [emoji](https://pypi.org/project/emoji/) characters. The game header indicates the number of chips to win, and the footer indicates the turn number. The prompt asks the player to enter a column number to drop a chip.

            ![Default 6x7 Game Board](images/default_board.jpg)

+ 3 custom functions model and encapsulate the 3 primary actions of game play:
    + **Dropping a chip into a column**
        + This action is handled by the *drop_chip* custom function which accepts a *GameBoard* object instance, an integer column number, and a *GameBoard* player object fetched from the *GameBoard* instance to fill the play slot. The function calculates the next open position to place the chip, and checks to ensure that the column is valid and that the column isn't already full.

            ```python
            # returns True if the chip drop has been successful; False otherwise
            def drop_chip(gb: GameBoard, c: int, **kwargs)
            ```
    + **Searching for winning rows, columns, and diagonals**
        + This action is handled by the *get_chains* custom function which accepts a *GameBoard* object instance, and integer column and row numbers representing the grid coordinate from which to generate the row, column, and diagonal chains of chips to inspect for a win (i.e., same-colored chips). This emulates real-life human behavior, as the game play algorithm first inspects the last played position for a given player, followed by the last played position for that same player, and so on and so forth.

            ```python
            # returns all of the valid chains for inspection at a given grid coordinate
            def get_chains(gb: GameBoard, c: int, r: int)
            ```
        + Chains are represented as cardinal directions, and there are only 7 possible chains in the game given the logic of ConnecK 4:
            + "S" represents a "South" chain that only inspects chips directly below the current coordinates
            + "E" represents an "East" chain that only inspects chips directly to the right of the current coordinates
            + "W" represents a "West" chain that only inspects chips directly to the left of the current coordinates
            + "SE", "SW", "NE", and "NW" thus represent the diagonal chains to inspect starting from the current coordinates
        + The number of chips to form a winning chain is a property of the *GameBoard*, and this function utilizes that fact to ensure that only *valid* chains are inspected. For example, on a 6 row by 7 column board, the coodinate at row 2, column 2 for a limit size of 4, only the "East" chain is valid for inspection. The "West" and "South" chains are invalid at that position.

    + **Testing for a win**
        + This action is handled by the *find_winner* function which accepts a *GameBoard* object instance as its only parameter. Given the current state of the game, the function starts with the last player's move (i.e., *drop_chip*) and begins using *get_chain* on that player's sequence of moves -- in reverse sequence -- to test for a win. Thus, this function also emulates real-life human behavior, as only the player's *played* positions on the board are inspected, and this is more efficient than blindly checking for every possible sequence of chips at every coordinate on the grid which, on a large board, could be expensive.

            ```python
            # return the winning player, or None if no player has won yet
            def find_winner(gb: GameBoard)
            ```

## Project and File Structure

The project and file structure of ConnecK 4 follows the basic requirements of the CS50P Final Project:
+ The program is written entirely in *Python*
+ The program is written in a file called *project.py* which also contains the *GameBoard* class
+ The program contains a *main()* function, and 3 custom functions at the same indentation level as *main()*, in *project.py*
+ The program includes a test file called *test_project.py* which contains test functions prepended with "test_" for each of the 3 custom functions
+ Both *project.py* and *test_project.py* are located in the root of the project folder
+ Images for this README are contained in the *Images* folder in the root directory

## Dependencies

ConnecK 4 has four dependencies that may require package manager [pip] for installation:
+ [emoji 2.9.0](https://pypi.org/project/emoji/)

    ```bash
    pip install emoji
    ```
+ [inflect 7.0.0](https://pypi.org/project/inflect/)

    ```bash
    pip install inflect
    ```
+ [argparse 1.4.0](https://pypi.org/project/argparse/)

    ```bash
    pip install argparse
    ```
+ [pytest 7.4.4](https://pypi.org/project/pytest/) (only for the *test_project.py* test file)

    ```bash
    pip install pytest
    ```
+ random (comes built-in with Python)

## Usage

ConnecK 4 can be run from the terminal absent of any input arguments or a combination of arguments specifying the number of rows, columns, and / or limit size (i.e., number of same-color chips to form a winning chain). Given no arguments, ConnecK 4 will default to a standard Connect 4 game board with 6 rows and 7 columns.

```python
usage: project.py [-h] [-r R] [-c C] [-l L]

options:
  -h, --help  show this help message and exit
  -r R        Optional argument to set the number of rows on the game board. Values can range from 1 to 24. Default value is 6.
  -c C        Optional argument to set the number of columns on the game board. Values can range from 1 to 10. Default value is 7.
  -l L        Optional argument to set the number of chips to form a winning row, column, or diagonal. Values can be any whole greater than 1, but the game will automatically scale it down to the maximum of the nunmber of rows or columns to ensure that the game ensures a possible winner.
```

```python
# starts the game with the default 6x7 grid and 4 same-colored chips in a chain to win
python project.py
```

```python
# starts the game with a 4x4 grid and 3 same-colored chips in a chain to win
python project.py -r 4 -c 4 -l 3
```

## Gameplay Visuals

Below are representative visuals of ConnecK 4 gameplay illustrating various game board sizes and states.

![Examples of Game Play with Various Board Sizes and States](images/gameplay.jpg)

## Roadmap

Although this project was done as a completion requirement for CS50P, I would love to continue developing ConnecK 4 to experiment with implementing the following:
+ 1-player mode against Computer / AI using minimax, negamax, and other algorithms
+ N-player mode to allow for 3+ players

## Authors and acknowledgment

This project was entirely designed and coded by me, [Brian P. S. Chi](bpschi@gmail.com), as the Final Project for CS50P. I would like to thank Prof. David Malan for the outstanding lectures, courseware, and exercises. It was a thoroughly enjoyable and educational experience.
