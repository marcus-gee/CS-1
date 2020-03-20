from tkinter import *
import random

def random_color():
    values = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", 
    "7", "8", "9"]
    color = '#'
    for i in range(6):
        output= random.choice(values)
        color += output
    return color
def random_size(a, b):
    assert a > 0
    assert b > 0
    assert a % 2 == 0
    assert b % 2 == 0
    assert a < b
    c = random.randint(a, b)
    return c
def random_position(max_x, max_y):
    assert max_x >= 0 
    assert max_y >= 0
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x,y)
def draw_square(canvas, color, width, center):
    x1 = center[0] - width/2
    x2 = center[0] + width/2
    y1 = center[1] - width/2
    y2 = center[1] + width/2
    square = canvas.create_rectangle(x1, y1, x2, y2, fill=color, 
                                     outline=color)
    return square

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack() 
    for x in range(50):
        pos = random_position(800, 800)
        s = random_size(20, 150)
        draw_square(canvas, random_color(), s, pos)
    root.mainloop()
    