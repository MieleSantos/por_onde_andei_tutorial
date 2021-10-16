from flask import Flask, render_template, redirect, url_for
from utils.maps import create_map

app = Flask(__name__)


@app.get('/')
def home():

    return render_template("index.html")


@app.get('/oops')
def oops():
    return render_template('oops.html')


@app.get('/ping')
def update_map():
    created = create_map()
    if created:
        return render_template("index.html")

    return redirect(url_for("oops"))
