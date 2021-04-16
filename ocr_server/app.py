import os
import sys
import pyrebase
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename

# import our OCR function
from ocr_core import ocr_core
from recipt_parser import recipt_parser
from recipesFinder import recipesFinder

# define a folder to store and later serve the images
config = {
    "apiKey": "AIzaSyDndI7zOsl3kUQptIIZenw0eQ4B7lA8jzA",
    "authDomain": "recipefinder-f1bd3.firebaseapp.com",
    "databaseURL": "https://recipefinder-f1bd3-default-rtdb.firebaseio.com",
    "projectId": "recipefinder-f1bd3",
    "storageBucket": "recipefinder-f1bd3.appspot.com",
    "messagingSenderId": "957469821622",
    "appId": "1:957469821622:web:453fb296ca38bed40b3417",
    "measurementId": "G-P7KGSFSPE1"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


UPLOAD_FOLDER = os.path.join('static', 'uploads')

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# function to check the file extension


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the home page


@app.route('/')
def home_page():
    return render_template('index.html')

# route and function to handle the upload page


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # call the OCR function on it
            extracted_text = ocr_core(file)
            # print(extracted_text, file=sys.stderr)
            recipt_parser(extracted_text)
            recipes = recipesFinder()
            # print(recipes, file=sys.stderr)
            full_filename = os.path.join(
                app.config['UPLOAD_FOLDER'], filename)
            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=full_filename,
                                   recipes=recipes)
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run()
