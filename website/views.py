from flask import Blueprint, render_template, request, flash, jsonify, send_from_directory,url_for,current_app
import json
import csv
import os
import csv

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@views.route('/textEditor', methods=['GET', 'POST'])
def textEditor():
    return render_template("textEditor.html")

@views.route('/encondingTable', methods=['GET', 'POST'])
def encondingTable():
    return render_template("encondingTable.html")


@views.route('/data/<info_type>')
def get_data(info_type):
    if info_type == 'ascii':
        filename = 'ascii.csv'
    elif info_type == 'unicode':
        filename = 'unicode.csv'
    else:
        return jsonify({'error': 'Invalid info_type'})

    csv_path = os.path.join(current_app.static_folder, 'files', filename)

    # Check if the file exists
    if not os.path.exists(csv_path):
        return jsonify({'error': 'File not found'})

    # Read and return the CSV data
    with open(csv_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return jsonify(data)

@views.route('/images', methods=['GET', 'POST'])
def images():
    return render_template("images.html")

@views.route('/search', methods=['GET', 'POST'])
def search():
    search_query = request.args.get('q', '') 
    if not search_query:
        search_query = "Search..."

    return render_template("search.html", search_query=search_query)

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
