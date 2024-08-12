
from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    file_contents = file.read()
    md5_hash = hashlib.md5(file_contents).hexdigest()

    return jsonify({'filename': file.filename, 'md5_hash': md5_hash})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
