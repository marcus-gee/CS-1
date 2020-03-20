from tkinter import *
import random

# Graphics commands.
def random_color(): 
    '''The function generates a random color'''
    values = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", 
    "7", "8", "9"]
    color = '#'
    for i in range(6):
        output = random.choice(values)
        color += output
    return color

def random_diameter():
    '''Generates a random integer to represent the diameter'''
    diameter = random.randint(10, 50)
    return diameter

def change_color():
    '''Changes the original color''' 
    global color
    color = random_color()
    
def draw_circle(canvas, color, x, y):
    '''Draws a circle of random color and size''' 
    global handlst
    d = random_diameter()
    circle = canvas.create_oval(x + (d/2), y + (d/2), x - (d/2), y - (d/2), 
                                outline=color, fill=color)
    handlst.append(circle)


# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    key = event.keysym
    global canvas
    global color 
    global handlst
    if key == 'q':
        quit()
    elif key == 'c':
        change_color()
    elif key == 'x':
        for i in handlst:
            canvas.delete(i)

def button_handler(event):
    '''Handle left mouse button click events.'''
    root.bind('<button_1>', draw_circle(canvas, color, event.x, event.y))
        


if __name__ == '__main__':
    global color
    global handlst
    handlst = []
    global canvas  
    color = random_color()
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

