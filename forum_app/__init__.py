from flask import Flask, render_template

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='jinja2_templates')