from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[
        DataRequired(message='Username is required!'),
        Length(
            min=5,
            max=8, 
            message='Username must be bewteen 5-8 characters long!')])

    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required!'),
        Length(
            min=6,
            message='Password must be atleast 6 characters!')])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign In')
