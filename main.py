from flask import Flask, Response , make_response , request
from qrcode import make , QRCode, constants
from io import BytesIO

app = Flask(__name__)

@app.route('/qrcode', methods=['GET'])
def qr_code():
    url = request.args.get(url)
    if not url:
        return "No URL provided", 400
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    # print(url)
    qr.add_data(url)
    # create qr code image
    qr.make(fit=True)
    # save qr code image to buffer
    img = qr.make_image(fill_color="black", back_color="white")
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    # create response
    response = make_response(byte_io.getvalue())
    response.mimetype = 'image/png'
    return response

if __name__ == '__main__':
    app.run(debug=True , port=5022)
