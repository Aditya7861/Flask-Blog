from flask import render_template, url_for, flash, redirect
from flask_blog.form import RegistrationForm, LoginForm
from flask_blog import app , db ,bcrypt
from flask_blog.models import User,Post
from flask_login import login_user ,current_user,logout_user
posts = [{
    'author': "Aditya Singh",
    'title': "First Blog Post",
    'content': 'First Blog Post Content'
}, {
    'author': "Pradeep Gupta",
    'title': "First Pradeep Post",
    'content': 'First Pradeep Content'
}]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/registration", methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email = form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Account Has Been Created ! Now You will be able to Create Post','success')
        flash(f'Account Created for {form.username.data}!', "success")
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password','danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/log_out")
def log_out():
    logout_user()
    redirect(url_for('home'))
