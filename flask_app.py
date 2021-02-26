from flask import Flask, render_template

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='jinja2_templates')

@app.route('/')
def root_page():
    #return app.config
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31000, debug=True)