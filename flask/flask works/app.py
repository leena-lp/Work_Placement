from flask import Flask,render_template
import psycopg2
import psycopg2.extras
from flask_apscheduler import APScheduler


from datetime import datetime,timezone

import pytz



app = Flask(__name__)
app.app_context().push()

sched = APScheduler()  #intializing the apschduler

now = datetime.now(timezone.utc)



DB_HOST = "localhost"
DB_NAME = "monitor"
DB_USER = "postgres"
DB_PASS = "Password@123"


conn = psycopg2.connect(dbname=DB_NAME , user=DB_USER , password=DB_PASS , host=DB_HOST) 






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
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT last_updated FROM worker where id=6"
    cur.execute(s)
    list_hos = cur.fetchone()
    target_time = list_hos[0]
    print("updated time:" ,target_time)
    # date = datetime.now()

    current_time = datetime.now(pytz.timezone('Asia/Kolkata'))

    difference=current_time-target_time
    
    print("current time:",current_time)
    # print(type(target_time))
    # print(type(date))

    print('difference :',difference)
    
    total_seconds=difference.total_seconds() 
    td_in_minutes = total_seconds / 60 
    print("minutes:",td_in_minutes)
    if td_in_minutes > 18:
        print("completed")
        with app.app_context():
            sent_mail()
        
    else:
        with app.app_context():
            sent_mailproces()
        print("processing")


    # print("processing")


# ===============================================

from flask import Flask
from flask_mail import Mail, Message

mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'pythondrf@gmail.com'
app.config['MAIL_PASSWORD'] = "ybtkiraqstrslvvg"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/email")
def sent_mail():
    msg = Message('Hello', sender = 'pythondrf@gmail.com', recipients = ['shinas@yopmail.com'])
    msg.body = "completed successfully done"
    mail.send(msg)
    return "Mail has sent"


def sent_mailproces():
    msg = Message('Hello', sender = 'pythondrf@gmail.com', recipients = ['shinas@yopmail.com'])
    msg.body = "processing"
    mail.send(msg)
    return "Mail has sent"


# ================================================

if __name__ == "__main__":

    sched.add_job(id="scheduler",func=scheduler, trigger = 'interval' , seconds = 10) #we add to the scheduler
    sched.start()
    
    app.run(debug=True, use_reloader = False)