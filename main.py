import qrcode

# Data to encode
data = "https://www.twitch.tv/pipluptiny"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qrcode.png")

print("QR code created and saved as 'qrcode.png'")
