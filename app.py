from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return redirect('/')

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

@app.route('/notes')
def blog():
    return render_template('notes.html')


if __name__ == '__main__':
    app.run(debug = True)
