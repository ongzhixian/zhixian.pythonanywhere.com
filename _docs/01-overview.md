# Overview

## What to do after a new clone

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt

python .\flask_app.py

"{}" > $env:USERPROFILE\.pythonanywhere.json
notepad $env:USERPROFILE\.pythonanywhere.json
{
    "HOST": "mysql-host",
    "PORT": "mysql-port",
    "USERNAME": "root",
    "PASSWORD": "pass1234",
    "DATABASE": "forum"
}


## Create
python -c 'import secrets; print(secrets.token_hex())'

## Using ApexCharts

https://apexcharts.com/docs/chart-types/pie-donut/


## Setup testing database on Kubernetes (Minikube)

1.  Check if we have MySql docker image using `minikube image list`
    The image that we want is `docker.io/library/mysql:5.7`

    If we do not have the image "load" it with `minikube image load mysql:5.7`

tldr;

docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:5.7

minikube kubectl -- create deployment mysql-minikube --image=mysql:5.7
minikube kubectl -- set env deployment/mysql-minikube MYSQL_ROOT_PASSWORD=pass1234
minikube kubectl -- expose deployment mysql-minikube --type=NodePort --port=3306


# Notes PythonAnywhere

Latest version of Python supported is 3.7
Latest version of MySql  supported is 5.7.34

# Reference

Github google / material-design-lite 
https://github.com/google/material-design-lite/tree/60f441a22ed98ed2c03f6179adf460d888bf459f/src
