from tkinter import *
import random
import math

global canvas
global color 
global handlst
global N

handlst = []        

# Graphics commands.
def random_color():
    global color
    '''This function generates a random color'''
    values = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", 
    "7", "8", "9"]
    color = '#'
    for i in range(6):
        output = random.choice(values)
        color += output
    return color

def random_diameter():
    '''This function generates a random integer that will represent the 
    diameter'''
    diameter = random.randint(50, 100)
    return diameter

def change_color():
    '''Changes the original color'''
    global color
    color = random_color()
    
def draw_circle(canvas, color, x, y):
    '''Draws a circle of a random color and size'''
    d = random_diameter()
    circle = canvas.create_oval(x + (d/2), y + (d/2), x - (d/2), y - (d/2), 
                                outline=color, fill=color)
    handlst.append(circle)

def draw_line(canvas, color, x1, y1, x2, y2):
    line = canvas.create_line(x1, y1, x2, y2)
    handlst.append(line)
    return handlst

def draw_star(canvas, color, x, y):
    d = random_diameter()
    angle = math.pi / 2
    new_angle = (2 * math.pi) / N
    points = []
    for values in range(N):
        x0 = d * math.cos(angle)
        y0 = d * math.sin(angle)
        point = (x - x0, y - y0)
        points.append(point)
        angle += new_angle
        
    new_point = points[0]
    skip = (N - 1) / 2
    for i in range(N + 1):
        next_point = points[int((i * skip) % N)]
        draw_line(canvas, color, new_point[0], new_point[1], next_point[0], 
                  next_point[1])
        new_point = next_point
        

# Event handlers.
    
def key_handler(event):
    '''Handle key presses.'''
    key = event.keysym
    global N
    
    if key == 'q':
        quit()
    elif key == 'c':
        change_color()
    elif key == 'p':
        N += 2
    elif key == 'm':
        if N > 5:
            N -= 2
    elif key == 'x':
        for i in handlst:
            canvas.delete(i)
    print(N)
    
def button_handler(event):
    '''Handle left mouse button click events.'''
    root.bind('<button_1>', draw_star(canvas, color, event.x, event.y))
        


if __name__ == '__main__':
    N = 5
    color   = random_color()    
    root = Tk()
    root.geometry('800x800')
    canvas  = Canvas(root, width=800, height=800)    
    canvas.pack()
    

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()