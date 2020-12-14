from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

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
