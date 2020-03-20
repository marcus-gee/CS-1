'''
lab3c.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 
def update(dic, Lstring):
    '''This function generates the next version of the L-system string.'''
    Lstring2 = ''
    for x in Lstring:
        if x in dic:
            Lstring2 += dic[x]
        else:
            Lstring2 += x
    return Lstring2

def iterate(lsys, n):
    '''This function returns the string which results from starting with the 
    starting string for that L-system and updating n times.'''
    start_string = lsys['start']
    for i in range(n):
        start_string = update(lsys, start_string)
    return start_string
    
def lsystemToDrawingCommands(draw, s):
    '''This function returns the list of drawing commands needed to draw the 
    figure corresponding to the L-system string.'''
    lst = []
    for character in s:
        if character in draw:
            lst.append(draw[character])
    return lst

def nextLocation(x, y, angle, cmd):
    '''This function generates the next location and direction of the turtle 
    after the drawing command has been executed'''
    direction = cmd.split()
    radians = (angle * (math.pi/180))
    magnitude = int(direction[1])
    if direction[0] == 'F':
        x += math.cos(radians) * magnitude
        y += math.sin(radians) * magnitude
    elif direction[0] == 'R':
        angle -= magnitude
    elif direction[0] == 'L':
        angle += magnitude
    angle %= 360
    return (x, y, angle)

def bounds(cmds):
    '''This function computes the bounding coordinates of the resulting 
    drawing.'''
    xmin = 0
    ymin = 0
    xmax = 0
    ymax = 0
    x = 0
    y = 0
    angle = 0
    for cmd in cmds:
        (x, y, angle) = nextLocation(x, y, angle, cmd)
        if x > xmax:
            xmax = x
        elif x < xmin:
            xmin = x
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y
    float(xmin)
    float(xmax)
    float(ymin)
    float(ymax)
    return (xmin, xmax, ymin, ymax)
    
def saveDrawing(filename, bounds, cmds):
    '''This function writes the file, bounds, and list of drawing commands 
    and writes the bounds on a single line and each of the drawing commands on 
    a seperate line'''
    bstring = '{} {} {} {}'.format(bounds[0], bounds[1], bounds[2], bounds[3])
    with open(filename, 'w') as f:
        f.write(bstring + '\n')
        for cmd in cmds:
            f.write(cmd + '\n')
            
def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print('Making drawings for {}...'.format(name))
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)
