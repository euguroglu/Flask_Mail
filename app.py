from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'xxxx.smtp.gmal.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'xxx@xmail.com'
app.config['MAIL_PASSWORD'] = 'xxxxxxxxx'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'xxx@xmail.com'

mail = Mail()
mail.init_app(app)

@app.route('/')
def index():
    msg = Message('Hello From Flask',recipients=['enes@gmail.com'])
    mail.send(msg)

    return '<h1>Sent!</h1>'

if __name__ == '__main__':
	app.run(debug=True)
