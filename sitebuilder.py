import sys

from flask import Flask, render_template, request
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)


@app.route("/")
def index():
    return render_template('index.html', title="Home")


@app.route("/contact.html")
def contact():
    return render_template('contact.html', title="Contact")


@app.route("/whycode.html")
def whycode():
    return render_template('whycode.html', title="Why Code")


@app.route("/classes.html")
def classes():
    return render_template('classes.html', title="Classes")


@app.route("/about.html")
def about():
    return render_template('about.html', title="Classes")


@app.route("/resources.html")
def resources():
    return render_template('resources.html', title="Resources")


@app.route('/font/<path:filename>')
@app.route('/img/<path:filename>')
def static_root(filename):
    f = open(request.path[1:])
    return f.read()


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=5001)
