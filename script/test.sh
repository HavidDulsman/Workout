#!/bin/bash

source ~/.bashrc
source venv/bin/activate
python3 -m pytest ./test/test.py
pip3 show coverage
python3 -m coverage run -m pytest test/test.py
python3 -m coverage report -m