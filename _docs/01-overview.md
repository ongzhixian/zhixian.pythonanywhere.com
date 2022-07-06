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


# Running tests

tldr; this is the preferred way to execute

python -m unittest discover tests

Syntax reference (assuming running from `D:\src\github\proj\`)

1.  Run all tests; Not ideal because this will also trigger `flask_app.py`
`python -m unittest discover`
`python -m unittest` (this is same as above)

2.  Run all tests in selected directory; this is the preferred approach
`python -m unittest discover <test_directory>`

3.  Run all tests in selected directory that match specified filename pattern
`python -m unittest discover -s <directory> -p '*_test.py'`

# Notes PythonAnywhere

Latest version of Python supported is 3.7
Latest version of MySql  supported is 5.7.34

# Reference

Github google / material-design-lite 
https://github.com/google/material-design-lite/tree/60f441a22ed98ed2c03f6179adf460d888bf459f/src

https://getmdl.io/components/index.html

https://docs.oracle.com/cd/E19078-01/mysql/mysql-refman-5.0/error-handling.html#error-messages-server