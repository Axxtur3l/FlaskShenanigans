from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)

connection = pymysql.connect(
    host='10.100.33.60',
    user='agrenardo',
    password='220279616',
    database='agrenardo_todo',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True 
)

todolist = ["have at least 5k in my account","upgrade my computer once more"]

@app.route('/')
def index():
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `Todos`')

    results=cursor.fetchall()
    
    return render_template(
        'todo.html.jinja', 
        todos = results
    )

if __name__ == '__main__':
    app.run()

@app.route("/add", methods = ['POST'])
def add():
   new_todo = request.form['new_todo']
   return new_todo