from flask import Flask, render_template
from flask import session, redirect, url_for, escape, request, jsonify
import json
import requests
from firebase import firebase

app = Flask(__name__)

FIREBASE_URL = 'https://springboardcourses-c48ca.firebaseio.com'
HACKEREATH_URL = 'http://hackerearth.0x10.info/api/learning-paths?type=json&query=list_paths'

@app.route("/")
def home():
    fire = firebase.FirebaseApplication(FIREBASE_URL, None)
    response = fire.get('/paths', None)
    kwargs = locals()

    return render_template('home.html', **kwargs)


@app.route("/filter", methods=["POST"])
def filter():
    print "r", request.form
    category = request.form['type']
    fire = firebase.FirebaseApplication(FIREBASE_URL, None)
    response = fire.get('/paths', None)
    kwargs = locals()

    return redirect(url_for("home"))


if __name__ == '__main__':
	app.run(port=8000, debug=True)
