import random

def complement(DNA):
    complement = ''
    for letter in DNA:
        if letter == 'A':
            complement += 'T'
        elif letter == 'T':
            complement += 'A'
        elif letter == 'C':
            complement += 'G'
        elif letter == 'G':
            complement += 'C'
    return complement

def list_complement(DNA):
    for i in range(len(DNA)):
        if DNA[i] == 'A':
            DNA[i] = 'T'
        elif DNA[i] == 'T':
            DNA[i] = 'A'
        elif DNA[i] == 'C':
            DNA[i] = 'G'
        elif DNA[i] == 'G':
            DNA[i] = 'C'        
         
def product(nums):
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
    return product

def factorial(num):
    product = 1
    for num in range(1, num+1):
        product *= (num)
    return product

def dice(m, n):
    sum = 0
    for x in range(n):
        sum += random.choice(list(range(1, m+1)))
    return sum

def remove_all(lst, num):
    while lst.count(num) > 0:
        lst.remove(num)
        
def remove_lst2(lst, num):
    total = lst.count(num)
    for x in range(0, total):
        lst.remove(num)    
        
def remove_all3(lst, value):
    while value in lst:
        lst.remove(value)

def any_in(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return True
        else:
            return False
        
        
        
        
        
        
def make_random_code():
    colors = ['R', 'G', 'B', 'Y', 'O','W']
    code   = ''
    for i in range(4):
        code += random.choice(colors)
    return code

def count_exact_matches(code, guess):
    correct = 0
    for i in range(len(code)):
        if code[i] == guess[i]:
            correct += 1
        else:
            correct += 0
    return correct

def count_letter_matches(code, guess):
    counter = 0
    guess_lst = list(guess)
    code_lst = list(code)
    for i in range(len(code_lst)):
        if code_lst[i] in guess_lst:
            counter += 1
            guess_lst.remove(code_lst[i])
        else:
            counter += 0
    return counter

def compare_codes(code, guess):
    response = ''
    black_pegs = count_exact_matches(code, guess)
    white_pegs = (count_letter_matches(code, guess) - black_pegs)
    blank_pegs = 4 - (black_pegs + white_pegs)
    response = (black_pegs * 'b') + (white_pegs * 'w') + (blank_pegs * '-')
    return response

def run_game():
    print('New Game.')
    guesses = 0
    code = make_random_code()
    while True:
        guess = input('Enter your guess: ')
        guesses += 0
        print('Result: {} '.format(compare_codes(match, guess)))
        if compare_codes(match, guess) == 'bbbb':
            print('Congratulations! You cracked the code in ' + 
                  '{}'.format(str(x)) + ' moves!')