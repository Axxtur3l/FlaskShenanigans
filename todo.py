from flask import Flask, render_template, request

app = Flask(__name__)

todolist = ["have at least 5k in my account","upgrade my computer once more"]

@app.route('/')
def index():
    return render_template(
        'todo.html.jinja', 
        todo = todolist)

if __name__ == '__main__':
    app.run()

@app.route("/add", methods = ['POST'])
def add():
   new_todo = request.form['new_todo']
   return new_todo