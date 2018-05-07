from flask import Flask , render_template
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)