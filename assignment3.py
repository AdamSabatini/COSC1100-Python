# File Name: assignment3.py
# Date: 2023 - 12 - 1
# Author: Adam Sabatini
# Brief Description: allow the user to select a conversion to km or miles.
# Enter a measurement in km or miles. Convert the inputted measurement into the opposite unit.

# libraries
from tkinter import *
from tkinter.tix import *

# modules
import sys

# functions
def calculate_distance(_event = None):
    """function that calculates the conversion to km or mi from the users input"""
    # try block. check to see if user input is a float value
    try:
        # save user inputs to a variable in the fuction
        valid_distance = float(entry_input.get())

        # check to see if the input is a posititve number and if the kilometer radio button is selected
        if valid_distance > 0 and radiobutton_choice.get()== "kilometer":
            # calculate the distance converting from miles to kilometers
            calculated_kilometers = valid_distance*1.609
            # output the calculated distance to the label_result_output
            label_result_output.configure(text= str(valid_distance)+"mi converts to " + "{:.2f}km".format(calculated_kilometers))
        # check to see if the input is a posititve number and if the miles radio button is selected
        elif valid_distance > 0 and radiobutton_choice.get() == "miles":
            # calculate the distance converting from kilometers to miles
            calculated_miles = valid_distance/1.609
            # output the calculated distance to the label_result_output
            label_result_output.configure(text= str(valid_distance)+"km converts to " + "{:.2f}mi".format(calculated_miles))
        # display error message if the number isn't above 0.
        else:
            label_result_output.configure(text="ERROR: Please enter a positive distance.")
    # except block. display error message if user input isn't a number
    except ValueError:
        label_result_output.configure(text="ERROR: Please enter a numeric distance.")
                                          
def clear_fields(_event = None):
    """function to clear all fields in the window"""
    entry_input.delete(0,END)
    label_result_output.configure(text = "")
    # put focus back on the top entry box
    entry_input.focus()
    # put focus back on kilometer radio button
    radiobutton_choice.set("kilometer")
    
def close_window(_event = None):
    """function to exit the window"""
    sys.exit()

# create a tk instance
window = Tk()

# window properties
window.geometry("350x150")
window.minsize(width=350, height=150)
window.title("Distance Unit Conversion")

# create a Balloon object for tooltips
tooltip = Balloon(window)

# Row 0 widgets
# create a label for the convert widget
label_convert = Label(text="Convert to: ")
label_convert.grid(row=0, column=0, padx=5, pady=5, sticky=E)
# create tooltip for convert widget
tooltip.bind_widget(label_convert, msg = "Choose an option to convert to")

# Use a StringVar to associate with the radiobuttons
radiobutton_choice = StringVar()

# create radio button for kilometer option
radiobutton_kilometer = Radiobutton(window, text="Kilometers", variable=radiobutton_choice, value="kilometer")
radiobutton_kilometer.grid(row=0, column=1,padx=5, pady=5, sticky=W)
# create tooltip for the kilometers radio button widget
tooltip.bind_widget(radiobutton_kilometer, msg = "Convert from miles to kilometers.")
# create radio button for miles option
radiobutton_miles = Radiobutton(window, text="Miles", variable=radiobutton_choice, value="miles")
radiobutton_miles.grid(row=0, column=2, padx=5, sticky=W)
# create tooltip for the miles radio button widget
tooltip.bind_widget(radiobutton_miles, msg = "Convert from kilometers to miles.")

# Row 1 widgets
# create label for user input
label_input = Label(text="Enter Distance: ")
label_input.grid(row=1,column=0,padx=5,pady=5, sticky=E)
# create entry for user input widget
entry_input = Entry(width=30)
entry_input.grid(row=1,column=1,columnspan=2, padx=5,pady=5, sticky=W)
# create tooltip for input widget
tooltip.bind_widget(entry_input, msg = "Enter the distance you want to convert")

# Row 2 widgets
# create label for results widget
label_result = Label(text="Result: ")
label_result.grid(row=2,column=0,padx=5,pady=5, sticky=E)
# create label for results output
label_result_output = Label(width = 32, bd = 2, relief = SUNKEN)
label_result_output.grid(row=2,column=1, columnspan=2, padx=5, pady=5, sticky=W)
# create tooltip for results output widget
tooltip.bind_widget(label_result_output, msg= "Displays the converted distance of your choice")

# Row 3 widgets
# create button to clear all fields
button_clear_fields = Button(text="Clear Fields", width=10, command=clear_fields)
button_clear_fields.grid(row=3,column=0,padx=5,pady=5, sticky=E)
# create tooltip for clear fields button
tooltip.bind_widget(button_clear_fields, msg = "Click to clear all fields")

# create button to calculate distance
button_calculate = Button(text="Calculate", width=10,command=calculate_distance)
button_calculate.grid(row=3,column=1,padx=5,pady=5,sticky=E)
# create tooltip for calculate button
tooltip.bind_widget(button_calculate, msg = "Click to calculate the conversion of your choice")

# create button to quit program
button_quit = Button(text="Quit", width=10, command=close_window)
button_quit.grid(row=3,column=2,padx=10,pady=5,sticky=E)
# create tooltip for the button_quit widget
tooltip.bind_widget(button_quit, msg = "Click to exit the application")

# By default when opening the window select the kilometer radio button
radiobutton_choice.set("kilometer")

# add hotkey support
window.bind("<Alt-z>", clear_fields)
window.bind("<Alt-x>", calculate_distance)
window.bind("<Return>", calculate_distance)
window.bind("<Alt-c>", close_window)

# Run the main loop
window.mainloop()