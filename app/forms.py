from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    remember_me = BooleanField('remember_me', default=False)
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])

class NewMetricForm(Form):
    name = StringField('name', validators=[DataRequired()])
    is_bool = BooleanField('Yes/No', default=False)
    max_val = IntegerField('max_val', default=1)
    min_val = IntegerField('min_val', default=0)
    increment = IntegerField('increment', default=1)
