from os import path
from flask import render_template, session, request, redirect, url_for
from markdown import markdown
from forum_app import app, app_path

from forum_app.features.dice import DiceFeature
import logging

@app.route('/dice/')
def root_dice_page():
    return redirect(url_for('dice_page', notation='d6'))

@app.route('/dice/<notation>')
def dice_page(notation):
    """Go to dice page
    If you just want a value, use API at
    /api/dice/roll/<notation>
    """
    dice = DiceFeature()
    
    (num, side) = dice.parse_dice_notation(notation)
    
    # return "2d6"
    # file_name = name if name.endswith('.md') else f"{name}.md"

    # file_path = path.join(app_path, 'data', 'markdown', file_name)

    # if not path.exists(file_path):
    #     return "FILE DOES NOT EXISTS.", 404

    # with open(file_path, 'r', encoding='utf8') as infile:
    #     markdown_text = infile.read()

    # # return render_template('authentication/login_get.html', message = message)
    # return markdown(markdown_text)
    return render_template('dice/dice_dashboard.html', number_of_dice = num, dice_sides = side)
