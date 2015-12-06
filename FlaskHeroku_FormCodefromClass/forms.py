from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField

class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")
# Represents an <input type="submit">. This allows checking if a given submit button has been pressed.
