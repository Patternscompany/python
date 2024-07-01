from flask import Flask, request, send_file
import qrcode
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <body>
                <h1>QR Code Generator</h1>
                <form action="/generate_qr" method="post">
                    <label for="data">Enter data for QR code:</label>
                    <input type="text" id="data" name="data">
                    <input type="submit" value="Generate QR Code">
                </form>
            </body>
        </html>
    '''

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']
    img = qrcode.make(data)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png', as_attachment=True, download_name='qr_code.png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
