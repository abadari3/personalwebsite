from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')
    
@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/dashcam')
def cv():
    return render_template('dashcam.html')

@app.route('/projects/dashcamproposal')
def cvprop():
    return render_template('dashcamproposal.html')

@app.route('/projects/dashcammidterm')
def cvmid():
    return render_template('dashcammidterm.html')

@app.route('/projects/dashcamfinal')
def cvfin():
    return render_template('dashcamfinal.html')

@app.route('/projects/stock')
def ml():
    return render_template('stock.html')

@app.route('/projects/stockprop')
def mlprop():
    return render_template('stockprop.html')

@app.route('/projects/stockmidterm')
def mlmid():
    return render_template('stockmidterm.html')

@app.route('/projects/stockfinal')
def mlfin():
    return render_template('stockfinal.html')

# TEMPORARY, until google links the correct page when you search up my name.
@app.route('/home')
def home():
    return redirect('/')

@app.route('/beta')
def beta():
    return redirect('/')

@app.route('/projects/stockpredict')
def remove():
    return redirect('/projects/stock')

if __name__ == '__main__':
    app.run(debug = True)
