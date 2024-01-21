from flask import Blueprint, render_template, request, flash, jsonify
import json

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

    return render_template("about.html")

