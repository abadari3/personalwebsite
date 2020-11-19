from flask import Flask, render_template, url_for, request, redirect
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hpkzufpyrlpwsl:223744b81464ff97c191afbd8f35565e58a4d47f64db56dba1fee1013f7b3867@ec2-3-231-16-122.compute-1.amazonaws.com:5432/de2o41b7f60dk8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# test test

@app.route('/')
def index():
    # return todo()
    return redirect("https://www.linkedin.com/in/anandabadari/")
    # return render_template('index.html')

@app.route('/home')
def home():
    # return todo()
    return render_template('index.html')

@app.route('/cvproject')
def cvproject():
    # return todo()
    return render_template('cvindex.html')

@app.route('/cvproposal')
def cvprop():
    # return todo()
    return render_template('cvprop.html')

@app.route('/cvmidterm')
def cvmidterm():
    # return todo()
    return render_template('cvmidterm.html')


if __name__ == '__main__':
    app.run(debug = True)