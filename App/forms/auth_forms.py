from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo,Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username is required.')])
    password = PasswordField('Password', validators=[DataRequired(message='Password is required.')])
    submit = SubmitField('Login')
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username is required.')])
    email = StringField('Email', validators=[DataRequired(message="Email is required"), Email(message='Invalid email.')])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required."),Length(min=6, message='Password must be at least 6 characters long')])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message="This field is required"), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')