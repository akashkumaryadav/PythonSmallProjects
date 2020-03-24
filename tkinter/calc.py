from tkinter import *

root = Tk()
root.title("Calculator")

label = Entry(root, width=35, borderwidth=3)
label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = {}
previous = ''


def button_click(e):
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


def createButtons():
    for k in range(0, 10):
        buttons[k] = Button(root, text=f'{k}', padx=40, pady=20)
    buttons[0].config(command=lambda: button_click(0))
    buttons[1].config(command=lambda: button_click(1))
    buttons[2].config(command=lambda: button_click(2))
    buttons[3].config(command=lambda: button_click(3))
    buttons[4].config(command=lambda: button_click(4))
    buttons[5].config(command=lambda: button_click(5))
    buttons[6].config(command=lambda: button_click(6))
    buttons[7].config(command=lambda: button_click(7))
    buttons[8].config(command=lambda: button_click(8))
    buttons[9].config(command=lambda: button_click(9))
    key_value = 9
    for i in range(1, 4):
        for j in range(0, 3):
            print(i, j)
            buttons[key_value].grid(row=i, column=j, padx=2, pady=5)
            key_value -= 1
    buttons_add = Button(root, text='+', padx=82,
                         pady=20,  command=lambda: button_click('+'))
    buttons_equal = Button(root, text='=', padx=40,
                           pady=20, command=lambda: button_click('='))
    buttons_clear = Button(root, text='clear', padx=78,
                           pady=20, command=lambda: button_click('cls'))
    # for number 0
    buttons[key_value].grid(row=i+1, column=j-2)

    # buttons[k].
    buttons_add.grid(row=i+1, column=j-1, columnspan=2)
    buttons_clear.grid(row=i+2, column=j-1, columnspan=2)
    buttons_equal.grid(row=i+2, column=j-2)


createButtons()

root.mainloop()
