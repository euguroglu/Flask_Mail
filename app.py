from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smpt.itu.edu.tr'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '@itu.edu.tr'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = '@itu.edu.tr'

mail = Mail()
mail.init_app(app)

@app.route('/')
def index():
    msg = Message('Hello From Flask',recipients=['@gmail.com'])
    msg.add_recipient('@yahoo.com')
    msg.body = "This is text of the mail"
    msg.html = '<b>This is a html message</b>'
    mail.send(msg)

    return '<h1>Sent!</h1>'

if __name__ == '__main__':
	app.run(debug=True)
