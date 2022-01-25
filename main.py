from tkinter import *
from tkinter import messagebox

# creating a window object from the Tk()-class
master = Tk()
master.title("Tic Tac Toe")

# The game starts with "X"
clicked = True
counter = 0


# Function to draw "X" or "O" into the boxes, switching the symbol by checking the value of clicked and increasing
# the game counter
def button_clicked(button):
    global clicked, counter
    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        counter += 1
        check_if_won()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        counter += 1
        check_if_won()
    else:
        messagebox.showerror("Tic Tac Toe", "Invalid box, please pick another!")


# disables all the buttons to prevent another game move
def disable_buttons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)


def check_if_won():

    global winner
    winner = False

    # check if "X" won
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg="red")
        button2.config(bg="red")
        button3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, X won!")
        disable_buttons()
    elif button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X":
        button3.config(bg="red")
        button4.config(bg="red")
        button5.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, X won!")
        disable_buttons()
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.config(bg="red")
        button8.config(bg="red")
        button9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, X won!")
        disable_buttons()
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.config(bg="red")
        button4.config(bg="red")
        button7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, X won!")
        disable_buttons()
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.config(bg="red")
        button5.config(bg="red")
        button8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, X won!")
        disable_buttons()
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.config(bg="red")
        button6.config(bg="red")
        button9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, X won!")
        disable_buttons()
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.config(bg="red")
        button5.config(bg="red")
        button9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, X won!")
        disable_buttons()
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.config(bg="red")
        button5.config(bg="red")
        button7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, X won!")
        disable_buttons()

    # check if "O" won
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg="red")
        button2.config(bg="red")
        button3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, O won!")
        disable_buttons()
    elif button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O":
        button3.config(bg="red")
        button4.config(bg="red")
        button5.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, O won!")
        disable_buttons()
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg="red")
        button8.config(bg="red")
        button9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, O won!")
        disable_buttons()
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.config(bg="red")
        button4.config(bg="red")
        button7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, O won!")
        disable_buttons()
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.config(bg="red")
        button5.config(bg="red")
        button8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, you won!")
        disable_buttons()
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.config(bg="red")
        button6.config(bg="red")
        button9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, O won!")
        disable_buttons()
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg="red")
        button5.config(bg="red")
        button9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, O won!")
        disable_buttons()
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.config(bg="red")
        button5.config(bg="red")
        button7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "GG, O won!")
        disable_buttons()

    # check if tie
    if counter == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie, no one wins!")
        disable_buttons()


# function to reset the game by choosing it in options menu
def reset_game():

    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global clicked, counter
    clicked = True
    counter = 0

    # Creating the buttons for the game
    button1 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white",
                     command=lambda: button_clicked(button1))
    button2 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white",
                     command=lambda: button_clicked(button2))
    button3 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white",
                     command=lambda: button_clicked(button3))

    button4 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white",
                     command=lambda: button_clicked(button4))
    button5 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white",
                     command=lambda: button_clicked(button5))
    button6 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white",
                     command=lambda: button_clicked(button6))

    button7 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white",
                     command=lambda: button_clicked(button7))
    button8 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white",
                     command=lambda: button_clicked(button8))
    button9 = Button(master, text=" ", font=("Helvetica", 18), height=4, width=7, bg="white",
                     command=lambda: button_clicked(button9))

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


# creating a main menu
game_menu = Menu(master)
master.config(menu=game_menu)

# create the options in  menu
options_menu = Menu(game_menu, tearoff=False)
game_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset_game)

reset_game()
mainloop()
