from tkinter import *

root = Tk()
root.title("Calculator")
# root.config(bg="#594F4F")

# intiatiating the label on root
label = Entry(root, width=35, borderwidth=3)

# result label to display the input and result placed on grid
label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# dictionary of buttons
buttons = {}

# variable to store the previous values of label
previous = ''


def action(e):
    """
    method to perform arithmetic and logical operations with user input
    """
    global previous
    current = label.get()
    if e == 'cls':
        label.delete(0, END)
    elif e == "+":
        previous = label.get()
        label.delete(0, END)
    elif e == '=':
        previous = str(int(previous) + int(current))
        label.delete(0, END)
        label.insert(0, previous)
    else:
        label.delete(0, END)
        label.insert(0, f'{current}{e}')


def placeButtons():
    """
    method to place the buttons on the grid
    """
    # getting the buttons from dictionary and placing on the grid of root
    key_value = 9
    for i in range(1, 4):
        for j in range(0, 3):
            print(i, j)
            buttons[key_value].grid(row=i, column=j, padx=2, pady=5)
            key_value -= 1
    buttons[key_value].grid(row=i+1, column=j-2, padx=2, pady=5)
    buttons['add'].grid(row=i+1, column=j-1, columnspan=2, padx=2, pady=5)
    buttons['clear'].grid(row=i+2, column=j-1, columnspan=2, padx=2, pady=5)
    buttons['equal'].grid(row=i+2, column=j-2, padx=2, pady=5)


def createButtons():
    """
    method to create the buttons and initatilizes the callback
    """
    # creating buttons for values 0 -9
    for k in range(0, 10):
        buttons[k] = Button(
            root, text=f'{k}', padx=40, pady=20, bg="#355C7D", fg="white")

    # assigning callbacks to the buttons with respective value
    buttons[0].config(command=lambda: action(0))
    buttons[1].config(command=lambda: action(1))
    buttons[2].config(command=lambda: action(2))
    buttons[3].config(command=lambda: action(3))
    buttons[4].config(command=lambda: action(4))
    buttons[5].config(command=lambda: action(5))
    buttons[6].config(command=lambda: action(6))
    buttons[7].config(command=lambda: action(7))
    buttons[8].config(command=lambda: action(8))
    buttons[9].config(command=lambda: action(9))

    # functional buttns like add , equal, clear etc..
    buttons['add'] = Button(root, text='+', padx=82, pady=20,
                            command=lambda: action('+'),  bg="#355C7D", fg="white")
    buttons['equal'] = Button(root, text='=', padx=40,
                              pady=20, command=lambda: action('='),  bg="#355C7D", fg="white")
    buttons['clear'] = Button(root, text='clear', padx=78,
                              pady=20, command=lambda: action('cls'),  bg="#355C7D", fg="white")
    placeButtons()


if __name__ == '__main__':
    createButtons()
    root.mainloop()
