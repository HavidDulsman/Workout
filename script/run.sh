#!/bin/bash
sudo cp /var/lib/jenkins/workspace/workout-pipline/script/flask.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable flask.service
sudo systemctl start flask.service
