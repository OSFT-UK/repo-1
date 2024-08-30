# Import tkinter module for GUI
import tkinter as tk
from tkinter import ttk

# Import math module for scientific functions
import math

# Define the main window
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("300x400")
# Remove the window.resizable(0, 0) line to make the window resizable
# window.resizable(0, 0)

# Define the display entry
display = tk.Entry(window, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Define the buttons
buttons = [
    "(", ")", "%", "AC",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    ".", "0", "=", "+",
    "sin", "cos", "tan", "log",
    "sqrt", "pi", "e", "^"
]

# Define the button click function
def button_click(event):
    # Get the text of the button
    text = event.widget.cget("text")
    
    # If the text is AC, clear the display
    if text == "AC":
        display.delete(0, tk.END)
    
    # If the text is =, evaluate the expression
    elif text == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    
    # If the text is a scientific function, apply it to the display
    elif text in ["sin", "cos", "tan", "log", "sqrt"]:
        try:
            value = float(display.get())
            result = getattr(math, text)(value)
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    
    # If the text is pi or e, insert their values
    elif text in ["pi", "e"]:
        display.insert(tk.END, str(getattr(math, text)))
    
    # If the text is ^, insert **
    elif text == "^":
        display.insert(tk.END, "**")
    
    # Otherwise, insert the text to the display
    else:
        display.insert(tk.END, text)

# Create and place the buttons on a grid
row = 1
col = 0
for button in buttons:
    btn = ttk.Button(window, text=button)
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    btn.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        row += 1
        col = 0

# Start the main loop
window.mainloop()
