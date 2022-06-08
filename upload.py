import os
import time

from flask import Flask, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images'


app = Flask(__name__, static_url_path="/static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def upload_file():
    file = None
    if "photoUrl" in request.files.keys():
        file = request.files['photoUrl']
    if not file:
        return ""
    if file == None:
        return ""

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'tiff', 'tif', 'bmp', 'svg', 'ico', 'webp'}
    msec = int(round(time.time() * 1000))
    ext = file.filename.split('.')[-1]
    if file and ext.lower() in ALLOWED_EXTENSIONS:
        filename = secure_filename(file.filename)
        photo_name = file.filename.split('.')[0]
        photo_name += str(msec)
        photo_name += '.'
        photo_name += ext
        filename = photo_name
        file.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), app.config['UPLOAD_FOLDER'], filename))
        return os.path.sep + 'images' + os.path.sep + filename
    else:
        return False
