from flask import Flask, request, make_response, render_template
import qrcode
import io

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/qr', methods=['POST'])
def qr():
    # Get the text from the query string
    # url = request.args.get('text')

    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    # Print the input text
    # print(f'Input text: {user_input}')
    if name == '':
        e = ''
    else:
        e = '\n Name: ' + name
    if phone == '':
        phone = ''
    else:
        phone = '\n Phone: ' + phone
    if email == '':
        email = ''
    else:
        email = '\n Email:' + email
    k = name + phone + email
    # Create a Qr code image
    img = qrcode.make(k)
    # Save the QR CODE IMAGE TO A buffer
    buffer = io.BytesIO()
    img.save(buffer)  # , format='PNG')
    buffer.seek(0)
    # Createthe response object
    response = make_response(buffer.getvalue())
    response.mimetype = 'image/png'
    # Return the response
    return response


if __name__ == "__main__":
    app.run(debug=TRUE)
