from PIL import Image
import os

def paste_logo_on_qr(qr_path, logo_path, output_path):
    # Open images
    qr_image = Image.open(qr_path).convert("RGB")
    logo_image = Image.open(logo_path).convert("RGBA")  # Keep transparency if available

    # Get dimensions
    qr_width, qr_height = qr_image.size
    logo_size = int(qr_width * 0.2)  # 20% of QR size

    # Resize logo while keeping aspect ratio
    logo_image.thumbnail((logo_size, logo_size), Image.LANCZOS)

    # Calculate position to center the logo
    pos_x = (qr_width - logo_image.width) // 2
    pos_y = (qr_height - logo_image.height) // 2

    # Paste logo using mask for transparency
    qr_image.paste(logo_image, (pos_x, pos_y), logo_image)

    # Save result
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    qr_image.save(output_path)
    print(f"QR code with logo saved to {output_path}")

# Example usage:
paste_logo_on_qr(
    qr_path='data/qrcodes/qrCode.png',
    logo_path='logo/logo.jpg',
    output_path='data/qrcodes/qrCode_with_logo.png'
)
