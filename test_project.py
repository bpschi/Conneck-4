import pytest
import project
from project import GameBoard

def test_init_default():
    gb = GameBoard()
    assert gb.rows == 6
    assert gb.cols == 7
    assert gb.limit == 4

def test_init_limit():
    gb = GameBoard(limit = 3)
    assert gb.rows == 6
    assert gb.cols == 7
    assert gb.limit == 3

def test_init_size():
    gb = GameBoard(rows = 3, cols = 3)
    assert gb.rows == 3
    assert gb.cols == 3
    assert gb.limit == 3

def test_init_limit_beyond_board_size_3x3():
    with pytest.raises(AssertionError):
        gb = GameBoard(limit = 4)
        assert gb.rows == 3
        assert gb.cols == 3
        assert gb.limit == 4

def test_init_limit_beyond_board_size_3x6():
    with pytest.raises(AssertionError):
        gb = GameBoard(limit = 4)
        assert gb.rows == 3
        assert gb.cols == 6
        assert gb.limit == 7

def test_init_rows_invalid():
    gb = GameBoard(rows = -1)
    assert gb.rows == 6
    assert gb.cols == 7
    assert gb.limit == 4

def test_init_rows_beyond_max_rows():
    gb = GameBoard(rows = 25)
    assert gb.rows == 6
    assert gb.cols == 7
    assert gb.limit == 4

def test_init_cols_invalid():
    gb = GameBoard(cols = -1)
    assert gb.rows == 6
    assert gb.cols == 7
    assert gb.limit == 4

def test_init_cols_beyond_max_cols():
    gb = GameBoard(cols = 12)
    assert gb.rows == 6
    assert gb.cols == 7
    assert gb.limit == 4

def test_get_chains_at_c1r1():
    gb = GameBoard()
    chains = project.get_chains(gb, 1, 1)
    assert len(chains) == 2
    assert not any("S" in c for c in chains)
    assert any("E" in c for c in chains)
    assert any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert not any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c1r3():
    gb = GameBoard()
    chains = project.get_chains(gb, 1, 3)
    assert len(chains) == 2
    assert not any("S" in c for c in chains)
    assert any("E" in c for c in chains)
    assert any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert not any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c1r4():
    gb = GameBoard()
    chains = project.get_chains(gb, 1, 4)
    assert len(chains) == 3
    assert any("S" in c for c in chains)
    assert any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert any("SE" in c for c in chains)
    assert not any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c1r6():
    gb = GameBoard()
    chains = project.get_chains(gb, 1, 6)
    assert len(chains) == 3
    assert any("S" in c for c in chains)
    assert any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert any("SE" in c for c in chains)
    assert not any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c7r1():
    gb = GameBoard()
    chains = project.get_chains(gb, 7, 1)
    assert len(chains) == 2
    assert not any("S" in c for c in chains)
    assert not any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert any("W" in c for c in chains)
    assert any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c7r3():
    gb = GameBoard()
    chains = project.get_chains(gb, 7, 3)
    assert len(chains) == 2
    assert not any("S" in c for c in chains)
    assert not any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert any("W" in c for c in chains)
    assert any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c7r4():
    gb = GameBoard()
    chains = project.get_chains(gb, 7, 4)
    assert len(chains) == 3
    assert any("S" in c for c in chains)
    assert not any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert any("SW" in c for c in chains)

def test_get_chains_at_c7r6():
    gb = GameBoard()
    chains = project.get_chains(gb, 7, 6)
    assert len(chains) == 3
    assert any("S" in c for c in chains)
    assert not any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert any("SW" in c for c in chains)

def test_get_chains_at_c3r3():
    gb = GameBoard()
    chains = project.get_chains(gb, 3, 3)
    assert len(chains) == 2
    assert not any("S" in c for c in chains)
    assert any("E" in c for c in chains)
    assert any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert not any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c3r4():
    gb = GameBoard()
    chains = project.get_chains(gb, 3, 4)
    assert len(chains) == 3
    assert any("S" in c for c in chains)
    assert any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert any("SE" in c for c in chains)
    assert not any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c5r3():
    gb = GameBoard()
    chains = project.get_chains(gb, 5, 3)
    assert len(chains) == 2
    assert not any("S" in c for c in chains)
    assert not any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert any("W" in c for c in chains)
    assert any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c5r4():
    gb = GameBoard()
    chains = project.get_chains(gb, 5, 4)
    assert len(chains) == 3
    assert any("S" in c for c in chains)
    assert not any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert any("SW" in c for c in chains)

def test_get_chains_at_c4r3():
    gb = GameBoard()
    chains = project.get_chains(gb, 4, 3)
    assert len(chains) == 4
    assert not any("S" in c for c in chains)
    assert any("E" in c for c in chains)
    assert any("NE" in c for c in chains)
    assert not any("SE" in c for c in chains)
    assert any("W" in c for c in chains)
    assert any("NW" in c for c in chains)
    assert not any("SW" in c for c in chains)

def test_get_chains_at_c4r4():
    gb = GameBoard()
    chains = project.get_chains(gb, 4, 4)
    assert len(chains) == 5
    assert any("S" in c for c in chains)
    assert any("E" in c for c in chains)
    assert not any("NE" in c for c in chains)
    assert any("SE" in c for c in chains)
    assert any("W" in c for c in chains)
    assert not any("NW" in c for c in chains)
    assert any("SW" in c for c in chains)

def test_drop_one_chip_c1():
    gb = GameBoard()
    assert gb.next_turn() == gb.PLAYER_A
    success = project.drop_chip(gb, 1)
    assert success
    assert len(gb.moves) == 1
    assert gb.get_lastmove()["player"] == gb.PLAYER_A
    assert gb.get_lastmove()["c"] == 1
    assert gb.get_lastmove()["r"] == 1
    assert gb.get_player(1, 1) == gb.PLAYER_A
    assert gb.next_turn() == gb.PLAYER_B

def test_drop_one_chip_c7():
    gb = GameBoard()
    assert gb.next_turn() == gb.PLAYER_A
    success = project.drop_chip(gb, 7)
    assert success
    assert len(gb.moves) == 1
    assert gb.get_lastmove()["player"] == gb.PLAYER_A
    assert gb.get_lastmove()["c"] == 7
    assert gb.get_lastmove()["r"] == 1
    assert gb.get_player(7, 1) == gb.PLAYER_A
    assert gb.next_turn() == gb.PLAYER_B

def test_drop_one_chip_c0_invalid():
    gb = GameBoard()
    assert gb.next_turn() == gb.PLAYER_A
    assert not project.drop_chip(gb, 0)
    assert len(gb.moves) == 0
    assert gb.next_turn() == gb.PLAYER_A

def test_drop_one_chip_c8_invalid():
    gb = GameBoard()
    assert gb.next_turn() == gb.PLAYER_A
    assert not project.drop_chip(gb, 8)
    assert len(gb.moves) == 0
    assert gb.next_turn() == gb.PLAYER_A

def test_drop_one_chip_c1_column_full():
    gb = GameBoard()
    for _ in range(6):
        assert project.drop_chip(gb, 1)
    assert gb.next_turn() == gb.PLAYER_A
    assert len(gb.moves) == 6

def test_drop_one_chip_c1_column_already_full():
    gb = GameBoard()
    for _ in range(6):
        assert project.drop_chip(gb, 1)
    assert not project.drop_chip(gb, 1)
    assert gb.next_turn() == gb.PLAYER_A
    assert len(gb.moves) == 6

def test_drop_two_chips_c1c1():
    gb = GameBoard()
    assert gb.next_turn() == gb.PLAYER_A
    assert project.drop_chip(gb, 1)
    assert gb.next_turn() == gb.PLAYER_B
    assert project.drop_chip(gb, 1)
    assert len(gb.moves) == 2
    assert gb.get_lastmove()["player"] == gb.PLAYER_B
    assert gb.get_lastmove()["c"] == 1
    assert gb.get_lastmove()["r"] == 2
    assert gb.get_player(1, 2) == gb.PLAYER_B
    assert gb.next_turn() == gb.PLAYER_A

def test_drop_three_chips_c1c1c1():
    gb = GameBoard()
    assert gb.next_turn() == gb.PLAYER_A
    assert project.drop_chip(gb, 1)
    assert gb.next_turn() == gb.PLAYER_B
    assert project.drop_chip(gb, 1)
    assert gb.next_turn() == gb.PLAYER_A
    assert project.drop_chip(gb, 1)
    assert len(gb.moves) == 3
    assert gb.get_lastmove()["player"] == gb.PLAYER_A
    assert gb.get_lastmove()["c"] == 1
    assert gb.get_lastmove()["r"] == 3
    assert gb.get_player(1, 2) == gb.PLAYER_B
    assert gb.get_player(1, 3) == gb.PLAYER_A
    assert gb.next_turn() == gb.PLAYER_B

def test_drop_three_chips_c1c1c2():
    gb = GameBoard()
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    assert len(gb.moves) == 3
    assert gb.get_player(1, 1) == gb.PLAYER_A
    assert gb.get_player(1, 2) == gb.PLAYER_B
    assert gb.get_player(2, 1) == gb.PLAYER_A

def test_drop_three_chips_c1c2c2():
    gb = GameBoard()
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 2)
    assert len(gb.moves) == 3
    assert gb.get_player(1, 1) == gb.PLAYER_A
    assert gb.get_player(2, 1) == gb.PLAYER_B
    assert gb.get_player(2, 2) == gb.PLAYER_A

def test_drop_three_chips_c1c2c3():
    gb = GameBoard()
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 3)
    assert len(gb.moves) == 3
    assert gb.get_player(1, 1) == gb.PLAYER_A
    assert gb.get_player(2, 1) == gb.PLAYER_B
    assert gb.get_player(3, 1) == gb.PLAYER_A

def test_drop_one_chip_board_full():
    gb = GameBoard()
    for c, r in ((i, j) for i in range(1,8) for j in range(1,7)):
        assert project.drop_chip(gb, c)
    assert len(gb.moves) == 42

def test_drop_one_chip_board_already_full():
    gb = GameBoard()
    for c, r in ((i, j) for i in range(1,8) for j in range(1,7)):
        assert project.drop_chip(gb, c)
    assert len(gb.moves) == 42
    assert not project.drop_chip(gb, 1)
    assert gb.next_turn() == gb.PLAYER_A
    assert len(gb.moves) == 42

def test_find_winner_1x1_limit_1():
    gb = GameBoard(rows = 1, cols = 1, limit = 1)
    p = gb.next_turn()
    assert project.drop_chip(gb, 1)
    assert project.find_winner(gb) == p

def test_find_winner_2x2_limit_1():
    gb = GameBoard(rows = 2, cols = 2, limit = 1)
    p = gb.next_turn()
    assert project.drop_chip(gb, 1)
    assert project.find_winner(gb) == p

def test_find_winner_2x2_limit_2_win_row():
    gb = GameBoard(rows = 2, cols = 2, limit = 2)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 1)
    p = gb.next_turn()
    assert project.drop_chip(gb, 2)
    assert project.find_winner(gb) == p

def test_find_winner_2x2_limit_2_win_col():
    gb = GameBoard(rows = 2, cols = 2, limit = 2)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    p = gb.next_turn()
    assert project.drop_chip(gb, 1)
    assert project.find_winner(gb) == p

def test_find_winner_2x2_limit_2_win_diag():
    gb = GameBoard(rows = 2, cols = 2, limit = 2)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    p = gb.next_turn()
    assert project.drop_chip(gb, 2)
    assert project.find_winner(gb) == p

#W
def test_find_winner_3x3_limit_3_win_row_end():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 2)
    p = gb.next_turn()
    assert project.drop_chip(gb, 3)
    assert project.find_winner(gb) == p

#E #W
def test_find_winner_3x3_limit_3_win_row_mid():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 3)
    p = gb.next_turn()
    assert project.drop_chip(gb, 2)
    assert project.find_winner(gb) == p

#E
def test_find_winner_3x3_limit_3_win_row_front():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 3)
    p = gb.next_turn()
    assert project.drop_chip(gb, 1)
    assert project.find_winner(gb) == p

#S
def test_find_winner_3x3_limit_3_win_col_end():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    p = gb.next_turn()
    assert project.drop_chip(gb, 1)
    assert project.find_winner(gb) == p

#SW
def test_find_winner_3x3_limit_3_win_diag_fwd_end():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 3)
    p = gb.next_turn()
    assert project.drop_chip(gb, 3)
    assert project.find_winner(gb) == p

#SW #NE
def test_find_winner_3x3_limit_3_win_diag_fwd_middle():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 1)
    p = gb.next_turn()
    assert project.drop_chip(gb, 2)
    assert project.find_winner(gb) == p

#NE
def test_find_winner_3x3_limit_3_win_diag_fwd_front():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 2)
    p = gb.next_turn()
    assert project.drop_chip(gb, 1)
    assert project.find_winner(gb) == p

#SE
def test_find_winner_3x3_limit_3_win_diag_bkwd_front():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 1)
    p = gb.next_turn()
    assert project.drop_chip(gb, 1)
    assert project.find_winner(gb) == p

#SE #NW
def test_find_winner_3x3_limit_3_win_diag_bkwd_middle():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 3)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 3)
    p = gb.next_turn()
    assert project.drop_chip(gb, 2)
    assert project.find_winner(gb) == p

#NW
def test_find_winner_3x3_limit_3_win_diag_bkwd_end():
    gb = GameBoard(rows = 3, cols = 3, limit = 3)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 1)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 2)
    assert project.drop_chip(gb, 2)
    p = gb.next_turn()
    assert project.drop_chip(gb, 3)
    assert project.find_winner(gb) == p
