from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://drive.google.com/file/d/1aURG6o-SkLhuz0CLBdQGRtD37HSqsmuB/view?usp=sharing")
    # return render_template('index.html')


@app.route('/transcript')
def transcript():
    return redirect("https://drive.google.com/file/d/1w0Vke7WA5_LV6SVrq2STEg3X_TT_VUbB/view?usp=sharing")

# TEMPORARY, until google links the correct page when you search up my name.
@app.route('/courses')
def courses():
    return transcript()
    # return render_template('courses.html')
    
@app.route('/jellyfin')
def jellyfin():
    return redirect("http://win.anandabadari.com/")

@app.route('/aboutme')
def about():
    return index()
    # return render_template('about.html')

@app.route('/resume')
def resume():
    return index()
    # return render_template('resume.html')
    
@app.route('/projects')
def projects():
    return index()
    # return render_template('projects.html')

# Projects.
@app.route('/dashcam')
def cv():
    return render_template('dashcam.html')

@app.route('/dashcamproposal')
def cvprop():
    return render_template('dashcamproposal.html')

@app.route('/dashcammidterm')
def cvmid():
    return render_template('dashcammidterm.html')

@app.route('/dashcamfinal')
def cvfin():
    return render_template('dashcamfinal.html')

@app.route('/stock')
def ml():
    return render_template('stock.html')

@app.route('/stockprop')
def mlprop():
    return render_template('stockprop.html')

@app.route('/stockmidterm')
def mlmid():
    return render_template('stockmidterm.html')

@app.route('/stockfinal')
def mlfin():
    return render_template('stockfinal.html')

@app.errorhandler(404)
def page_not_found(e):
    return index()
    # return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug = False)
    # app.run(host = "0.0.0.0", debug = True)
