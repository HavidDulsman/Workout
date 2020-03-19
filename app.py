from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
import os
import var

variable = var

app = Flask(__name__)

#MySQL Config
app.config['MYSQL_HOST'] = os.environ['MYSQLHOST']
app.config['MYSQL_USER'] = os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQLDB']

mysql = MySQL(app)
#############################################################################################################################################################################################
# ---------------------------------------------------------- Homepage route + Functions -----------------------------------------------------------------------------------------------------
#############################################################################################################################################################################################

@app.route('/')
@app.route('/home')

def nav_home():
    return render_template("home.html")


#############################################################################################################################################################################################
#---------------------------------------------------------- Routines: Create & View ----------------------------------------------------------------------------------------------------------
#############################################################################################################################################################################################

#Read: shows available workouts
@app.route("/routine", methods =['GET', 'POST'])
def view_routine():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM workout")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close() 
    if len(rows) == 0:
        print("no info")
    else:
        pass

    info =[]
    for row in rows:
        info.append(row)
    if request.method == "POST":
        details=request.form
        variable.workout=details['workout']
        variable.workout_id=details['workout']
        return redirect("/workoutpage")
    return render_template("routine.html", info1 =info, workout=variable.workout, workout_id=variable.workout_id)


#Create: Create a new blank workout
@app.route('/newroutine',  methods =['GET', 'POST'])
def create_new_workout():

    info =[]

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM workout")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close() 
    if len(rows) == 0:
        print("no info")
    else:
        pass

    for row in rows:
        info.append(row)

    if request.method == "POST":
        details = request.form
        wName = details['wName']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO workout (name_workout) VALUES (%s)", [wName])
        mysql.connection.commit()
        cur.close()
        return render_template('routine.html', info1=info)
   
    return render_template('newroutine.html', info1=info)

#############################################################################################################################################################################################
#--------------------------------------------------------------------- Actions: Create, Read & Delete ---------------------------------------------------------------------------------------
#############################################################################################################################################################################################

#Read: View pre made actions
@app.route('/action', methods =['GET', 'POST'])
def view_action():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Action")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close() 
    if len(rows) == 0:
        print("no info")
    else:
        pass

    info =[]

    for row in rows:
        info.append(row) 
    
    return render_template("action.html", info1=info)

#Create: Create a new workout
@app.route('/action/add', methods =['GET', 'POST'])
def new_action():
    if request.method == "POST":
        details = request.form
        actionName = details['aName']
        catChoice = details['catChoice']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Action (name_action,id_category) VALUES (%s, %s)", (actionName, catChoice))
        mysql.connection.commit()
        cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Action")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close() 
    if len(rows) == 0:
        print("no info")
    else:
        pass

    info =[]

    for row in rows:
        info.append(row)
    
    return render_template("action.html", info1=info)

#Delete: Deletes records from the action table AND traces of that action inside other workout routines
@app.route('/action/delete', methods =['GET', 'POST'])
def delete_action():
    if request.method == "POST":
        details = request.form
        dName = details['dName']
        cur = mysql.connection.cursor()
        cur.execute("SELECT id_action FROM Action WHERE name_action = (%s)", [dName])
        mysql.connection.commit()
        actionID = cur.fetchall()
        print(actionID)
        cur.execute("DELETE FROM workout_action WHERE id_action = (%s)", [actionID])
        cur.execute("DELETE FROM Action WHERE name_action = (%s)",[dName])
        mysql.connection.commit()
        cur.close()
        
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Action")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close() 
    if len(rows) == 0:
        print("no info")
    else:
        pass

    info =[]

    for row in rows:
        info.append(row)

    return render_template("action.html", info1 = info)

#############################################################################################################################################################################################
#------------------------------------------------------------- Workout Page: Create, Read, Update & Delete ----------------------------------------------------------------------------------
#############################################################################################################################################################################################

#Read: Pulls related records from Many-to-Many junction table 'workout_action'
@app.route('/workoutpage', methods =['GET', 'POST'])
def get_workout_actions():
    cur = mysql.connection.cursor()
    wo = variable.workout
    cur.execute("SELECT Action.name_action FROM Action INNER JOIN workout_action ON Action.id_action = workout_action.id_action WHERE workout_action.id_workout = (%s);", [wo])
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    workout_info = []
    for row in rows:
        workout_info.append(str(row)[2:-3])

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Action")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    info = []
    for row in rows:
        info.append(row)
    print(info)    
    
#Create: Inserts New records into Many-to-Many junction table 'workout_action'
    if request.method == "POST":
        details=request.form
        actChoice = details['actionChoice']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO workout_action (id_workout, id_action) VALUES (%s, %s)", (variable.workout, actChoice))
        mysql.connection.commit()
        cur.close()
        
        return redirect (url_for('get_workout_actions'))    
    return render_template("workoutpage.html", workout_info1=workout_info, workout = variable.workout, workout_id=variable.workout_id,info1=info)

#Delete: Removes records from a workout
@app.route('/workoutpage/delete/action', methods =['GET', 'POST'])
def delete_action_from_workout():
    cur = mysql.connection.cursor()
    wo = variable.workout
    cur.execute("SELECT Action.name_action FROM Action INNER JOIN workout_action ON Action.id_action = workout_action.id_action WHERE workout_action.id_workout = (%s);", [wo])
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    workout_info = []
    for row in rows:
        workout_info.append(str(row)[2:-3])

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Action")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    info = []
    for row in rows:
        info.append(row)

    if request.method == "POST":
        details = request.form
        dAName = details['dAName']
        cur = mysql.connection.cursor()
        cur.execute("SELECT id_action FROM Action WHERE name_action = (%s)",  [dAName])
        deletedActionID = cur.fetchall()
        print(deletedActionID)
        deletedActionID = deletedActionID[2::-3]
        cur.execute("DELETE FROM workout_action WHERE id_action = (%s) AND id_workout = (%s)",  (deletedActionID, variable.workout))
        mysql.connection.commit()
        cur.close()

        return redirect (url_for('delete_action_from_workout'))
    return render_template("workoutpage.html", workout_info1=workout_info, workout = variable.workout, workout_id=variable.workout_id,info1=info)

#Update: Update the name of the record you are on
@app.route('/routine/update', methods = ['GET', 'POST'])
def edit_workout_name():
    cur = mysql.connection.cursor()
    wo = variable.workout
    print(wo)
    cur.execute("SELECT Action.name_action FROM Action INNER JOIN workout_action ON Action.id_action = workout_action.id_action WHERE workout_action.id_workout = (%s);", [wo])
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    workout_info = []
    for row in rows:
        workout_info.append(str(row)[2:-3])

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Action")
    mysql.connection.commit()
    rows = cur.fetchall() 
    cur.close()
    info = []
    for row in rows:
        info.append(row) 

    if request.method == "POST":
        details = request.form
        cur = mysql.connection.cursor()
        wo = variable.workout
        cur.execute("SELECT name_workout FROM workout WHERE id_workout = (%s)", [wo])
        mysql.connection.commit()
        row = cur.fetchall()
        print(row)
        print("Look Above!")
        cur.close()
        oldName = ""
        oldName=(str(row)[3:-5])
        newName = details['newName']
        print(newName)
        print(oldName)
        if newName != oldName:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE workout SET name_workout = (%s) WHERE name_workout = (%s)", (newName, oldName))
            mysql.connection.commit()
            cur.close()
        return redirect (url_for('edit_workout_name'))
    return render_template("workoutpage.html", workout_info1=workout_info, workout = variable.workout, workout_id=variable.workout_id,info1=info)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)