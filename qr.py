from flask import Flask, request, make_response
import qrcode
import io
app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def qr():
    # Get the URL from the query string
    url = request.args.get('url')
    # Create a Qr code image
    img = qrcode.make(url)
    # Save the QR CODE IMAGE TO A buffer
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    # Createthe response object
    response = make_response(buffer.getvalue())
    response.mimetype = 'image/png'
    # Return the response
    return response

if __name__ == "__main__":
    app.run()
