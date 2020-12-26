from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.itu.edu.tr'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '@itu.edu.tr'
app.config['MAIL_PASSWORD'] = '7'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ('Enes U' ,'u@itu.edu.tr')

mail = Mail()
mail.init_app(app)

@app.route('/')
def index():
    msg = Message('Hello From Flask',recipients=['u@gmail.com'],sender=('Enes','@itu.edu.tr'))
    msg.add_recipient('@yahoo.com')
    msg.body = "This is text of the mail"
    msg.html = '<b>Please see attached</b>'
    #How to send attachement with e mail
    with app.open_resource('convolutional_strategy.pdf') as pdf:
        msg.attach('flask.pdf','application/pdf',pdf.read())
    mail.send(msg)

    return '<h1>Sent!</h1>'

if __name__ == '__main__':
	app.run(debug=True)
