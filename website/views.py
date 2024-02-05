from flask import Blueprint, render_template, request, flash, jsonify, send_from_directory
import json
import csv
import os

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@views.route('/textEditor', methods=['GET', 'POST'])
def textEditor():
    return render_template("textEditor.html")

@views.route('/images', methods=['GET', 'POST'])
def images():
    return render_template("images.html")

@views.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # Process form data
        message = request.form['message']
        email = request.form['suggestion-email']
        # Check if the CSV file exists, create it if not
        if not os.path.exists("website/static/messeages/notes.csv"):
            with open("website/static/messeages/notes.csv", 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Add header row if the file is newly created
                csv_writer.writerow(['Email', 'Message'])

        # Add a new row to the CSV file
        with open("website/static/messeages/notes.csv", 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([email, message])

    return render_template("about.html")

@views.route('/search/<query>')
def search(query):
    print("?")