# Features

Features should be defined in `features` folder as a module.

Web page routes should be defined in `forum_app.pages.<feature-module-name>` module file.

Web pages files should be defined in `jinja_templates\<feature-module-name>` folder.

## What this mean

`forum_app.features.authentication`

If I'm defining a feature in `forum_app\features\authentication.py`

Website templates files should be placed in `forum_app\jinja2_templates\authentication` folder.

Routes should be defined in `forum_app\pages\authentication.py` module.


As a example see `forum_app.features.authentication` module.