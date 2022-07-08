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

## Setup Kibana/Elasticsearch on Kubernetes (Minikube)

(Work-in-progress)

To run Kibana, we need Elasticsearch image as well.

`minikube image load elasticsearch:8.3.1`
`minikube image load kibana:8.3.1`

Running Elasticsearch
Example: docker run -d --name elasticsearch --net somenetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:tag

Run as standalone
minikube kubectl -- run my-elasticsearch --image=elasticsearch:8.3.1 --port=9200 --port=9300 -it --rm --env="discovery.type=single-node"

After Elasticsearch startup, it will display the following chunk.
We need the enrollment token (starts with ey*** ) in paragraph 4 to configure Kibana

```txt
---------------------------------------------------------
-> Elasticsearch security features have been automatically configured!
-> Authentication is enabled and cluster connections are encrypted.

->  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  lnlp8t9DQ_UA+F39VZGx

->  HTTP CA certificate SHA-256 fingerprint:
  56e4909d76ee73bcff91444f689d6a46dcc5eaa14882398d6d9e3bdcc41ba741

->  Configure Kibana to use this cluster:
* Run Kibana and click the configuration link in the terminal when Kibana starts.
* Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjMuMSIsImFkciI6WyIxNzIuMTcuMC42OjkyMDAiXSwiZmdyIjoiNTZlNDkwOWQ3NmVlNzNiY2ZmOTE0NDRmNjg5ZDZhNDZkY2M1ZWFhMTQ4ODIzOThkNmQ5ZTNiZGNjNDFiYTc0MSIsImtleSI6IkFDaEQwb0VCd2R5VVAtZHpEVlc0OnVsZ2ZDN1VuUkRDTkN0THNsV3QtTHcifQ==

-> Configure other nodes to join this cluster:
* Copy the following enrollment token and start new Elasticsearch nodes with `bin/elasticsearch --enrollment-token <token>` (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjMuMSIsImFkciI6WyIxNzIuMTcuMC42OjkyMDAiXSwiZmdyIjoiNTZlNDkwOWQ3NmVlNzNiY2ZmOTE0NDRmNjg5ZDZhNDZkY2M1ZWFhMTQ4ODIzOThkNmQ5ZTNiZGNjNDFiYTc0MSIsImtleSI6IkFpaEQwb0VCd2R5VVAtZHpEVlhtOjE2V1E5cGVPUVIyV0ctNFVDYjhEUXcifQ==

  If you're running in Docker, copy the enrollment token and run:
  `docker run -e "ENROLLMENT_TOKEN=<token>" docker.elastic.co/elasticsearch/elasticsearch:8.3.1`
---------------------------------------------------------
```


Note: Default username for Kibana is `elastic`. Password is as above.


```cmd: Not working: Attempt to get Elasticsearch running on deployment
minikube kubectl -- create deployment elasticsearch-minikube --image=elasticsearch:8.3.1 --port=9200 --port=9300
minikube kubectl -- set env deployment/elasticsearch-minikube "discovery.type=single-node"
minikube kubectl -- expose deployment elasticsearch-minikube --type=NodePort --port=9200
```


Example: docker run -d --name kibana --net somenetwork -p 5601:5601 kibana:tag

minikube kubectl -- create deployment kibana-minikube --image=kibana:8.3.1
minikube kubectl -- expose deployment kibana-minikube --type=NodePort --port=5601

After Kibana startup, you need to go to the Kibana website.
On the first time you open the website, it will prompt you for Elasticsearch enrollment token.

|-------------|-----------------|--------------|-----------------------------|
|  NAMESPACE  |      NAME       | TARGET PORT  |             URL             |
|-------------|-----------------|--------------|-----------------------------|
| default     | kibana-minikube |         5601 | http://172.17.124.205:32499 |
|-------------|-----------------|--------------|-----------------------------|

After you paste the enrollment token, it will prompt for a Kibana verification code.
To get this code, you need to open a shell session on the Kibana pod to retrieve it as follow:


Aside: Open a shell in pod

minikube kubectl -- exec <pod-id> -it -- /bin/bash
minikube kubectl -- exec <pod-id> --stdin --tty -- /bin/bash

Then run:

`bin/kibana-verification-code`


# Running tests

tldr; this is the preferred way to execute

`python -m unittest discover tests`

Syntax reference (assuming running from `D:\src\github\proj\`)

1.  Run all tests; Not ideal because this will also trigger `flask_app.py`
`python -m unittest discover`
`python -m unittest` (this is same as above)

2.  Run all tests in selected directory; this is the preferred approach
`python -m unittest discover <test_directory>`

3.  Run all tests in selected directory that match specified filename pattern
`python -m unittest discover -s <directory> -p '*_test.py'`

## Running coverage

Use this to discover uncovered files.

`coverage run --source="./forum_app,tests" -m unittest discover tests`

Use this to only calculate coverage for tested files.

`coverage run -m unittest discover tests `

Then use one of the following to generate a report.

 `coverage report`
-- OR --
`coverage html`

# Notes PythonAnywhere

Latest version of Python supported is 3.7
Latest version of MySql  supported is 5.7.34

# Reference

Github google / material-design-lite 
https://github.com/google/material-design-lite/tree/60f441a22ed98ed2c03f6179adf460d888bf459f/src

https://getmdl.io/components/index.html

https://docs.oracle.com/cd/E19078-01/mysql/mysql-refman-5.0/error-handling.html#error-messages-server