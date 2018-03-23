from flask_wtf import Form
from wtforms import TextField, SubmitField, TextAreaField
from wtforms.validators import Length, Email, Required

# Form ORM
class QuizForm(Form):
        essay_question = TextAreaField('Who do you think won the console wars of 1991, Sega Genesis or Super Nintendo? (2048 characters)', validators=[Required(),Length(max=2047)] )
        email_addr = TextField('Enter Your Email', validators=[Required(), Email()])
        submit = SubmitField('Submit')
