import os
from flask import Flask
from flask import request
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.get("/")
def form():
    html ="""
    <form action="/" enctype="multipart/form-data" method="post">
        <input type="file" id="file-input" name="uploaded_file">
        <input type="submit">
    </form>
    """
    return html

@app.post("/")
def submit_form():
    file = request.files['uploaded_file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('.', filename))
    return "File uploaded succesfully"