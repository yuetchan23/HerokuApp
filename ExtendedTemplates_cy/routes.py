from flask import Flask, render_template, request
from forms import ContactForm
from flask.ext.mail import Message, Mail

app = Flask(__name__)

app.secret_key = 'WebDesign'

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'umsiwebdesign@gmail.com',
    MAIL_PASSWORD = '105sstate',
))

mail = Mail(app)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", name='index')

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", name='gallery')

@app.route("/about")
def about():
    return render_template("about.html", name='about')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
 #  	msg = Message("Hello From Flask", sender="sleepycactus23@gmail.com", recipients=["yuetchan@umich.edu"])
 #  	mail.send(msg)
 #  	return 'Form posted.'

    msg_0 = Message(form.subject.data, sender=form.email.data, recipients=['yuetchan@umich.edu']) #besure to change this to your own test email
    msg_0.body = """
      From: %s <%s>

            %s
      """ % (form.name.data, form.email.data, form.message.data)
    mail.send(msg_0)

    msg_1 = Message("Comfirmation: Your email to Yue has been sent.", sender="umsiwebdesign@gmail.com", recipients=[form.email.data]) #besure to change this to your own test email
    msg_1.body = """
      From: Yue <yuet@umich.edu>

            Thank you for contacting me:)
      """
    mail.send(msg_1)

    return render_template('contact.html', name='contact', form=form, message="Thank you for sumitting your email")


  elif request.method == 'GET':
    return render_template('contact.html', name='contact', form=form)


@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def pageNotFound(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
  app.run(debug=True)
