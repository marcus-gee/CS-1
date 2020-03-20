# Ex A.1
'''This function takes a list and creates a new list that is the reverse of the 
original list without changing the original.'''
def list_reverse(lst):
    lst_new = lst[::-1]
    return lst_new

# Ex A.2
'''This function takes a list and creates a new list that is the reverse of the 
original list without changing the original.''' 
def list_reverse2(lst):
    lst2 = lst[:]
    lst2.reverse()
    return lst2

# Ex A.3
'''This function takes an input of a file and returns the number of lines, 
words, and characters in the file.'''
def file_info(filename):
    f = open(filename, 'r')
    total_lines = 0
    total_words = 0
    total_characters = 0
    while True:
        line = f.readline()
        if line == '':
            break
        total_lines += 1
        word = line.split()
        total_words += len(word)
        total_characters += len(line)
    f.close()
    return (total_lines, total_words, total_characters)

# Ex A.4
'''This function takes a file as its input and returns the number of lines, 
words, and characters in the file as a dictionary.'''
def file_info2(file_x):
    total_lines, total_words, total_characters = file_info(file_x)
    totals = {'lines': total_lines, 'words': total_words, 'characters': total_characters}
    return totals

# Ex A.5
'''This function takes a file as its input and returns the length of the 
longest line and the longest line itself.'''
def longest_line(filename):
    f = open(filename, 'r')
    line_length = 0
    long_line = ''
    for line in f:
        length = len(line)
        if length > line_length:
            line_length = length
            long_line = line
    f.close()
    return(line_length, long_line)

# Ex A.6
'''This function takes a string as its argument and splits each word of the 
string into its own string and sorts them alphabetically.'''
def sort_words(s):
    lst = s.split()
    lst.sort()
    return lst

# Ex A.7
#   11011010 ---> 1*2^7 + 1*2^6 + 0*2^5 + 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 
#            ---> 218
# Largest eight-digit number in binary ---> 255

# Ex A.8
'''This function takes an input of binary numbers and converts them to a Python 
integer.'''
def binaryToDecimal(lst):
    decimal = 0
    for i, val in enumerate(lst):
        if val == 1:
            decimal += int(2**(len(lst) - i - 1))
    return decimal

# Ex B.2.1
# This function has bad spacing between the + operators. Also the function name 
# 'sc' is defined poorly and inside the argument there should be a space after 
# each comma.
def sum_of_cubes(a, b, c):
    return a*a*a + b*b*b + c*c*c

# Ex B.2.2
# This example chose poor names for the argument as well as the function. 
# Additionally, there should be a space after '#' in the comment and the grammar
# of the actual comment is not good. The last line should be brokeb up because 
# it is too long.
def sumofcubes(a, b, c, d):
    # reutrn sumof cubes of args a b c & d
    return (a * a * a) + (b * b * b) + (c * c * c) + (d * d * d)

# Ex B.2.3
# In this example there is inconsistent indentation and there should be a blanck
# line between the two functions. 
def sum_of_squares(x, y):
    return (x * x) + (y * y)

def sum_of_three_cubes(x, y, z):
    return (x * x * x) + (y * y * y) + (z * z * z)
