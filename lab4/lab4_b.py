import random

# Ex B.1
'''This function takes an argument of two even, positive values where the first
is smaller than the second and returns a random integer that is also even and 
in the range between the two arguments.''' 
def random_size(a, b):
    assert a >= 0
    assert b >= 0
    assert a % 2 == 0
    assert b % 2 == 0
    assert a < b
    
    c = random.randrange(a, b, 2)
    assert c % 2 == 0
    
    if c % 2 == 0:
        return c

# Ex B.2
'''This function takes as its argument two positive integers and returns a
random (x,y) pair with 0 < x < max_x and 0 < y < y_max.'''
def random_position(max_x, max_y):
    assert max_x >= 0
    assert max_y >= 0
    
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y)

# Ex B.3
'''This function generates a random color recognized by the tkinter graphics
package'''
def random_color():
    import random
    values = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", 
              "7", "8", "9"]
    color = '#'
    for i in range(6):
        output = random.choice(values)
        color += output
    return color
    
# Ex B.4
'''This function takes a dictionary as its argument and returns a count of the 
number of the number of distinct values it contains.'''
def count_values(dic):
    lst = dic.values()
    lst2 = []
    total = 0
    for x in lst:
        if x not in lst2:
            lst2.append(x)
            total += lst2.count(x)
    return total
    
# Ex B.5
'''This function takes a dictionary and an arbitrary value that could be in 
the dictionary as its argument. It removes the key/value pair from the 
dictionary which has that value.'''
def remove_value(dic, x):
    keys = list(dic.keys())
    lst1 = []
    values = list(dic.values())
    if x not in values:
        return None
    for item in keys:
        if dic[item] == x:
            lst1.append(item)
    for item in lst1:
        del dic[item]
    return dic

# Ex B.6
'''This function takes a dictionary as its argument and splits the dicitonary 
into a tuple of two dictionaries, one whose keys start with the letters a-m and 
the other whose keys start with n-z.'''
def split_dict(dic):        
    keys = list(dic.keys())
    vals = list(dic.values())
    dic_am = {}
    dic_nz = {}
    for k in keys:
        if k[0].upper() <= 'M':
            dic_am[k] = dic[k]
        elif k[0].upper() >= 'M':
            dic_nz[k] = dic[k]
    return (dic_am, dic_nz)

#Ex B.7
'''This function takes a dictionary as its argument and returns the number of 
values that appear two or more times.'''
def count_duplicates(dic):
    lst = list(dic.values())
    duplicates = []
    total = 0
    for item in lst:
        if lst.count(item) > 1:
            if item not in duplicates:
                duplicates.append(item)
                total += duplicates.count(item)
    return total