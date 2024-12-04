# File Name: userinterfaces.py
# Date: 2023 - 11 - 22
# Author: Adam Sabatini
# Brief Description: allow the user to enter a width and length of a rectangle.
# Perform perimeter and area calculations using the users input.

# libraries
from tkinter import *
from tkinter.tix import *
import sys

# functions
def calculate_rectangle(_event = None):
    """function that calculates the area and perimeter from the users input"""
    # define constants
    NUMBER_OF_SIDES = 2 
    # check to see if user input is a float value
    try:
        # save user inputs to a variable in the fuction
        valid_width = float(entry_width.get())
        valid_length = float(entry_length.get())
        
        # check to see if both inputs are a positive number
        if valid_width > 0 and valid_length > 0:
            # calculate the perimeter
            calculated_perimeter = NUMBER_OF_SIDES*(valid_length + valid_width)
            # calculate the area
            calculated_area = valid_width * valid_length
            # output the calculated area and perimeter values to their respective labels
            label_perimeter_output.configure(text = "{:.2f} m".format(calculated_perimeter))
            label_area_output.configure(text = "{:.2f} m²".format(calculated_area))
        else:
            # display error message if input isnt > 0
            label_area_output.configure(text = "ERROR: All inputs must be positive")
            label_perimeter_output.configure(text = "ERROR: All inputs must be positive")
    # display error message if input isn't numeric
    except ValueError:
        label_area_output.configure(text= "ERROR: All inputs must be numeric")
        label_perimeter_output.configure(text= "ERROR: All inputs must be numeric")

def close_window(_event = None):
    """function to exit"""
    sys.exit()

def clear_fields(_event = None):
    """function to clear all fields in the window"""
    entry_length.delete(0,END)
    entry_width.delete(0,END)
    label_area_output.configure(text = "")
    label_perimeter_output.configure(text = "")
    # put focus back on the top entry box
    entry_width.focus()

# create a tk instance
window = Tk()

# window properties
window.geometry("325x175")
window.minsize(width = 325, height = 175)
window.title("Rectangle Calculator")

# create a ballon object for tooltips
tooltip = Balloon(window)

# Row 0 widgets
# create label for the width widget
label_width = Label(text = "Width: ")
label_width.grid(row = 0, column = 0, padx=5,pady=5, sticky=E)
# create entry for the width widget
entry_width = Entry(width = 35)
entry_width.grid(row = 0, column = 1, columnspan=2, padx=5,pady=5, sticky=W)
# create tooltip for the width entry widget
tooltip.bind_widget(entry_width, msg = "Enter the width of your rectangle")
# add focus to top widget when opening the window
entry_width.focus()

# Row 1 widgets
# create label for the length widget
label_length = Label(text = "Length: ")
label_length.grid(row = 1, column = 0, padx=5,pady=5, sticky=E)
# create entry for the length widget
entry_length = Entry(width = 35)
entry_length.grid(row = 1, column = 1, columnspan=2, padx=5,pady=5, sticky=W)
# create tooltip for the length entry widget
tooltip.bind_widget(entry_length, msg = "Enter the length of your rectangle")

# Row 2 widgets
# create label for the area widget
label_area = Label(text = "Area: ")
label_area.grid(row = 2, column = 0, padx=5,pady=5, sticky=E)
# create label for the output area widget
label_area_output = Label(width = 30, bd = 2, relief = SUNKEN)
label_area_output.grid(row = 2, column = 1,columnspan=2, padx=5,pady=5)
# create tooltip for the label_area_output label widget
tooltip.bind_widget(label_area_output, msg = "Displays the calculated area of the rectangle")

# Row 3 widgets
# create label for the perimeter widget
label_perimeter = Label(text = "Perimeter: ")
label_perimeter.grid(row = 3, column = 0, padx=5,pady=5, sticky=E)
# create label for the output perimeter widget
label_perimeter_output = Label(width = 30, bd = 2, relief = SUNKEN)
label_perimeter_output.grid(row = 3, column = 1,columnspan=2,padx=5,pady=5)
# create tooltip for the label_perimeter_output label widget
tooltip.bind_widget(label_perimeter_output, msg = "Displays the calculated perimeter of the rectangle")

# Row 4 widgets
# create button for clear fields widget
button_clear_fields = Button(text="Clear Fields", width=10, command=clear_fields)
button_clear_fields.grid(row=4,column=0,padx=5,pady=5)
# create tooltip for button_clear_fields widget
tooltip.bind_widget(button_clear_fields, msg = "Click to clear all fields")
# create button for the calculate widget
button_calculate = Button(text="Calculate", width=10, command= calculate_rectangle)
button_calculate.grid(row=4,column=1,padx=5,pady=5,sticky=E)
# create tooltip for button_calculate widget
tooltip.bind_widget(button_calculate, msg = "Click to calculate the perimeter and area of your rectangle")
# create button for the quit widget
button_quit = Button(text="Quit", width=10, command= close_window)
button_quit.grid(row=4,column=2,padx=5,pady=5,sticky=E)
# create tooltip for the button_quit widget
tooltip.bind_widget(button_quit, msg = "Click to exit the application")

# add hotkey support 
window.bind("<Alt-z>", clear_fields)
window.bind("<Alt-x>", calculate_rectangle)
window.bind("<Return>", calculate_rectangle)
window.bind("<Alt-c>", close_window)

# Run the main loop
window.mainloop()