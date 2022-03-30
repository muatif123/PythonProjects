# Importing the required libraries
from tkinter import *
import calendar


# Defining the function
def showCal():
    box = Tk()
    box.title("calendar for the Year")
    box.geometry('500x600')
    find_year = int(year_field.get())
    first_label = Label(box, text = 'Calendar', bg = 'dark grey', font = ('times', 28, 'bold'))
    first_label.grid(row = 1, column = 1)
    box.config(background = 'white')
    cal_data = calendar.calendar(find_year)
    cal_year = Label(box, text = cal_data, font = 'Consolas 10 bold', justify = LEFT)
    cal_year.grid(row = 2, column = 1, padx = 20)
    box.mainloop()


if __name__ == '__main__':
    gui = Tk()
    gui.config(background = 'misty rose')
    gui.title("Calendar")
    gui.geometry('250x250')
    cal = Label(gui, text = 'Calendar', bg = 'Lavender', font = ('Helvetica', 28, 'bold', 'underline'))
    year = Label(gui, text = 'Enter Year', bg = 'Peach Puff', padx = 10, pady = 10)
    year_field = Entry(gui)
    Show = Button(gui, text = 'Close', bg = 'Peach Puff', command = exit)
    cal.grid(row = 1, column = 1)
    year.grid(row = 3, column = 1)
    year_field.grid(row = 4, column = 1)
    Show.grid(row = 5, column = 1)
    # ExitNow.grid(row, column = 1)
    gui.mainloop()