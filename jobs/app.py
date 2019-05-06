import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
# an additional route decorator, so jobs can be reached through '/' and '/jobs'.
def jobs():
    return render_template('index.html')
