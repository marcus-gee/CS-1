# Ex A.1.1
def union(s1, s2):
    '''This function takes two sets and returns the unions of the two as another 
    set'''
    return s1.union(s2)


# Ex A.1.2
def intersection(s1, s2):
    '''takes two sets and computes and returns their intersection as another 
    set'''
    return s1.intersection(s2)


# Ex A.2
def mySum(*nums):
    '''This function takes an arbitrary number of arguments, all of which should
    be integers greater than zero, and returns their sum'''
    for num in nums:
        if type(num) is not int:
            raise TypeError('Argument must be an integer!')
        if num < 0:
            raise ValueError('Argument must be greater than 0!')
    return sum(nums)


# Ex A.3
def myNewSum(*nums):
    '''This function takes a single list of positive integers as its only 
    argument and which will return the sum of the list'''
    if len(nums) == 1 and type(nums[0]) == list:
        for num in nums[0]:
            if num < 1:
                raise ValueError('Supplied integers must be at least 1!')
        return sum(nums[0])
    else:
        for num in nums:
            if type(num) is not int:
                raise TypeError('Input needs to be integers or a single list of'
                                ' integers')
            if num < 1:
                raise ValueError('Supplied integers must be at least 1!')
        return sum(nums)
            
       
# Ex A.4
def myOpReduce(lst, **kw): 
    '''This function takes one required argument (a list of integers) and 
    one keyword argument called op, whose value should be a string. If op is 
    '+', then the function will sum all the integers; if it's '*', it will 
    multiply them all together, and if it's 'max', it will return the maximum 
    of the numbers'''
    if len(kw) > 1:
        raise ValueError('Too many keyword arguments')
    elif len(kw) == 0:
        raise ValueError('No keyword argument')    
    else:
        for args in kw:
            if args != 'op':
                raise ValueError('Invalid keyword argument')
            else:
                if kw['op'] == '+':
                    return sum(lst)
                elif kw['op'] == '*':
                    product = 1
                    for i in lst:
                        product *= i
                    return product
                elif kw['op'] == 'max':
                    if len(lst) > 1:
                        return max(lst)
                    else:
                        return 0
                elif type(kw['op']) is not str:
                    raise TypeError('Value for keyword argument must be a'
                                    ' string')
                else:
                    raise ValueError('Invalid keyword argument')
    
    
# Ex B.1
# The problem with this code is that if the error happens, you dont want it to 
# quit.
import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and 
    key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:   
        if key1 not in dict:
            return dict[key2]
        if key2 not in dict:
            return dict[key1]
        if key1 not in dict and key2 not in dict:
            return 0


# Ex B.2
# The problem with this function is that it does not let the user know which 
# key is not in the dictionary.
import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:   # raised if a key isn't in a dictionary
        if key1 not in dict:
            print >> sys.stderr, 'key1 not found'
            return dict[key2]
        if key2 not in dict:
            print >> sys.stderr, 'key2 not found'
            return dict[key1] 
        if key1 not in dict and key2 not in dict:
            print >> sys.stderr, 'key1 and key2 not found'
            return 0

        
# Ex B.3
# The problem with this code is that you don't need to raise the KeyError after 
# you have already excepted it.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:   # raised if a key isn't in a dictionary
        if key1 not in dict:
            print >> sys.stderr, 'key1 not found'
            return dict[key2]
        if key2 not in dict:
            print >> sys.stderr, 'key2 not found'
            return dict[key1] 
        if key1 not in dict and key2 not in dict:
            print >> sys.stderr, 'key1 and key2 not found'
            return 0