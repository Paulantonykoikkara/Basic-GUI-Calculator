import tkinter as tk

# Function to handle button clicks
def click(event):
    current = display.get()
    text = event.widget.cget('text')

    if text == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)

# Main window setup
window = tk.Tk()
window.title("Basic GUI Calculator")

# Entry widget for display
display = tk.Entry(window, font=("Arial", 25), justify="right")
display.pack(fill=tk.X, padx=10, pady=10, ipady=10)

# Frame for buttons
btn_frame = tk.Frame(window)
btn_frame.pack()

# Button labels layout
button_labels = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

# Create and place buttons in the grid
for row in button_labels:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack()
    for label in row:
        btn = tk.Button(row_frame, text=label, font=("Arial", 20), width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

# Run the application
window.mainloop()