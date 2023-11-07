import tkinter as tk
from tkinter import ttk

# Function to be executed when the button is clicked
def button_click():
    text = entry.get()
    num = int(numeric_field.get())
    selected_option = dropdown_var.get()
    result_label.config(text=f"Text: {text}, Number: {num}, Option: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Python GUI Demo")

# Set the width and height of the main window
root.geometry("400x200")  # Width x Height

# Create a label
label = tk.Label(root, text="Enter Text:")
label.pack()

# Create a text field
entry = tk.Entry(root)
entry.pack()

# Create a label for numeric field
numeric_label = tk.Label(root, text="Enter Number:")
numeric_label.pack()

# Create a numeric field using Entry widget
numeric_field = tk.Entry(root)
numeric_field.pack()

# Create a label for the dropdown menu
dropdown_label = tk.Label(root, text="Select an Option:")
dropdown_label.pack()

# Create a dropdown menu
options = ["Option 1", "Option 2", "Option 3"]
dropdown_var = tk.StringVar(root)
dropdown_menu = ttk.Combobox(root, textvariable=dropdown_var, values=options)
dropdown_menu.pack()

# Create a button
button = tk.Button(root, text="Submit", command=button_click)
button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
