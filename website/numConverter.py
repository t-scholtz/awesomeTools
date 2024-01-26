from flask import Blueprint, render_template, request, flash, jsonify

numConverter = Blueprint('numConverter', __name__)

@numConverter.route('/numconverter', methods=['GET', 'POST'])
def pasteBinPage():
    return render_template("numConverter.html")