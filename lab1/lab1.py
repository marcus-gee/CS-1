# Ex C.1.1:  9 - 3       --> 6
# Ex C.1.2:  8 * 2.5     --> 20.0
# Ex C.1.3:  9 / 2       --> 4.5
# Ex C.1.4:  9 / -2      --> -4.5
# Ex C.1.5:  9 % 2       --> 1
# Ex C.1.6:  9 % -2      --> -1
# Ex C.1.7:  -9 % 2      --> 1
# Ex C.1.8:  9 / -2.0    --> -4.5
# Ex C.1.9:  4 + 3 * 5   --> 19
# Ex C.1.10: (4 + 3) * 5 --> 35

# Ex C.2.1:  x = 100    --> 100
# Ex C.2.2:  x = x + 10 --> 110
# Ex C.2.3:  x += 20    --> 130
# Ex C.2.4:  x = x - 40 --> 90
# Ex C.2.5:  x -= 50    --> 40
# Ex C.2.6:  x *= 3     --> 120
# Ex C.2.7:  x /= 5     --> 24.0
# Ex C.2.8:  x %= 3     --> 0.0

# Ex C.3:  x += x - x
#          x = x + x - x 
#          x = x           --> 3

# Ex C.4.1:  1j + 2.4j       --> 3.4j
# Ex C.4.2:  4j * 4j         --> (-16+0j)
# Ex C.4.3:  (1+2j) / (3+4j) --> (0.44+0.08j)
# Ex C.4.1:  (1+2j) * (1+2j) --> (-3+4j)
# Ex C.4.2:  1+2j * 1+2j     --> (1+4j)
# Ex C.4: The last two expressions gave different results because one of had  
# parentheses and thus changing the order of operations. This tells us that 
# python handles the order of operations with expressions involving complex 
# numbers the same as expressions not involving complex numbers.

# Ex C.5.1:  cmath.sin(-1.0+2.0j)        
#                        --> (-3.165778513216168+1.9596010414216063j)
# Ex C.5.2:  cmath.log(-1.0+3.4j)
#                        --> (1.2652585805200263+1.856847768512215j)
# Ex C.5.3:  cmath.exp(-cmath.pi * 1.0j) --> (-1-1.2246467991473532e-16j)
# EX C.5:  It is better to enter "import math/ cmath" because with 
# "from math/ cmath import *" there is a possibility that you will have a name 
# clash.

# Ex C.6.1:  "foo" + 'bar' --> 'foobar'
# Ex C.6.2:  "foo" 'bar'   --> 'foobar'
# Ex C.6.3:  a = 'foo'
#            b = "bar"
#            a + b         --> 'foobar'
# Ex C.6.4:  a = 'foo'
#            b = "bar"
#            a b           --> Syntax Error: invalid syntax: <string>, line 1, 
#                                                                         pos 3


# Ex C.7: 'A\n' + \
#         'B\n' + \
#         'C\n'
    
# Ex C.8: 80 * '-'

# Ex C.9: print('first line\nsecond line\nthird line\n')

# Ex C.10.1:
x = 3
y = 12.5
'The rabbit is {}.'.format(x)

# Ex C.10.2:
'The rabbit is {} years old.'.format(x)

# Ex C.10.3:
'{} is average.'.format(y)

# Ex C.10.4:
'{} * {}'.format(y,x)

# Ex C.10.5:
'{} * {} is {}.'.format(y,x,x*y)

# Ex C.11:
num = input("Enter a number: ")
print(num)

# Ex C.12:
def quadratic(a, b, c, x):
    return a * (x ** 2) + (b * x) + c


#Ex C.13:
'''The function finds the number of C and G bases in the DNA 
sequence and divides it by the the total number of bases in the DNA sequence'''
def GC_content(DNA):
    GCcount = DNA.count('C') + DNA.count('G')
    total = len(DNA)
    return GCcount / total