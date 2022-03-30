# Importing the required libraries
import math
import tkinter


# Initializing the tkinter window
root = tkinter.Tk()
root.title('Standard Calculator')
root.resizable(0, 0)

# Creating an entry field
e = tkinter.Entry(root, width = 35, bg = '#f0ffff', fg = 'black', borderwidth = 5, justify = 'right', font = 'Calibri 15')
e.grid(row = 0, column = 0, columnspan = 3, padx = 12, pady = 12)


# Defining the function for clicking
def buttonClick(num):
    temp = e.get()              # Temporary storing the current input to show on the screen
    e.delete(0, tkinter.END)
    e.insert(0, temp + num)


def buttonClear():
    e.delete(0, tkinter.END)

# Defining the function for storing the first input and printing the operator
def buttonGet(oper):
    global num1, math
    num1 = e.get()
    math = oper
    e.insert(tkinter.END, math)
    try:
        num1 = float(num1)
    except ValueError:
        buttonClear()

# Defining the funtion for printing the sum
def buttonEqual():
    inp = e.get()
    num2 = float(inp[inp.index(math) + 1:])     # Function to get the second number input
    e.delete(0, tkinter.END)
    if math == '+':
        e.insert(0, str(num1 + num2))
    elif math == '-':
        e.insert(0, str(num1 - num2))
    elif math == '*':
        e.insert(0, str(num1 * num2))
    elif math == '/':
        try:
            e.insert(0, str(num1 + num2))
        except ZeroDivisionError:
            e.insert(0, 'Undefined')

# Defining the buttons
b1 = tkinter.Button(
    root, text = '1', padx = 40, pady = 10, command = lambda: buttonClick('1'), font = 'Calibri 12'
)
b2 = tkinter.Button(
    root, text = '2', padx = 40, pady = 10, command = lambda: buttonClick('2'), font = 'Calibri 12'
)
b3 = tkinter.Button(
    root, text = '3', padx = 40, pady = 10, command = lambda: buttonClick('3'), font = 'Calibri 12'
)
b4 = tkinter.Button(
    root, text = '4', padx = 40, pady = 10, command = lambda: buttonClick('4'), font = 'Calibri 12'
)
b5 = tkinter.Button(
    root, text = '5', padx = 40, pady = 10, command = lambda: buttonClick('5'), font = 'Calibri 12'
)
b6 = tkinter.Button(
    root, text = '6', padx = 40, pady = 10, command = lambda: buttonClick('6'), font = 'Calibri 12'
)
b7 = tkinter.Button(
    root, text = '7', padx = 40, pady = 10, command = lambda: buttonClick('7'), font = 'Calibri 12'
)
b8 = tkinter.Button(
    root, text = '8', padx = 40, pady = 10, command = lambda: buttonClick('8'), font = 'Calibri 12'
)
b9 = tkinter.Button(
    root, text = '9', padx = 40, pady = 10, command = lambda: buttonClick('9'), font = 'Calibri 12'
)
b0 = tkinter.Button(
    root, text = '0', padx = 40, pady = 10, command = lambda: buttonClick('0'), font = 'Calibri 12'
)
bdot = tkinter.Button(
    root, text = '.', padx = 41, pady = 10, command = lambda: buttonClick('.'), font = 'Calibri 12'
)
badd = tkinter.Button(
    root, text = '+', padx = 29, pady = 10, command = lambda: buttonGet('+'), font = 'Calibri 12'
)
bsub = tkinter.Button(
    root, text = '-', padx = 30, pady = 10, command = lambda: buttonGet('-'), font = 'Calibri 12'
)
bmul = tkinter.Button(
    root, text = '*', padx = 30, pady = 10, command = lambda: buttonGet('*'), font = 'Calibri 12'
)
bdiv = tkinter.Button(
    root, text = '/', padx = 30.5, pady = 10, command = lambda: buttonGet('/'), font = 'Calibri 12'
)
bclear = tkinter.Button(
    root, text = 'AC', padx = 20, pady = 10, command = buttonClear, font = 'Calibri 12'
)
bequal = tkinter.Button(
    root, text = '=', padx = 39, pady = 10, command = buttonEqual, font = 'Calibri 12'
)

# Putting the buttons on the screen
b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)
badd.grid(row = 3, column = 3)

b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
bmul.grid(row = 2, column = 3)

b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)
bdiv.grid(row = 1, column = 3)

b0.grid(row = 4, column = 0)
bdot.grid(row = 4, column = 1)
bequal.grid(row = 4, column = 2)
bsub.grid(row = 4, column = 3)

bclear.grid(row = 0, column = 3)

# Looping the window
root.mainloop()