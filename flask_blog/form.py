from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , BooleanField
from wtforms.validators import DataRequired ,Length ,Email , EqualTo , ValidationError
from flask_blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=2,max =20)])
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password =  PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField ('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken Please Take Another One.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken Please Take Another One.')


class LoginForm(FlaskForm):
    # username = StringField('username', validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Rembember Me")
    submit = SubmitField('Login')
