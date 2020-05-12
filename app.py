from flask import Flask, render_template, url_for, request, redirect
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hpkzufpyrlpwsl:223744b81464ff97c191afbd8f35565e58a4d47f64db56dba1fee1013f7b3867@ec2-3-231-16-122.compute-1.amazonaws.com:5432/de2o41b7f60dk8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    return beta()
    # return todo()

@app.route('/beta')
def beta():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/todo', methods=['POST', 'GET'])
def todo():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/todo')
        except:
            return "Error."
        
    else:
        tasks = Todo.query.order_by(Todo.date).all()
        return render_template('todo.html', tasks=tasks)

@app.route('/todo/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/todo')
    except:
        return "Error."

@app.route('/todo/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/todo')
        except:
            return "Error."
    else:
        return render_template('update.html', task=task)

if __name__ == '__main__':
    app.run(debug = True)