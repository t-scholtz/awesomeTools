from flask import Blueprint, render_template, request, flash, jsonify, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

fileConverter = Blueprint('fileConverter', __name__)

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

class ConversionForm(FlaskForm):
    conversion_choices = [('pdf', 'PDF'), ('txt', 'Text'), ('csv', 'CSV')]  # Add more choices as needed
    conversion = SelectField('Conversion Type', choices=conversion_choices)
    submit_conversion = SubmitField('Convert')

@fileConverter.route('/fileConverter', methods=['GET', 'POST'])
def fileConverterPage():
    from main import getApp
    form = UploadFileForm()
    conversion_form = ConversionForm()

    if form.validate_on_submit():
        file = form.file.data
        if file:
            file_extension = os.path.splitext(file.filename)[1][1:]  # Get the file extension
            possible_conversions = get_possible_conversions(file_extension)
            
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), getApp().config['UPLOAD_FOLDER'], secure_filename(file.filename)))
            flash("File has been uploaded successfully.", 'success')
            
            # Populate the conversion form choices based on the file extension
            conversion_form.conversion.choices = possible_conversions

    return render_template("fileConverter.html", form=form, conversion_form=conversion_form)

@fileConverter.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(os.path.abspath(os.path.dirname(__file__)), getApp().config['UPLOAD_FOLDER'], filename)

def get_possible_conversions(file_extension):
    # Add logic here to determine possible conversions based on file extension
    # For example, you can define a dictionary mapping extensions to possible conversions
    conversion_mapping = {
        'pdf': ['txt', 'csv'],
        'txt': ['pdf', 'csv'],
        'csv': ['pdf', 'txt']
        # Add more mappings as needed
    }

    return [(ext, ext.upper()) for ext in conversion_mapping.get(file_extension, [])]

