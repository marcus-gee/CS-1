import random
# Ex D.1
def make_random_code():
    '''This function will return random choices of the colors presented in the 
    game.'''
    choices = ['R', 'G', 'B', 'Y', 'O', 'W']
    colors = ''
    for x in range(4):
        colors += random.choice(choices)
    return colors

# Ex D.2
def count_exact_matches(code, guess):
    ''' This function will return the number of matches where the list the 
    computer presents and the list of the guesses from the player have the 
    same letter in the same position.''' 
    total = 0
    for x in range(4):
        if code[x] == guess[x]:
            total += 1
    return total
    
# Ex D.3
def count_letter_matches(code, guess):
    '''This function will return the total number of letters that the two lists 
    have in common.''' 
    total = 0
    guess_lst = list(guess)
    for item in code:
        if item in guess_lst:
            total += 1
            guess_lst.remove(item)
    return total
    
# Ex D.4
def compare_codes(code, guess):
    '''This function will return 'b', 'w', or '-' depending on the number of 
    black, white, or blanck pegs based on the guesses by the player.
    Return value is not ordered.'''
    black_pegs = count_exact_matches(code, guess)
    white_pegs = count_letter_matches(code, guess) - black_pegs
    blank_pegs = 4 - (black_pegs + white_pegs)
    return 'b' * black_pegs + 'w' * white_pegs + '-' * blank_pegs

# Ex D.5
def run_game():
    '''This function runs the Mastermind game.'''
    print('New game.')
    match = make_random_code()
    x = 0
    while True:
        guess = input('Enter your guess: ')
        x += 1
        print('Result: {} '.format(compare_codes(match, guess)))
        if compare_codes(match, guess) == 'bbbb':
            print('Congratulations! You cracked the code in ' + 
                  '{}'.format(str(x)) + ' moves!')