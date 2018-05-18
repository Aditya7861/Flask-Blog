from flask import Flask , render_template , url_for ,flash , redirect
from form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '33e691769378c0ad911e5a951faccdf8'
posts = [
    {
    'author': "Aditya Singh",
    'title': "First Blog Post",
    'content': 'First Blog Post Content'
},
{
    'author': "Pradeep Gupta",
    'title': "First Pradeep Post",
    'content': 'First Pradeep Content'
}
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)



@app.route("/about")
def about():
    return render_template('about.html',title = "About")


@app.route("/registration",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!',"success")
        return redirect(url_for('home'))
    return render_template('register.html',title='register', form = form)


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)