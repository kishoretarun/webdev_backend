from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://SoCQuBVBp8:sRw0RWEumh@remotemysql.com/SoCQuBVBp8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(300), nullable=True)
    time = db.Column(db.DateTime, default=datetime.now())

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        title1 = request.form['title']
        description1 = request.form['description']
        date_time1 = datetime.now()

        todo = Todo(
            title=title1,
            description=description1,
            time=date_time1
        )
        db.session.add(todo)
        db.session.commit()

        return redirect('/')

    todos1 = Todo.query.all()
    return render_template('index.html',todos=todos1)

@app.route('/delete/<int:sno>')
def delete(sno):
    searched = Todo.query.filter_by(sno=sno).first()
    db.session.delete(searched)
    db.session.commit()

    return redirect('/')

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title2 = request.form['title']
        description2 = request.form['description']

        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title2
        todo.description = description2
        todo.time = datetime.now()

        db.session.add(todo)
        db.session.commit()
        return redirect('/')


    searched = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=searched)

@app.route('/tarun')
def tarun():
    return "I'm tarun"

if __name__=='__main__':
    app.run(debug=True, port=8000)