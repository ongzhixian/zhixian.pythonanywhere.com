from os import path
from forum_app import app, app_path
from markdown import markdown

@app.route('/dice/<notation>')
def dice_page(notation):
    return "2d6"
    # file_name = name if name.endswith('.md') else f"{name}.md"

    # file_path = path.join(app_path, 'data', 'markdown', file_name)

    # if not path.exists(file_path):
    #     return "FILE DOES NOT EXISTS.", 404

    # with open(file_path, 'r', encoding='utf8') as infile:
    #     markdown_text = infile.read()

    # # return render_template('authentication/login_get.html', message = message)
    # return markdown(markdown_text)
