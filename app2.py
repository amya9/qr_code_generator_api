from flask import Flask, request, jsonify
from qrcode import QRCode
from PIL import Image

app = Flask(__name__)
# final script which is working fine
@app.route('/qr', methods=['GET'])
def generate_qr():
    url = request.args.get('url')
    qr = QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to a file
    img.save("qrcode.png")

    # Open the QR code image file
    with open("qrcode.png", "rb") as f:
        qr_code = f.read()

    # Send the QR code image as the API response
    return qr_code, 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(debug=True , port=5023)
