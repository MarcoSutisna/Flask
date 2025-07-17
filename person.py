from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
    person={
        'name' : 'Marco',
        'age' : 27,
        'city' : 'Bandung'
    }
    return "Hello from "+ person['city']