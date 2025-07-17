from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

@app.route("/hello")
def hello_world():
    return "Hello, World!"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'{username}\'s profile'

@app.route('/login')
def login():
    return 'login'


@app.route('/post/<int:post_id>')
def post(post_id):
    return f'Post {post_id}.'

@app.route('/url')
def url():
    return f'''
            <p>{url_for('index')}</p>
            <p>{url_for('login')}</p>
        
            <p>{url_for('user', username='Marco')}</p>
            '''