import math
# Ex A.1
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def distanceTo(self1, self2):
        distance = math.sqrt((self1.x - self2.x)**2 + (self1.y - self2.y)**2 + 
                             (self1.z - self2.z)**2)
        return distance

# Ex A.2
class Triangle:
    def __init__(self, Point1, Point2, Point3):
        self.Point1 = Point1
        self.Point2 = Point2
        self.Point3 = Point3
        
    def area(self):
        a = self.Point1.distanceTo(self.Point2)
        b = self.Point1.distanceTo(self.Point3)
        c = self.Point2.distanceTo(self.Point3)
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
# Ex A.3
class Averager:
    def __init__(self):
        self.nums = []
        self.total = 0.0
        self.n = 0
        
    def getNums(self):
        lst2 = self.nums[:]
        return lst2
    
    def append(self, x):
        self.nums.append(x)
        self.total += x
        self.n += 1
        
    def extend(self, lst):
        self.nums += lst
        self.total += sum(lst)
        self.n += len(lst)
        
    def average(self):
        if self.n == 0:
            return 0.0
        elif self.n > 0:
            average = (self.total / self.n)
            newAverage = float(average)
            return newAverage
        
    def limits(self):        
        if self.n == 0:
            return (0, 0)
        elif self.n > 0:
            min_num = min(self.nums)
            max_num = max(self.nums)
            return (min_num, max_num)
        
                
            
        
        
        

        
# Ex B.1
# In this code, you can just write return x > 0 and it will return True or False
# depending on if x is greater or less than 0.
def is_positive(x):
    '''Test if x is positive.'''
    return x > 0

# Ex B.2
# This code is unnecessarily complex. It has an additional "if" and "else 
# statements that are not needed. You can just have the return location command 
# outside the "if" statement and at the end of the "for" loop because if 
# item == x then found = True and the second "if" statement is not needed. 
# Or if item != then location will still be -1 and you won't that last 
# "else" statement.
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    for i, n in enumerate(lst):
        if n == x:
            return i
    else:
        return -1
            

            
    

# Ex B.3
# This code is unnecessarily inefficient. The "if" statements after the 
# first one should elif statements that way if one of the if conditions are met,
# the computer does not iterate through the rest of the statments.
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        category = 'negative'
    elif x == 0:
        category = 'zero'
    elif x > 0 and x < 10:
        category = 'small'
    elif x >= 10:
        category = 'large'
    return category

# Ex B.4
# You can make this code a lot more concise by eliminating the middle two 
# "elif" and the variables found and location statements because it makes the
# code a lot longer for no reason and just making them part of the last one.
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    total = 0
    for item in lst:
        total += item
    return total