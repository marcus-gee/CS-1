
# Name: Marcus Gee
# Login: mcgee

# ---------------------------------------------------------------------- 
# Part 1: Pitfalls
# ---------------------------------------------------------------------- 

# Problem 1.1
# First in the argument of the function being defined, lst is input as a string,
# but it should have no quotes. Second, the docstring only has two single quotes
# on either side of it when it should have three. Next, the while loop should 
# have a colon after the boolean expression. Fourth, there is unnecessary spaces
# between lines in the code. Lastly, the code has result.append(item) and reurn 
# result twice, when it should only be there once at the end.

# Problem 1.2
# In the first function, we want it to return True if the input is a palindrome,
# but all the function does is print lst == lst.reverse() it doesnt return True.
# Second, you should define s as input(). Instead put s as the argument when 
# writing the function name and define s as '', an empty string. In the for loop
# at the end, the second comment is unnecessary. Next, you do not need both the 
# lists palindromes and ps, they are both the same and contain the same elements
# thus you can get rid of palindromes and just return ps.Lastly, you should 
# close the file after you have returned the palindrome list.

# Problem 1.3
# First, the function is named poorly. Second, the docstring should be inside 
# two sets of triple quotes and should be more descriptive of the function. Next
# there is poor operator spacing between =, +, and * operators. On the third
# line after the doctstrig, there is unnecessary extra spacing. On the lines \
# following the elif statement there is extra indentation. Also, the first line
# after the elif statment is longer than 80 characters. Lastly the first lines
# after the if and elif statement should read j+= not j=.

# ---------------------------------------------------------------------- 
# Part 2: Simple functions.
# ---------------------------------------------------------------------- 

import random, sys

#
# Problem 2.1
#

def draw_box(n):
    '''

    Return a string which, if printed, would draw a box on the terminal.  The
    exterior of the box should be made from '+' '-' and '|' characters.  The
    interior will have dimensions nxn and the characters will be one of the
    characters 'x', 'y', 'o', or '.', which will occur in order (even between
    lines).  There is a blank line before and after the box contents in the
    returned string.

    Examples:

    >>> print(draw_box(1))

    +-+
    |x|
    +-+

    >>> print(draw_box(2))

    +--+
    |xy|
    |o.|
    +--+

    >>> print(draw_box(3))

    +---+
    |xyo|
    |.xy|
    |o.x|
    +---+

    >>> print(draw_box(4))

    +----+
    |xyo.|
    |xyo.|
    |xyo.|
    |xyo.|
    +----+

    >>> print(draw_box(5))

    +-----+
    |xyo.x|
    |yo.xy|
    |o.xyo|
    |.xyo.|
    |xyo.x|
    +-----+

    >>> print(draw_box(10))

    +----------+
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    +----------+

    Arguments:
      n -- a positive integer representing the side length of the box.

    Return value: none.
    '''
def draw_box(n): # code only works if n is a product of 4
    assert n > 0
    top = '\n+' + n*'-' + '+\n'
    bottom = '+' + n*'-' + '+\n'
    side = '|'
    whole = int(n**2 / 4)
    decimal = (n**2 % 4)
    
    extra = ''
    if decimal == 1:
        extra = 'x'
    elif decimal == 2:
        extra = 'xy'
    elif decimal == 3:
        extra = 'xyo'    
        
    contents = whole*'xyo.' + extra
    
    box = top 
    
    for i in range(0, len(contents), n):
        box += side 
        box += contents[i:i+n]
        box += side 
        box += '\n'
        
    box += bottom
    
    return box
         

def test_draw_box():
    print(draw_box(1))
    print(draw_box(2))
    print(draw_box(3))
    print(draw_box(4))
    print(draw_box(5))
    print(draw_box(10))


#
# Problem 2.2.1
#

def roll():
    '''
    Roll two six-sided dice and return their result.
    Arguments: none
    Return value: the result (an integer between 2 and 12).
    '''

    roll_total = random.randint(2,12)
    return roll_total


#
# Problem 2.2.2
#

def craps(verbose):
    '''
    Play one round of craps.

    Arguments: 
      verbose: print out the progress of the game while playing

    Return value: 
      True if the player wins, else False
    '''
    
    win   = [7, 11]
    lose  = [2, 3, 12]
    point = [4, 5, 6, 8, 9, 10]
    if verbose == True:
        num = roll()
        
        if num in win:
            print(f'You rolled {num}. You win!')
            return True
        
        elif num in lose:
            print(f'You rolled {num}. You lose!')
            return False  
        
        elif num in point:
            print(f'Your point is: {num}.')
            while True:
                new_roll = roll()
                print(f'You rolled {new_roll}.') 
                if new_roll == num:
                    print('You hit your point! You win!')
                    return True
                elif new_roll == 7:
                    print('You missed your point! You lose!')
                    return False
            
    if verbose == False:
        num = roll()
        if num in win:
            return True
        
        elif num in lose:
            return False 
        
        elif num in point:
            while True:
                new_roll = roll()
                if new_roll == num:
                    return True
                elif new_roll == 7:
                    return False
                
                
#
# Problem 2.2.3
#

def craps_edge(n):
    '''
    Estimate and return the house edge for craps.
    See https://wizardofodds.com/games/craps/appendix/1/ for an
    analytical derivation.  The result is 1 41/99 % or 1.4141... %.

    Argument: n: the number of rounds played (>= 0)
    Return value: the house edge in percent
    '''

    assert n >= 0
    wins  = 0
    for i in range(n):
        craps(False)
        if craps(False) == True:
            wins += 1
            
    pwin  = (wins / n)
    plose = ((n - wins) / n)
    edge = -((pwin) - (plose)) * 100
    
    return edge
    
    
#
# Problem 2.3.1
#
def remove_indices(lst, indices):
    lst2 = lst[:]
    for i in indices:
        lst2[i] = 'remove'
      
    while 'remove' in lst2:
            lst2.remove('remove')
    
    return lst2
    

def remove_indices(lst, indices):
    '''
    Return a copy of a list with the elements at the given indices removed.
    Valid negative indices (between -1 and -(length of list)) can be used.
    Out-of-bound indices are ignored.

    Argument:
      lst -- the input list
      indices -- a list of integers representing locations in the list to remove

    Return value:
      The new list.  The old list is not altered in any way.
    '''
    lst2 = lst[:]
    for i in indices:
        if i < len(lst2) and i >= -len(lst2):
            lst2[i] = 'remove'
      
    while 'remove' in lst2:
            lst2.remove('remove')
    
    return lst2

#    
# Problem 2.3.2
#

def get_bet_info(bets, cwins):
    '''
    Select the next bet information for a gambling system.

    Arguments:
      bets  -- the list of bets set by the gambling system
      cwins -- the consecutive wins (0, 1) previously

    Result:
      a two tuple containing:
      -- the bet amount;
      -- the indices of the 'bets' array where the bet amount was taken from
    '''
    
    assert len(bets) > 0
    for bet in bets:
        assert bet > 0
    assert cwins in [0, 1, 2]
    if cwins == 2:
        if len(bets) >= 3:
            bet_total = (bets[0] + bets[1] + bets[-1])
            indices = [0, 1, -1]
        elif len(bets) == 2:
            bet_total = (bets[0] + bets[-1])
            indices = [0, -1]            
        elif len(bets) == 1:
            bet_total = (bets[0])
            indices = [0]             
    if cwins == 1:
        if len(bets) >= 2:
            bet_total = (bets[0] + bets[-1])
            indices = [0, -1] 
        elif len(bets) == 1:
            bet_total = (bets[0])
            indices = [0]            
    if cwins == 0:
        if len(bets) >= 1:
            bet_total = (bets[0])
            indices = [0]
    return (bet_total, indices)


#
# Problem 2.3.3
#

def make_one_bet(bankroll, bets, cwins, next_is_win):
    '''
    Play a gambling system for a single bet.

    Arguments:
      bankroll    -- the player's money
      bets        -- the list of bets set by the gambling system
      cwins       -- the consecutive wins previously
      next_is_win -- the next result of the game being played

    Result:
       A tuple consisting of:
       1) the updated bankroll
       2) the updated bets list
       3) the updated consecutive wins (max 2)
    '''

    assert bankroll >= 0
    assert len(bets) > 0
    for bet in bets:
        assert bet > 0
    assert cwins in [0, 1, 2]
    assert next_is_win in [True, False]
    lst = list(get_bet_info(bets, cwins))
    bet_total = lst[0]
    indices = lst[1]
    if bankroll < bet_total:
        bets = []
        cwins = 0
        return (bankroll, bets, cwins)        
    if cwins == 2:
        if next_is_win == True:
            bankroll += bet_total
            bets = remove_indices(bets, indices)
            cwins = 2
            return (bankroll, bets, cwins)
        elif next_is_win == False:
            bankroll -= bet_total
            bets.append(bet_total)
            cwins = 0
            return (bankroll, bets, cwins)
    if cwins == 1:
        if next_is_win == True:
            bankroll += bet_total
            bets = remove_indices(bets, indices)
            cwins += 1
            return (bankroll, bets, cwins)
        elif next_is_win == False:
            bankroll -= bet_total
            bets.append(bet_total) 
            cwins = 0
            return (bankroll, bets, cwins)
    if cwins == 0:
        if next_is_win == True:
            bankroll += bet_total
            bets = remove_indices(bets, indices) 
            cwins += 1
            return (bankroll, bets, cwins)
        elif next_is_win == False:
            bankroll -= bet_total
            bets.append(bet_total)
            cwins = 0
            return (bankroll, bets, cwins)
    assert bankroll >= 2 * bet_total
    print(bet_total)
    

#
# Test code supplied to students.
#

def random_bool():
    '''Return a random True/False value.'''
    return random.choice([True, False])

def one_round(bankroll, bets, verbose):
    '''
    Play a gambling system for a single round.
    Halt if either the desired amount of money is made, or if
    the player's bankroll hits zero.  Return the final bankroll.

    Arguments:
      bankroll    -- the player's money
      bets        -- the list of bets set by the gambling system
      verbose     -- if True, print out debugging information

    Return value: total profit (negative if there was a loss)
    '''

    assert bankroll >= 0
    assert len(bets) > 0
    for bet in bets:
        assert bet > 0

    orig_bankroll = bankroll
    cwins = 0

    if verbose:
        print('bankroll: {}, bets: {}, cwins: {}'.format(bankroll, bets,
            cwins))

    while True:
        # Test the gambling system on craps.
        #result = craps(False)
        # Alternatively, test it on a random uniformly-distributed boolean 
        # result (like flipping heads or tails).
        result = random_bool()
        if verbose:
            print('result: {}'.format(result))
        (bankroll, bets, cwins) = make_one_bet(bankroll, bets, cwins, result)
        if verbose:
            print('bankroll: {}, bets: {}, cwins: {}'.format(bankroll, bets,
                cwins))
        if bets == []:
            break
    profit = bankroll - orig_bankroll
    return profit

def run_gambling_system(verbose):
    '''
    Run multiple iterations of the gambling system,
    carrying on the bankroll from one iteration to the next.
    '''

    niters = 1000
    bankroll = 700
    orig_bankroll = bankroll
    for _ in range(niters):
        bets = [10, 10, 15]
        profit = one_round(bankroll, bets, verbose)
        if verbose:
            print('PROFIT: {}\n'.format(profit))
        bankroll += profit
        if verbose:
            print('BANKROLL: {}'.format(bankroll))
        if bankroll <= 0:
            break
    total_profit = bankroll - orig_bankroll
    if verbose:
        print('TOTAL PROFIT: {}'.format(total_profit))
    return total_profit

def run_gambling_system_multiple_times(n, verbose):
    '''
    Run multiple independent iterations of the gambling system,
    estimating and printing the average profit.
    '''

    total_profit = 0
    for _ in range(n):
        net_profit = run_gambling_system(verbose)
        if verbose:
            print(net_profit)
        total_profit += net_profit
    avg_profit = total_profit / n
    print('AVERAGE PROFIT: {}'.format(avg_profit))

# Example of use:
# run_gambling_system_multiple_times(10000, False)

# ---------------------------------------------------------------------- 
# Miniproject: 2048 game.
# ---------------------------------------------------------------------- 

#
# Problem 3.1
#

def make_board():
    '''
    Create a game board in its initial state.
    The board is a dictionary mapping (row, column) coordinates 
    (zero-indexed) to integers which are all powers of two (2, 4, ...).
    Exactly two locations are filled.
    Each contains either 2 or 4, with an 80% probability of it being 2.

    Arguments: none
    Return value: the board
    '''
    board_dic = {}
    board_pos = [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2),
                 (1,3), (2,0), (2,1), (2,2), (2,3), (3,0), (3,1), 
                 (3,2), (3,3)]
    random.shuffle(board_pos)
    random.random()
    if random.random() <= 0.8:
        board_dic[board_pos[0]] = 2
    else:
        board_dic[board_pos[0]] = 4 
    random.random()
    if random.random() <= 0.8:
        board_dic[board_pos[1]] = 2
    else:
        board_dic[board_pos[1]] = 4  
    return board_dic
    
        

#
# Problem 3.2
#

def get_row(board, row_n):
    '''
    Return a row of the board as a list of integers.
    Arguments:
      board -- the game board
      row_n -- the row number

    Return value: the row
    '''

    assert 0 <= row_n < 4
    row = [0, 0, 0, 0]
    keys = list(board.keys()) # list of positions
    values = list(board.values()) # list of values
    for n in range(len(board)):
        if row_n == keys[n][0]:
            row[keys[n][1]] = values[n]
    return row
    

def get_column(board, col_n):
    '''
    Return a column of the board as a list of integers.
    Arguments:
      board -- the game board
      col_n -- the column number

    Return value: the column
    '''

    assert 0 <= col_n < 4
    col = [0, 0, 0, 0]
    keys = list(board.keys()) # list of positions
    values = list(board.values()) # list of values
    for n in range(len(board)):
        if col_n == keys[n][1]:
            col[keys[n][0]] = values[n]    
    return col    
    

def put_row(board, row, row_n):
    '''
    Given a row as a list of integers, put the row values into the board.

    Arguments:
      board -- the game board
      row   -- the row (a list of integers)
      row_n -- the row number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= row_n < 4
    assert len(row) == 4
    for n in range(4):
        board.update({(row_n, n): row[n]}) # add values to specific row on board
        if board.get((row_n, n)) == 0: # if value is zero, remove from board
            del(board[(row_n, n)])
    
    
    

def put_column(board, col, col_n):
    '''
    Given a column as a list of integers, put the column values into the board.

    Arguments:
      board -- the game board
      col   -- the column (a list of integers)
      col_n -- the column number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= col_n < 4
    assert len(col) == 4
    for n in range(4):
        board.update({(n, col_n): col[n]}) # add values to specific column on \
                                           # board
        if board.get((n, col_n)) == 0: # if value is zero, remove from board
            del(board[(n, col_n)])
            

#
# Problem 3.3
#

def make_move_on_list(numbers):
    '''
    Make a move given a list of 4 numbers using the rules of the
    2048 game.

    Argument: numbers -- a list of 4 numbers
    Return value: the list after moving the numbers to the left.
    '''

    assert len(numbers) == 4
    counter = 0
    while 0 in numbers:
        numbers.remove(0) # remove all zeros from list
        counter += 1 # count of zeros removed
    numbers += ([0] * counter) # add number of zeros removed to the end
    
    if numbers[0] == numbers[1]: # if adjecent numbers are the same add them
        numbers[0] += numbers[1] 
        numbers[1] = numbers[2] # shift other numbers
        numbers[2] = numbers[3]
        numbers[3] = 0 # add zero to the end so list length is 4
        
    if numbers[1] == numbers[2]:
        numbers[1] += numbers[2]
        numbers[2] = numbers[3]
        numbers[3] = 0
    
    if numbers[2] == numbers[3]:
        numbers[2] += numbers[3]
        numbers[3] = 0
    return numbers
    
#
# Problem 3.4
#

def make_move(board, cmd):
    '''
    Make a move on a board given a movement command.
    Movement commands include:

      'w' -- move numbers upward
      's' -- move numbers downward
      'a' -- move numbers to the left
      'd' -- move numbers to the right

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''

    assert cmd in ['w', 'a', 's', 'd']
    for n in range(4):
        
        if cmd == 'w':
            columns = get_column(board, n) # columns to shift up
            movedColumns = make_move_on_list(columns) # make shift on columns
            put_column(board, movedColumns, n) # update column on board
        
        elif cmd == 'a':
            rows = get_row(board, n) # rows to shift right
            movedRows = make_move_on_list(rows) # make shift on rows
            put_row(board, movedRows, n) # update rows on board
        
        elif cmd == 's':
            columns = get_column(board, n) # columns to shift down
            reverse = columns[::-1] # reverse columns to make shift
            movedColumns = make_move_on_list(reverse) # make shift on columns
            unreversedColumns = movedColumns[::-1] # undo reverse so shift is \
                                                   # downward
            put_column(board, unreversedColumns, n) # update columns on board
       
        elif cmd == 'd':
            rows = get_row(board, n) # rows to shift left
            reverse = rows[::-1] # reverse rows to make shift
            movedRows = make_move_on_list(reverse) # make shift on rows
            unreversedRows = movedRows[::-1] # undo reverse so shift is left
            put_row(board, unreversedRows, n) # update rows on board           
            
            
            

#
# Problem 3.5
#
def game_over(board):
    '''
    Sees if the game is over by checking if there are any valid moves remaining.
    
    Arguments:
    board --- the game board
    
    Return value: True/ False.
    '''
    
    cmds = ['w', 'a', 's', 'd']
    board_copy = board.copy()
    if len(board) == 16: # no empty spaces
        for n in range(4):
            make_move(board, cmds[n])
        if board_copy == board: # move doesn't change the board
            return True
        else:
            return False
        
        
#
# Problem 3.6
#
    
def update(board, cmd):
    '''
    Make a move on a board given a movement command.  If the board
    has changed, then add a new number (2 or 4, 90% probability it's 
    a 2) on a randomly-chosen empty square on the board.  
    If there are no empty squares, the game is over, so return False.

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''
    board_pos = [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2),
                 (1,3), (2,0), (2,1), (2,2), (2,3), (3,0), (3,1), 
                 (3,2), (3,3)] 
    open_square = []        
    board_original = board.copy()
    make_move(board, cmd)
    if board_original != board:
        for pos in board_pos:
            if pos not in board:
                open_square.append(pos)
                random_square = random.choice(open_square)
                random.random()        
        if random.random() > 0.9:
            board[random_square] = 4
        else:
            board[random_square] = 2
        
                
            
### Supplied to students:

def display(board):
    '''
    Display the board on the terminal in a human-readable form.

    Arguments:
      board  -- the game board

    Return value: none
    '''

    s1 = '+------+------+------+------+'
    s2 = '| {:^4s} | {:^4s} | {:^4s} | {:^4s} |'

    print(s1)
    for row in range(4):
        c0 = str(board.get((row, 0), ''))
        c1 = str(board.get((row, 1), ''))
        c2 = str(board.get((row, 2), ''))
        c3 = str(board.get((row, 3), ''))
        print(s2.format(c0, c1, c2, c3))
        print(s1)

def play_game():
    '''
    Play a game interactively.  Stop when the board is completely full
    and no moves can be made.

    Arguments: none
    Return value: none
    '''

    b = make_board()
    display(b)
    while True:
        move = input('Enter move: ')
        if move not in ['w', 'a', 's', 'd', 'q']:
            print("Invalid move!  Only 'w', 'a', 's', 'd' or 'q' allowed.")
            print('Try again.')
            continue
        if move == 'q':  # quit
            return
        update(b, move)
        if game_over(b) == True:
            print('Game over!')
            break
        display(b)
        
def random_game():
    '''Play a random game.'''
    board = make_board()
    display(board)
    while True:
        print()
        move = random.choice('wasd')
        update(board, move)
        display(board)
        if game_over(board):
            break