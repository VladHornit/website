from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/hello", methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")


if __name__ == "__main__":
     app.run()


'''3 from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")
def index():
    greet = request.args.get('greet', 'Hello')
    name = request.args.get('name', 'Nobody')

    if name:
        greeting = f"{greet}, {name}"
    else:
        greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
     app.run()
'''






'''1 from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "World"
    return 'Hello, {} {}!'.format(greeting, 23)

@app.route('/test')
def hello_test():
    return 'Hello, vlad'

if __name__ == "__main__":
    app.run()
'''


'''2 from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")

def index():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)


@app.route("/test")

def index_test():
    greeting = "VLAD"
    return render_template("index.html", greeting=greeting)


if __name__ == "__main__":
     app.run()
'''
