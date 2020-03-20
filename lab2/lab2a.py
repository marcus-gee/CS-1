import random


# Ex B.1
def complement (DNA):
    '''This function will return a string that is the complement of the original 
    string. So, 'A' will replace 'T', 'T' will replace 'A', 'C' will replace 
    'G', and 'G' will replace 'C'.'''
    comp = ''
    for letter in DNA:
        if letter == "A":
            comp += "T"
        if letter == "T":
            comp += "A"
        if letter == "C":
            comp += "G"
        if letter == "G":
            comp += "C"
    return comp

# Ex B.2
def list_complement (DNA):
    '''This function will return the complement list of all the base pairs.'''
    new_DNA = []
    lst_DNA = enumerate(DNA)
    for x in lst_DNA:
        if lst_DNA[x][1] == 'A':
            new_DNA += 'T'
        elif lst_DNA[x][1] == 'T':
            new_DNA += 'A'
        elif lst_DNA[x][1] == 'G':
            new_DNA += 'C'
        elif lst_DNA[x][1] == 'C':
            new_DNA += 'G'
    return new_DNA 
    
    
# Ex B.3
def product(nums):
    '''This function will find the product of an entire list of numbers.'''
    x = 1
    for element in nums:
        x *= element
    return x

# Ex B.4
def factorial(n):
    '''This funtion will return the factorial of the number in the argument.
    Multiplying from 1 up to the number in the argument.'''
    product = 1
    for n in range(1,n+1):
        product *= (n)
    return product

# Ex B.5
def dice(m,n):
    '''This function will return the possible sums of the dice roll based on m,
    the number of sides on the dice, and n, the number dice rolled'''
    sum = 0
    for x in range(n):
        sum += random.choice(list(range(1, m+1)))
    return sum
    
    
# Ex B.6
def remove_all(lst, y):
    '''This function will remove all values of the argument in a list'''
    while lst.count(y) > 0:
        lst.remove(y)
        

# Ex B.7.1
def remove_all2(lst, value):
    '''This funtion will remove all the values of the argument in a list'''
    total = lst.count(value)
    for x in range(0, total):
        lst.remove(value)
                
# Ex B.7.2
def remove_all3(lst, value):
    '''This funtion will remove all the values of the argument in a list'''
    while value in lst:
        lst.remove(value)
        

#  Ex B.8
def any_in(lst_1, lst_2):
    '''This function will return true or false depending on if an element in the
    first list is in the second list or not.'''
    for i in lst1:
        if i in lst2:
            return True
    return False
    
           
        
        
# Ex C.1.a   This code is incorrect because the "if a = 0" should be rewritten 
# as "if a == 0" because we don't know if a is 0.

# Ex C.1.b   This code is wrong because it uses a string as its argument instead
# of a variable. This can be fixed by taking away the single quotes in the 
# argument.

# Ex C.1.c   This code returns a string when its argument is a variable. It 
# should be returned as s without the single quotes.

# Ex C.1.d   This code won't work because bam is in string form. To fix it, 
# you'd put it inside brackets to have ['bam'].

# Ex C.1.e   This code doesn't work because lst2 = lst.reverse() does not create
# a new list named lst2 which is the reverse of lst, it just reverses lst. Thus, 
# the lst2.append step does nothing since there is no lst2 existing.

# Ex C.1.f  This code is invalid because can't name a list 'list' because 'list'
# turns whatever its argument is into an actual list. Thus, the step 'letter = 
# list(str) will turn str into a list. You will also want to use 
# list.extend(letters) at the end as opposed to list.append(letters).

# Ex C.2   The function prints out 30 because when the function solved for c, 
# it used the the values for a and b that preceeded it. If you want it to print 
# 30 you have to solve for c again after changing to value of a 30.

# Ex C.3   Using return gives the output back in a way in which it can be used 
# again. However, print just spits out the output, it cannot be used again.

# Ex C.4   The function n = 2 * sum_of_squares_2(2, 3) will not work because 
# when we defined sum_of_squares_2 we did not enter anything as its argument 
# so when we do it here with the argument (2,3) it will not work. Getting a 
# value interactively does not require an argument when the function is defined.  

# Ex C.5 This function will not work becasue you are using list notation to try 
# and change a string.=

# Ex C.6   This won't work because it only doubles the last element of the list
# and doesn't change list at all.