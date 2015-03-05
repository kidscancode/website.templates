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


# Seen high stats on analytics.  No idea where it's coming from, but let's catch it!
@app.route("/KidsCanCode-Coding-for-kids/")
def bad_url1():
    return render_template('redir.html', title="Home")


# another one
@app.route("/c/KidscancodeOrg/")
def bad_url2():
    return render_template('redir_yt.html', title="Home")


# another one
@app.route("/channel/UCNaPQ5uLX5iIEHUCLmfAgKg/")
def bad_url3():
    return render_template('redir_yt.html', title="Home")


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
    return render_template('about.html', title="About")


@app.route("/resources.html")
def resources():
    return render_template('resources.html', title="Resources")


@app.route("/store.html")
def store():
    return render_template('store.html', title="Store")


@app.route("/aboutpi.html")
def aboutpi():
    return render_template('aboutpi.html', title="About Raspberry Pi")


@app.route("/signup.html")
def signup():
    return render_template('signup.html', title="Signup")


# @app.route("/sumac/")
# def sumac2():
#     return render_template('sumac.html', title="Signup")


# @app.route("/reed/")
# def reed2():
#     return render_template('reed.html', title="Signup")


# @app.route("/monlux/")
# def monluxsignup():
#     return render_template('monlux.html', title="Signup")


@app.route("/class-terms.html")
def terms():
    return render_template('class-terms.html', title="Terms")


@app.route("/thanks.html")
def thanks():
    return render_template('thanks.html', title="Thanks")


@app.route("/summer/")
def summer():
    return render_template('summer2015.html', title="Summer Camps")


@app.route("/winter2015/")
def fall2014():
    return render_template('winter2015.html', title="After School Programs")


@app.route("/millikan/")
def millikan():
    return render_template('millikan.html', title="Signup")


@app.route("/montevista/")
def montevista():
    return render_template('montevista.html', title="Signup")


@app.route("/vip/")
def vip():
    return render_template('vip.html', title="Signup")


@app.route("/scratch.html")
def scratch():
    return render_template('scratch.html', title="About Scratch")


@app.route("/python-install.html")
def python_install():
    return render_template('python-install.html', title="Installing Python")


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
