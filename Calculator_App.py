# Import the tkinter library for creating the graphical user interface
from tkinter import *
# Import the ast module for abstract syntax tree operations
import ast

# Create the main window
root = Tk()
root.geometry("400x600")  # Set the initial dimensions of the main window

i = 0

# Function to insert the clicked number into the display area
def get_number(num):
    global i
    display.insert(i, num)
    i += 1

# Function to insert the clicked operation into the display area
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

# Function to clear all text in the display area
def clear_all():
    display.delete(0, END)

# Function to evaluate the expression and insert the result into the display area
def calculate():
    entire_string = display.get()
    try:
        # Parse the input expression into an AST node
        node = ast.parse(entire_string, mode="eval")
        # Evaluate the node to calculate the result
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Function to undo the last character entered
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")

# Create the display area with an increased font size
display = Entry(root, font=("Arial", 30))
display.grid(row=1, columnspan=6, padx=20, pady=20)

# List of number buttons (1-9)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        if counter < len(numbers):
            button_text = numbers[counter]
            button = Button(root, text=button_text, width=6, height=3, font=("Arial", 18), command=lambda text=button_text: get_number(text))
            button.grid(row=x + 2, column=y, padx=10, pady=10)
            counter += 1

# Button for the number 0
button = Button(root, text="0", width=6, height=3, font=("Arial", 18), command=lambda: get_number(0))
button.grid(row=5, column=1)

# List of operation buttons (+, -, *, /, *3.14, %, (, **, ), **2)
count = 0
operations = ['+', '-', '*', '/', '*3.14', '%', '(', '**', ')', '**2']
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], width=6, height=3, font=("Arial", 18), command=lambda text=operations[count]: get_operation(text))
            count += 1
            button.grid(row=x + 2, column=y + 3, padx=10, pady=10)

# Buttons for clear, calculate, and undo
Button(root, text="C", width=6, height=3, font=("Arial", 18), command=clear_all).grid(row=5, column=0, padx=10, pady=10)
Button(root, text="=", width=6, height=3, font=("Arial", 18), command=calculate).grid(row=5, column=2, padx=10, pady=10)
Button(root, text="<--", width=6, height=3, font=("Arial", 18), command=lambda: undo()).grid(row=5, column=4, padx=10, pady=10)

# Start the main loop to run the application
root.mainloop()
