from tkinter import *


def draw_fields(canvas, distance):
    # vertical lines at an interval of distance" pixel
    for x in range(distance, canvas_width, distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "distance" pixel
    for y in range(distance, canvas_height, distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")


master = Tk()            # creating a window object from the Tk()-class
canvas_width = 540       # defining the width of the game area
canvas_height = 540      # defining the height of the game area
field = Canvas(master, width=canvas_width, height=canvas_height)
field.pack()

draw_fields(field, 180)  # drawing the lines for the game area

cols = 3    # defining the number of vertical fields
rows = 3    # defining the number of horizontal fields
cell_width = canvas_width / cols    # defining the size of each field
cell_height = canvas_height / rows  # defining the size of each field

mainloop()
