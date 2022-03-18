# Overview

## What to do after a new clone

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt

python .\flask_app.py


## Create
python -c 'import secrets; print(secrets.token_hex())'