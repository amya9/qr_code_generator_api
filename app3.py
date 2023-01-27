from flask import Flask, request, jsonify, make_response
from qrcode import QRCode
from PIL import Image
from io import BytesIO
app = Flask(__name__)

# script to download qrcode  use this code only
@app.route('/qr', methods=['GET'])
def generate_qr():
    url = request.args.get('url')
    qr = QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")


    # Save the QR code image to a file
    # byte_io = BytesIO()
    img.save("qrcode.png")
    # byte_io.seek(0)
    # Open the QR code image file
    with open("qrcode.png", "rb") as f:
        qr_code = f.read()

    # Create the response with the appropriate headers
    response = make_response(qr_code)
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='qrcode.png')

    return response

if __name__ == '__main__':
    app.run(debug=True , port=5024)
