from flask import Blueprint, render_template, request, flash, jsonify
import json
from flask_wtf import FlaskForm
from wtforms import FileField , SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from . import app_instance as app

fileConverter = Blueprint('fileConverter', __name__)

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@fileConverter.route('/fileConverter', methods=['GET', 'POST'])
def fileConverterPage():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        if file:  
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
            flash("File has been uploaded successfully.", 'success')
        else:
            flash("No file was uploaded.", 'error')

    return render_template("fileConverter.html" , form = form)
