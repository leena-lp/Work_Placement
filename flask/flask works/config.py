from flask_mail import Mail, Message
from flask import Flask,render_template

app=Flask(__name__)
mail=Mail(app)



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'pythondrf@gmail.com'
app.config['MAIL_PASSWORD'] = "Password@123"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



mail = Mail(app)