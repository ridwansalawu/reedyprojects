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


class SearchAsset(FlaskForm):
    asset = StringField("Asset ID", validators=[DataRequired("please enter a valid asset ID"), Length(min=6, message="invalid asset code")])
    submit = SubmitField("Search")

# class TimeSheet(FlaskForm):
 
#     date = DateField("Date")
#     medium_pit = IntegerField("Medium Pit")
#     large_pit = IntegerField("Large Pit")
#     custom = IntegerField("Custom")
#     daily = IntegerField("Value")
  



# class AddressForm(FlaskForm):
#   address = StringField('Address', validators=[DataRequired("Please enter an address.")])
#   submit = SubmitField("Search")