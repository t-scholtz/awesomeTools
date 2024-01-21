from flask import Blueprint, render_template, request, flash, jsonify
from spellchecker import SpellChecker

import autopep8
import json
import subprocess

pasteBin = Blueprint('pasteBin', __name__)


@pasteBin.route('/format_text', methods=['POST'])
def format_text():
    print("formate called")
     # Receive data from the client (JavaScript)
    data = request.json
    text = data.get('text')
    language = data.get('language')
    print(text+language)
    # Implement formatting logic based on the selected language
    formatted_text = ''
    try:
        if language == 'python':
            formatted_text = autopep8.fix_code(text)
        elif language == 'c/java':
            formatted_text = subprocess.check_output(['clang-format', '-style=Google'], input=text.encode('utf-8'), text=True)
        elif language == 'asm':
            formatted_text = 'ASM Formatted: ' + text
        else:
            # Default formatting logic
            formatted_text = text
    except:
        formatted_text = text
        print("error")

    # Return formatted text to the client (JavaScript)
    return jsonify({'formatted_text': formatted_text})


@pasteBin.route('/spell_Check', methods=['POST'])
def SpellCheck():
    print("spellCheck")
     # Receive data from the client (JavaScript)
    data = request.json
    text = data.get('text')
    print(text)
    spell = SpellChecker()
    # Split the text into words
    words = text.split()
    # Get misspelled words
    misspelled = spell.unknown(words)

    # Correct misspelled words
    corrected_text = []
    for word in words:
        if word in misspelled:
            # Correct misspelled word
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)

    # Join the corrected words back into a sentence
    corrected_text = ' '.join(corrected_text)

    # Return formatted text to the client (JavaScript)
    return jsonify({'formatted_text': corrected_text})