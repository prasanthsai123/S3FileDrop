#cd files-transfer-app
#pip install flask boto3
#python app.py


from flask import Flask, render_template, request, redirect, flash
import boto3
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # You can change this

# AWS S3 Configuration
s3 = boto3.client(
    's3',
    aws_access_key_id='Yours_id',
    aws_secret_access_key='Yours_key',
    region_name='yours_region'  
)

BUCKET_NAME = 'filestransfersdemo'  # Change to your bucket name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']

        if file:
            filename = secure_filename(file.filename)
            print("📦 Selected file:", filename)

            try:
                print("🚀 Uploading to S3...")
                s3.upload_fileobj(
                    file,
                    BUCKET_NAME,
                    filename,
                    ExtraArgs={}  # this makes file accessible via link
                )
                file_url = f"https://{BUCKET_NAME}.eu-north-1.amazonaws.com/{filename}"
                print("✅ Upload successful:", file_url)

                flash(f"✅ File uploaded successfully! Shareable Link: {file_url}")

            except Exception as e:
                print("❌ Upload failed:", str(e))  # ← prints in terminal
                flash(f"❌ Upload failed: {str(e)}")  # ← shows in browser

            return redirect('/')  # return to upload form after POST

    return render_template('index.html')  # Show upload form on GET

if __name__ == '__main__':
    print("🚀 Starting Flask App...")
    app.run(debug=True)
