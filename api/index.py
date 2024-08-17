from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!, Feliz por aprender cada vez este framework maravilhoso ;)'

@app.route('/about')
def about():
    return 'About'
