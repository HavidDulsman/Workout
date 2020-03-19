#!/bin/bash

source venv/bin/activate

pip3 install pytest
pip3 install urllib3
pip3 install coverage
pip3 install flask
pip3 install flask_mysqldb
pip3 install flask-bootstrap

source ~/.bashrc

python3 -m pip install coverage

python3 /var/lib/jenkins/workspace/workout-pipeline/app.py
