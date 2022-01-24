
from tkinter import *
from tkinter import messagebox

# creating a window object from the Tk()-class
master = Tk()
master.title("Tic Tac Toe")

# The game starts with "X"
clicked = True
counter = 0

# Function to draw "X" or "O" into the boxes,
# switching the symbol by checking the value
# of clicked and increasing the game counter
def button_clicked(button):

    global clicked, counter
    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        counter += 1
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        counter += 1
    else:
        messagebox.showerror("Tic Tac Toe", "Invalid box, please pick another!")

# Creating the buttons for the game
button1 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white", command= lambda: button_clicked(button1))
button2 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white", command= lambda: button_clicked(button2))
button3 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white", command= lambda: button_clicked(button3))

button4 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white", command= lambda: button_clicked(button4))
button5 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white", command= lambda: button_clicked(button5))
button6 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white", command= lambda: button_clicked(button6))

button7 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white", command= lambda: button_clicked(button7))
button8 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white", command= lambda: button_clicked(button8))
button9 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white", command= lambda: button_clicked(button9))

# Drawing the buttons into a grid and positioning them by the value of rows and cols
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

mainloop()
