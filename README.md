# Python
import tkinter as tk

# Function to update the expression in the input field
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + key)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create input field
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        b = tk.Button(root, text=button, padx=20, pady=20, command=evaluate)
    elif button == 'C':
        b = tk.Button(root, text=button, padx=20, pady=20, command=clear)
    else:
        b = tk.Button(root, text=button, padx=20, pady=20, command=lambda key=button: press(key))
    
    b.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
