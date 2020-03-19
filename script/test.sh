#!/bin/bash

source ~/.bashrc
source venv/bin/activate
python3 -m pytest ./test/test.py
# pip3 show coverage
coverage run -m pytest ./test/test.py
coverage report 