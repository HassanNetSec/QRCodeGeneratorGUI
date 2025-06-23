### gui/event_bindings.py
import tkinter as tk
from tkinter import messagebox, filedialog
from generator.qr_creator import QrCodeCreator
from generator.file_handler import handleFile
import os


def generate_qr(entries):
    try:
        text = entries['text'].get()
        version = entries['version'].get()
        correction = entries['correction'].get().upper()
        box = int(entries['box'].get())
        border = int(entries['border'].get())
        fill = entries['fill'].get()
        back = entries['back'].get()
        filename = entries['filename'].get()

        img = QrCodeCreator(text, version, correction, box, border, fill, back)

        save_path = f"data/qrcodes/{filename}.png"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        img.save(save_path)

        messagebox.showinfo("Success", f"QR Code saved to {save_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR Code: {e}")


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text/CSV Files", "*.txt *.csv")])
    if file_path:
        try:
            handleFile(file_path)
            messagebox.showinfo("Success", "Batch QR Code generation completed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
