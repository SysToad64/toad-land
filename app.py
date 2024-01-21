from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/')
def hello_world():
    if(randint()):
        return 'Toads'
    else:
        return 'Frogs'
