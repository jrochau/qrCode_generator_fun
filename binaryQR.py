import qrcode
import base64

# Create QR code instance
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )

# Encode binary data to base64
data = b'''
".............................stuff...................."
'''
qr.add_data(data)

# Compile QR code
qr.make(fit=True)

# Print the QR as ASCII art
qr.print_ascii()
