from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    if(random.randint(0,1)):
        return 'Toads'
    else:
        return 'Froads'
