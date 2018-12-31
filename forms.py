from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField("First name", validators= [DataRequired("please enter your first name")])
    last_name = StringField("Last name", validators= [DataRequired("please enter your last name")])
    email = StringField("Email", validators= [DataRequired("please enter your email"), Email("hey! enter a valid email")])
    password = PasswordField("Password", validators= [DataRequired(), Length(min=6, message="Chairman, your password must be at least 6 characters")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Hey! a valid email please!!")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

# class AddressForm(FlaskForm):
#   address = StringField('Address', validators=[DataRequired("Please enter an address.")])
#   submit = SubmitField("Search")