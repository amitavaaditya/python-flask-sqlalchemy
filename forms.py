from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignUpForm(Form):
    first_name = StringField('First Name', validators=[DataRequired('Please enter your First Name')])
    email = StringField('Email', validators=[DataRequired('Please enter your Email'), Email('Please enter a valid email'
                                                                                            ' address')])
    last_name = StringField('Last Name', validators=[DataRequired('Please enter your Last Name')])
    password = PasswordField('Password', validators=[DataRequired('Please enter your Password'),
                                                     Length(min=8, max=20, message='Password length must be between 8 '
                                                                                   'and 20 characters')])
    submit = SubmitField('Sign up')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired('Please enter your email'),
                                             Email('Please enter a valid email address')])
    password = PasswordField('Password', validators=[DataRequired('Please enter your password')])
    submit = SubmitField('Sign in')
