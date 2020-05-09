from flask import Flask, render_template, url_for, request, redirect
from models import *

app = Flask(__name__)

# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'ananbada1234',
#     'db': 'things',
#     'host': 'localhost',
#     'port': '5432',
# }

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mnzmkqtiibjkns:93a26a7d22fb5c2918113f23c8423e1bbff5ec2bfe328e8a6334b5b81c79558c@ec2-52-70-15-120.compute-1.amazonaws.com:5432/d95d2r0uani23p'
db.init_app(app)

# This is for my Personal Website.

@app.route('/')
def index():
    # return beta()
    return todo()

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