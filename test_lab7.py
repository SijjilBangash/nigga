import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x150")

# Create a label widget
label = tk.Label(root, text="Click the button below")
label.pack(pady=10)

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()
