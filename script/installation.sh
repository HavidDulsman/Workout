#!/bin/bash
source venv/bin/activate
pip3 install pytest

pip3 install urllib3

pip3 isntall coverage

pip3 install flask

pip3 install flask_mysqldb

source ~/.bashrc

python3 /var/lib/jenkins/workspace/flaskapps/flaskprojects/app.py
