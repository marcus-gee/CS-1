import nose
import string, sys
from midterm import *

#
# PART 2.
#

def test_draw_box():
    box1  = '\n+-+\n|x|\n+-+\n' 
    box2  = '\n+--+\n|xy|\n|o.|\n+--+\n' 
    box3  = '\n+---+\n|xyo|\n|.xy|\n|o.x|\n+---+\n'
    box4  = '\n+----+\n|xyo.|\n|xyo.|\n|xyo.|\n|xyo.|\n+----+\n' 
    box5  = '\n+-----+\n|xyo.x|\n|yo.xy|\n|o.xyo|\n|.xyo.|\n|xyo.x|\n+-----+\n' 
    box10 = '\n+----------+\n|xyo.xyo.xy|\n|o.xyo.xyo.|\n|xyo.xyo.xy|\n|o.xyo.xyo.|\n|xyo.xyo.xy|\n|o.xyo.xyo.|\n|xyo.xyo.xy|\n|o.xyo.xyo.|\n|xyo.xyo.xy|\n|o.xyo.xyo.|\n+----------+\n'

    assert draw_box(1)  == box1
    assert draw_box(2)  == box2
    assert draw_box(3)  == box3
    assert draw_box(4)  == box4
    assert draw_box(5)  == box5
    assert draw_box(10) == box10

def test_roll():
    for _ in range(1000):
        r = roll()
        assert type(r) is int
        assert r >= 2 and r <= 12

def test_craps():
    for _ in range(1000):
        c = craps(False)
        print(c)
        assert type(c) is bool

def test_remove_indices():
    lst = [3, 1, 4, 1, 5, 9, 2, 6]
    assert remove_indices(lst, [-10]) == lst
    assert remove_indices(lst, [-10]) is not lst   # check for copy
    assert remove_indices(lst, [8]) == lst
    assert remove_indices(lst, [8]) is not lst   # check for copy
    assert remove_indices(lst, [0]) == [1, 4, 1, 5, 9, 2, 6]
    assert remove_indices(lst, [1]) == [3, 4, 1, 5, 9, 2, 6]
    assert remove_indices(lst, [2]) == [3, 1, 1, 5, 9, 2, 6]
    assert remove_indices(lst, [3]) == [3, 1, 4, 5, 9, 2, 6]
    assert remove_indices(lst, [4]) == [3, 1, 4, 1, 9, 2, 6]
    assert remove_indices(lst, [5]) == [3, 1, 4, 1, 5, 2, 6]
    assert remove_indices(lst, [6]) == [3, 1, 4, 1, 5, 9, 6]
    assert remove_indices(lst, [7]) == [3, 1, 4, 1, 5, 9, 2]
    assert remove_indices(lst, [-1]) == [3, 1, 4, 1, 5, 9, 2]
    assert remove_indices(lst, [-2]) == [3, 1, 4, 1, 5, 9, 6]
    assert remove_indices(lst, [-8]) == [1, 4, 1, 5, 9, 2, 6]
    assert remove_indices(lst, [0, 1]) == [4, 1, 5, 9, 2, 6]
    assert remove_indices(lst, [0, 7]) == [1, 4, 1, 5, 9, 2]
    assert remove_indices(lst, [0, -1]) == [1, 4, 1, 5, 9, 2]
    assert remove_indices(lst, [0, 1, 7]) == [4, 1, 5, 9, 2]
    assert remove_indices(lst, [0, 1, -1]) == [4, 1, 5, 9, 2]
    assert remove_indices(lst, [0, 6, 7]) == [1, 4, 1, 5, 9]
    assert remove_indices(lst, [0, -2, -1]) == [1, 4, 1, 5, 9]

def test_get_bet_info():
    def make_indices_positive(bets, indices):
        nbets = len(bets)
        new_indices = []
        for index in indices:
            if index < 0:
                new_indices.append(nbets + index)
            else:
                new_indices.append(index)
        return new_indices

    def check_bet_info(bets, cwins, bet, indices):
        indices = make_indices_positive(bets, indices)
        (b, ix) = get_bet_info(bets, cwins)
        ix = make_indices_positive(bets, ix)
        assert b == bet
        ix.sort()
        indices.sort()
        assert ix == indices

    check_bet_info([10, 10, 15], 0, 10, [0])
    check_bet_info([10, 10, 15], 1, 25, [0, -1])
    check_bet_info([10, 10, 15], 2, 35, [0, 1, -1])

    check_bet_info([10, 15], 0, 10, [0])
    check_bet_info([10, 15], 1, 25, [0, -1])
    check_bet_info([10, 15], 2, 25, [0, -1])

    check_bet_info([15], 0, 15, [0])
    check_bet_info([15], 1, 15, [0])
    check_bet_info([15], 2, 15, [0])

    check_bet_info([1, 2, 3, 4, 5], 0, 1, [0])
    check_bet_info([1, 2, 3, 4, 5], 1, 6, [0, -1])
    check_bet_info([1, 2, 3, 4, 5], 2, 8, [0, 1, -1])

def test_make_one_bet():
    assert make_one_bet(1000, [10, 10, 15],  0, True) == \
      (1010, [10, 15], 1)
    assert make_one_bet(1000, [10, 10, 15],  0, False) == \
      (990, [10, 10, 15, 10], 0)
    assert make_one_bet(1000, [10, 10, 15],  1, True) == \
      (1025, [10], 2)
    assert make_one_bet(1000, [10, 10, 15],  1, False) == \
      (975, [10, 10, 15, 25], 0)
    assert make_one_bet(1000, [10, 10, 15],  2, True) == \
      (1035, [], 2)
    assert make_one_bet(1000, [10, 10, 15],  2, False) == \
      (965, [10, 10, 15, 35], 0)

    assert make_one_bet(1000, [10, 15],  0, True) == \
      (1010, [15], 1)
    assert make_one_bet(1000, [10, 15],  0, False) == \
      (990, [10, 15, 10], 0)
    assert make_one_bet(1000, [10, 15],  1, True) == \
      (1025, [], 2)
    assert make_one_bet(1000, [10, 15],  1, False) == \
      (975, [10, 15, 25], 0)
    assert make_one_bet(1000, [10, 15],  2, True) == \
      (1025, [], 2)
    assert make_one_bet(1000, [10, 15],  2, False) == \
      (975, [10, 15, 25], 0)

    assert make_one_bet(1000, [15],  0, True) == \
      (1015, [], 1)
    assert make_one_bet(1000, [15],  0, False) == \
      (985, [15, 15], 0)
    assert make_one_bet(1000, [15],  1, True) == \
      (1015, [], 2)
    assert make_one_bet(1000, [15],  1, False) == \
      (985, [15, 15], 0)
    assert make_one_bet(1000, [15],  2, True) == \
      (1015, [], 2)
    assert make_one_bet(1000, [15],  2, False) == \
      (985, [15, 15], 0)

    # Test inadequate bankroll check.
    assert make_one_bet(5, [10, 10, 15],  0, True) == \
      (5, [], 0)
    assert make_one_bet(5, [10, 10, 15],  0, False) == \
      (5, [], 0)
    assert make_one_bet(20, [10, 10, 15],  1, True) == \
      (20, [], 0)
    assert make_one_bet(20, [10, 10, 15],  1, False) == \
      (20, [], 0)
    assert make_one_bet(30, [10, 10, 15],  2, True) == \
      (30, [], 0)
    assert make_one_bet(30, [10, 10, 15],  2, False) == \
      (30, [], 0)


#
# PART 3.
#

def test_make_board():
    for i in range(100):
        b = make_board()
        assert type(b) is dict  # make_board() returns a dictionary
        assert len(b) == 2
        for key in b:
            assert type(key) is tuple
            assert len(key) == 2
            assert b[key] in [2, 4]
            (row, col) = key
            assert 0 <= row <= 3
            assert 0 <= col <= 3

def random_board():
    '''Create and return a random board.'''
    board = make_board()
    for i in range(100):
        move = random.choice('wasd')
        update(board, move)
        if game_over(board):
            break
    return board

def test_accessors():
    b = random_board()
    r0 = get_row(b, 0)
    r1 = get_row(b, 1)
    r2 = get_row(b, 2)
    r3 = get_row(b, 3)
    c0 = get_column(b, 0)
    c1 = get_column(b, 1)
    c2 = get_column(b, 2)
    c3 = get_column(b, 3)
    for item in [r0, r1, r2, r3, c0, c1, c2, c3]:
        assert type(item) is list
        assert len(item) == 4
        for elem in item:
            assert type(elem) is int
    put_row(b, [2, 4, 8, 16], 0)
    assert get_row(b, 0) == [2, 4, 8, 16]
    put_column(b, [4, 0, 0, 2], 2)
    assert get_column(b, 2) == [4, 0, 0, 2]
    assert (1, 2) not in b  # setting to 0 clears location
    assert (2, 2) not in b

def test_make_move_on_list():
    assert make_move_on_list([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert make_move_on_list([0, 4, 0, 8]) == [4, 8, 0, 0]
    assert make_move_on_list([8, 8, 2, 2]) == [16, 4, 0, 0]
    assert make_move_on_list([2, 2, 2, 2]) == [4, 4, 0, 0]
    assert make_move_on_list([2, 2, 4, 4]) == [4, 8, 0, 0]
    assert make_move_on_list([2, 4, 4, 0]) == [2, 8, 0, 0]
    assert make_move_on_list([2, 4, 4, 2]) == [2, 8, 2, 0]
    assert make_move_on_list([0, 0, 0, 16]) == [16, 0, 0, 0]
    assert make_move_on_list([2, 0, 0, 16]) == [2, 16, 0, 0]
    assert make_move_on_list([2, 0, 16, 0]) == [2, 16, 0, 0]
    assert make_move_on_list([2, 16, 0, 0]) == [2, 16, 0, 0]

def test_make_move():
    b = {(3, 2): 2, (2, 3): 2}
    make_move(b, 'w')
    assert b == {(0, 2): 2, (0, 3): 2}
    b = {(3, 2): 2, (2, 3): 2}
    make_move(b, 'd')
    assert b == {(2, 3): 2, (3, 3): 2}
    b = {(3, 2): 2, (2, 3): 2}
    make_move(b, 'a')
    assert b == {(2, 0): 2, (3, 0): 2} 
    b = {(3, 2): 2, (2, 3): 2}
    make_move(b, 's')
    assert b == {(3, 2): 2, (3, 3): 2} 
    make_move(b, 'a')
    assert b == {(3, 0): 4} 

def test_game_over():
    b = make_board()
    assert not game_over(b)
    b = {(0, 0): 2, (0, 1): 8, (0, 2): 4, (0, 3): 2, 
         (1, 0): 16, (1, 1): 64, (1, 2): 128, (1, 3): 4, 
         (2, 0): 4, (2, 1): 16, (2, 2): 32, (2, 3): 2, 
         (3, 0): 2, (3, 1): 8, (3, 2): 4, (3, 3): 8}
    assert game_over(b)

def test_update():
    for i in range(100):
        b = make_board()
        for c in 'wasd':
            b2 = b.copy()
            make_move(b, c)
            update(b2, c)
            if b != b2:               # if a number was added ...
                for loc in b:
                    del b2[loc]
                assert len(b2) == 1   # make sure it's only one number...
                assert list(b2.values())[0] in [2, 4]   # either 2 or 4

if __name__ == '__main__':
    nose.runmodule()

