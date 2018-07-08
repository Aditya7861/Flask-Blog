from flask_wtf import FlaskForm
from flask_wtf.file import FileField ,FileAllowed
from flask_login import current_user
from wtforms import StringField , PasswordField , SubmitField , BooleanField , TextAreaField
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


class UpdateAccountForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken Please Take Another One.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is taken Please Take Another One.')


class PostForm(FlaskForm):
    title =  StringField('Title',validators=[DataRequired()])
    content = TextAreaField("Content",validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit =SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is No Account with This E-mail.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password =  PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(" Reset Password")
