import pytest
import urllib3
from flask import Flask, render_template, request
import os
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']

mysql = MySQL(app)
#############################################################################################################################################################################################
#---------------------------------------------------------- Test of URL links for each route for the app -----------------------------------------------------------------------------------
#############################################################################################################################################################################################

def test_homepage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.34.11:5000/')
    assert 200 == r.status

def test_homepage2():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.34.11:5000/home')
    assert 200 == r.status

def test_action():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.34.11:5000/action')
    assert 200 == r.status

def test_action_add():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.34.11:5000/action/add')
    assert 200 == r.status

def test_action_delete():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.34.11:5000/action/delete')
    assert 200 == r.status

def test_routine():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.34.11:5000/routine')
    assert 200 == r.status

def test_newroutine():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.34.11:5000/newroutine')
    assert 200 == r.status

def test_workoutpage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.34.11:5000/workoutpage')
    assert 200 == r.status

def test_update_routine_name():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.34.11:5000/routine/update')
    assert 200 == r.status

#############################################################################################################################################################################################
#---------------------------------------------------------- Databaswe Tests of the various functions of the app -----------------------------------------------------------------------------
#############################################################################################################################################################################################



def test_read_routine():
    with app.app_context():
        cur = mysql.connection.cursor()
        numRoutines = cur.execute("SELECT * FROM workout;")
        mysql.connection.commit()
        cur.close()
        assert 7 == numRoutines

def test_create_routine():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO workout(id_workout, name_workout) VALUES (50, 'Summer gains');")
        mysql.connection.commit()
        numWorkouts = cur.execute("SELECT * FROM workout")
        mysql.connection.commit()
        cur.close()
        assert 8 == numWorkouts

def test_update_workout():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE workout SET name_workout = 'Getting ready for Ibiza' WHERE workout_id = '50';")
        mysql.connection.commit()
        numWorkouts = cur.execute("SELECT * FROM workout;")
        mysql.connection.commit()
        cur.close()
        assert 8 == numWorkouts

def test_delete_action():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM workout WHERE id_workout = 50;")
        mysql.connection.commit()
        numWorkouts = cur.execute("SELECT * FROM workout;")
        mysql.connection.commit()
        cur.close()
        assert 7 == numWorkouts
    