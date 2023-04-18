from flask import Flask,render_template
import psycopg2
import psycopg2.extras
from flask_apscheduler import APScheduler


from datetime import datetime,timezone

import pytz



app = Flask(__name__)

sched = APScheduler()  #intializing the apschduler

now = datetime.now(timezone.utc)



# DB_HOST = "localhost"
# DB_NAME = "monitor"
# DB_USER = "postgres"
# DB_PASS = "Password@123"


# conn = psycopg2.connect(dbname=DB_NAME , user=DB_USER , password=DB_PASS , host=DB_HOST) 






# @app.route('/')
# def index():
#     return "hello world"

@app.route('/index')
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM worker"
    cur.execute(s)
    list_hos = cur.fetchall()
    return render_template('index.html',list_hos=list_hos)

@app.route("/sch")
def scheduler():
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # s = "SELECT last_updated FROM worker where id=5"
    # cur.execute(s)
    # list_hos = cur.fetchone()
    target_time =datetime.now(pytz.timezone('Asia/Kolkata'))
    print("updated time:" ,target_time)
    # date = datetime.now()

    current_time = datetime.now(pytz.timezone('Asia/Kolkata'))
    print(current_time)
    difference=current_time-target_time
    
    print("current time:",current_time)
    # print(type(target_time))
    # print(type(date))

    print('difference :',difference)
    
    total_seconds=difference.total_seconds() 
    td_in_minutes = total_seconds / 60 
    print("minutes:",td_in_minutes)
    if td_in_minutes < 20:
        print("completed")
        
        
    else:
        print("processing")