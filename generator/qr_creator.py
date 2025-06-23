import qrcode
import os

def QrCodeCreator(
    text: str,
    version_input=None,
    correction_input='M',
    box_size=10,
    border_size=4,
    fill_color='black',
    back_color='white'
):
    # Mapping of user input to qrcode constants
    correction_map = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H
    }

    # Handle version
    version = int(version_input) if version_input and str(version_input).strip() else None

    # Validate correction level
    error_correction = correction_map.get(correction_input.upper(), qrcode.constants.ERROR_CORRECT_M)

    # Create QR code object
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=int(box_size),
        border=int(border_size),
    )

    qr.add_data(text)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img
