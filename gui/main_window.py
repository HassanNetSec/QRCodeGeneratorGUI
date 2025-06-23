### gui/main_window.py
import tkinter as tk
from gui.input_widgets import create_widgets

def start_gui():
    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("600x500")

    create_widgets(root)

    root.mainloop()


