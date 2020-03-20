from tkinter import *
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
    c = Canvas(root, width=800, height=800)
    c.pack()
    draw_square(c, 'red', 100, [50,50])
    draw_square(c, 'green', 100, [750,50])
    draw_square(c, 'blue', 100, [50,750])
    draw_square(c, 'yellow', 100, [750,750])
    root.mainloop()