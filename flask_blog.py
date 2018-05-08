from flask import Flask , render_template , url_for
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
def hello():
    return render_template('home.html',posts=posts)



@app.route("/about")
def about():
    return render_template('about.html',title = "About")


@app.route("/registration")
def register():
    form = RegistrationForm()
    return render_template('register.html',title='register', form = form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


if __name__ == "__main__":
    app.run(debug=True)