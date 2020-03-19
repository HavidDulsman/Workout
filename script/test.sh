#!/bin/bash

source ~/.bashrc
source /var/lib/jenkins/workspace/workout-pipeline/venv/bin/activate
pytest ./test/test.py
# pip3 show coverage
coverage run -m pytest ./test/test.py
coverage report 