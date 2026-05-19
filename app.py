from flask import Flask, render_template, request
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import boto3
import os

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted"
DECRYPTED_FOLDER = "decrypted"

key = os.getenv("FERNET_KEY").encode()

fernet = Fernet(key)

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION")
)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():

    file = request.files['file']

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(filepath)

    with open(filepath, 'rb') as f:
        original_data = f.read()

    encrypted_data = fernet.encrypt(original_data)

    encrypted_filename = file.filename + ".encrypted"

    encrypted_path = os.path.join(
        ENCRYPTED_FOLDER,
        encrypted_filename
    )

    with open(encrypted_path, 'wb') as f:
        f.write(encrypted_data)

    s3.upload_file(
        encrypted_path,
        os.getenv("AWS_BUCKET_NAME"),
        encrypted_filename
    )

    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_path = os.path.join(
        DECRYPTED_FOLDER,
        file.filename
    )

    with open(decrypted_path, 'wb') as f:
        f.write(decrypted_data)

    signed_url = s3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': os.getenv("AWS_BUCKET_NAME"),
            'Key': encrypted_filename
        },
        ExpiresIn=300
    )

    return f'''
    File uploaded, encrypted, decrypted and stored successfully

    <br><br>

    <a href="{signed_url}">
    Download Encrypted File
    </a>
    '''

if __name__ == '__main__':
    app.run(debug=True)