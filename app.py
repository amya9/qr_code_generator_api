from flask import Flask, request, make_response
from qrcode import QRCode, constants

app = Flask(__name__)

@app.route('/qrcode/<string:url>', methods=['GET'])
def generate_qr_code(url):
    # url = request.args.get('url')
    if not url:
        return "No URL provided", 400
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    response = make_response(img.get_buffer().read())
    response.content_type = 'image/png'
    return response

if __name__ == '__main__':
    app.run(debug=True)
