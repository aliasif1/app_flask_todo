from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

# Set up the db model 
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    todo = db.Column(db.String(100))
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"Todo: {self.todo}, created At: {self.createdAt} "


@app.route('/home/')
def home():
    todos = Todo.query.all()
    return render_template('home.html', todos = todos)

@app.route('/addTodo', methods=['GET','POST'])
def addTodo():
    todo = ''
    if(request.method == 'POST'):
        todo = request.form['todo']
    else:
        todo = request.args['todo']
    newTodo = Todo(todo = todo)
    db.session.add(newTodo)
    db.session.commit()
    return redirect('/home')

@app.route('/deleteTodo/<int:id>', methods=['GET'])
def deleteTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/home')

@app.route('/showUpdateTodo/<int:id>/<value>', methods=['GET'])
def showUpdateTodo(id, value):
    return render_template('/update.html', id=id, value=value)

@app.route('/updateTodo', methods=['POST'])
def updateTodo():
    print(request.form)
    updatedTodo = request.form['todo']
    id = request.form['id']
    todo = Todo.query.filter_by(id=id).first()
    todo.todo = updatedTodo
    db.session.commit()
    return redirect('/home')

if __name__ == "__main__":
    app.run(debug=True)