from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %>' % self.id

# This is for my Personal Website.

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('todo.html')

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