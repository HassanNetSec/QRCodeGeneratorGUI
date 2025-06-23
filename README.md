# QRCodeGeneratorGUI

A customizable QR Code Generator with a graphical interface built using Python and Tkinter. Supports both single QR code creation and batch generation from CSV/TXT files. Easily choose colors, version, error correction, and size.

## 🧩 Features

- ✅ Generate QR codes from text or URLs
- 🎨 Customize fill and background colors
- 🧱 Set QR version, box size, and border
- 🔒 Choose error correction level (L, M, Q, H)
- 📁 Batch generate QR codes from file input (.csv or .txt)
- 💾 Save QR codes to local directory (`data/qrcodes/`)

## 📸 GUI Preview

*(Insert screenshot if available)*

## 🛠️ Technologies

- Python 3.x
- Tkinter
- qrcode (Python library)
- Pillow (image processing)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/HassanNetSec/QRCodeGeneratorGUI.git
cd QRCodeGeneratorGUI
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python app.py
```

## 📂 Project Structure

```
QRCodeGeneratorGUI/
│
├── app.py
├── requirements.txt
├── generator/
│   ├── qr_creator.py
│   └── file_handler.py
│
├── gui/
│   ├── __init__.py
│   ├── main_window.py
│   ├── input_widgets.py
│   └── event_bindings.py
│
├── data/
│   └── qrcodes/
│
└── README.md
```

## 📑 File Input Format for Batch Generation

- `.csv` or `.txt` files
- Each line should be: `text,filename,version,error_correction,box,border,fill_color,back_color`

Example:
```
https://example.com,example,1,M,10,4,black,white
```

## 📌 To-Do

- [ ] Add logo overlay support
- [ ] Dark/light theme toggle

## 🤝 License

MIT License

---

Made with ❤️ by [Hassan Khan](https://github.com/HassanNetSec)
