from forum_app import app

if __name__ == '__main__':
    print("Running application on localhost:31000")
    app.run(host='0.0.0.0', port=31000, debug=True)