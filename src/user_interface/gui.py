# src/user_interface/gui.py
import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("Bitcoin Tracker User Interface")

    # Placeholder GUI elements
    label = tk.Label(root, text="Welcome to Bitcoin Tracker!")
    label.pack(pady=10)

    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack(pady=10)

    root.mainloop()

def on_button_click():
    print("Button Clicked!")
