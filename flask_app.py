from flask import Flask, render_template
#from api.website import api_datetime

from app import app



@app.route('/')
def root_page():
    #return app.config
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31000, debug=True)