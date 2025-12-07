print("Welcome to my website")
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my website!</h1><p>This site is made with Python!</p>"

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is a simple website built with Flask.</p>"

