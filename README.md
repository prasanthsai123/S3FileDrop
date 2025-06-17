# S3FileDrop
S3FileDrop is a lightweight web application built using Flask and AWS S3. It allows users to upload files via a simple web interface and generates secure presigned URLs for file sharing. No login required, no public file access — just fast, temporary links that expire automatically.



#How to set up......
-> First we need to create one S3 bucket in AWS.
-> Then create one user in IAM.
-> Now, copy your "aws_access_key_id, aws_secret_access_key".

-> Now download "AWSCLIV2" in your system.
-> Now download files from my git (app.py and index.html) in one folder.
   Example :
         file-transfer-app/
                  ├── app.py             → main Flask app
                  ├── templates/         →(new folder)
                        └── index.html   → HTML upload form
                        
-> Open cmd (command prompt) and execute these commands
    => cd files-transfer-app (in place of 'files-transfer-app' this give your folder name that where you save the python code).
    => pip install flask boto3.
    => python app.py
-> You can see your localhost, example : (http://127.0.0.1:5000/).
-> Copy that and paste it in any browser.


That's awesome to hear! 🎉 I'm glad it's working smoothly now.


**If you're facing any challenges, feel free to connect with me via LinkedIn.** 
https://www.linkedin.com/in/vutukuri-sai-prasanth-4111631b8/
