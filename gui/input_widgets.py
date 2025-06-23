import tkinter as tk
from tkinter import filedialog, colorchooser
from gui.event_bindings import generate_qr, select_file

entries = {}

def create_widgets(root):
    global entries

    root.title("QR Code Generator")
    root.geometry("500x600")
    root.configure(bg="#f0f0f0")  # Light gray background

    font_label = ("Helvetica", 10, "bold")
    font_entry = ("Helvetica", 10)

    main_frame = tk.Frame(root, padx=20, pady=20, bg="#f0f0f0")
    main_frame.pack(expand=True)

    def add_label(text):
        return tk.Label(main_frame, text=text, font=font_label, bg="#f0f0f0")

    def add_entry(key):
        entries[key] = tk.Entry(main_frame, font=font_entry, width=40)
        entries[key].pack(pady=(0, 10))

    # Text input
    add_label("Enter text or URL:").pack(anchor="w")
    add_entry('text')

    # Version input
    add_label("QR Version (1–40 or blank):").pack(anchor="w")
    add_entry('version')

    # Error Correction
    add_label("Error Correction (L, M, Q, H):").pack(anchor="w")
    add_entry('correction')

    # Box size
    add_label("Box Size:").pack(anchor="w")
    add_entry('box')

    # Border size
    add_label("Border Size:").pack(anchor="w")
    add_entry('border')

    # Fill color
    entries['fill'] = tk.StringVar()
    tk.Button(main_frame, text="Choose Fill Color", command=lambda: choose_color('fill'), width=25).pack(pady=5)
    tk.Label(main_frame, textvariable=entries['fill'], bg="#f0f0f0").pack()

    # Background color
    entries['back'] = tk.StringVar()
    tk.Button(main_frame, text="Choose Background Color", command=lambda: choose_color('back'), width=25).pack(pady=5)
    tk.Label(main_frame, textvariable=entries['back'], bg="#f0f0f0").pack()

    # Output file name
    add_label("Output File Name (without .png):").pack(anchor="w")
    add_entry('filename')

    # Generate QR Button
    tk.Button(main_frame, text="Generate QR Code", command=lambda: generate_qr(entries),
              bg="#4CAF50", fg="white", font=font_label, width=30).pack(pady=15)

    # Batch File Button
    tk.Button(main_frame, text="Batch Generate from File", command=select_file,
              bg="#2196F3", fg="white", font=font_label, width=30).pack(pady=5)


def choose_color(key):
    color = colorchooser.askcolor()[1]
    if color:
        entries[key].set(color)
