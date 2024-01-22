from flask import Blueprint, render_template, request, flash, jsonify
from spellchecker import SpellChecker
from black import format_str
import autopep8
import json
import subprocess
import re

pasteBin = Blueprint('pasteBin', __name__)

@pasteBin.route('/pasteBin', methods=['GET', 'POST'])
def pasteBinPage():
    return render_template("pasteBin.html")

@pasteBin.route('/format_text', methods=['POST'])
def format_text():
     # Receive data from the client (JavaScript)
    data = request.json
    text = data.get('text')
    language = data.get('language')
    if language == "Select Language":
        language = autoDetect(text)
    # Implement formatting logic based on the selected language
    formatted_text = ''
    try:
        if language == 'python':
            formatted_text = autopep8.fix_code(text)
        elif language == 'c/java':
            formatted_text = format_str(text, mode=True)
        elif language == 'asm':
            formatted_text = 'ASM Formatted: ' + text
        else:
            paragraphs = text.split('\n\n')
            formatted_paragraphs = []
            for paragraph in paragraphs:
                paragraph = paragraph.strip()
                lines = paragraph.split('\n')
                indented_lines = ['    ' + line.strip() for line in lines]
                formatted_paragraph = '\n'.join(indented_lines)
                formatted_paragraphs.append(formatted_paragraph)
            formatted_text = '\n\n'.join(formatted_paragraphs)
    except:
        formatted_text = text
        print("error")

    # Return formatted text to the client (JavaScript)
    return jsonify({'formatted_text': formatted_text, 'updatedLanguage': language})


def autoDetect(input):
    # Check for common Python keywords and patterns
    python_keywords = ['def', 'class', 'if', 'else', 'for', 'while', 'import']
    python_pattern = re.compile(r'\b(?:' + '|'.join(python_keywords) + r')\b')

    # Check for common C/Java keywords and patterns
    c_java_keywords = ['int', 'float', 'char', 'void', 'if', 'else', 'for', 'while']
    c_java_pattern = re.compile(r'\b(?:' + '|'.join(c_java_keywords) + r')\b')

    # Count occurrences of key characters for general text detection
    semi_colon_count = input.count(';')
    curly_bracket_count = input.count('{') + text.count('}')
    
    # Determine text type based on patterns and counts
    if python_pattern.search(input):
        return 'python'
    elif c_java_pattern.search(input) and semi_colon_count > 0 and curly_bracket_count > 0:
        return 'c_java'
    else:
        return 'gen'

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