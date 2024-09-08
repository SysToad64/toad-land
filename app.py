from flask import Flask
import random
import os
app = Flask(__name__)

@app.route('/rand')
def hello_world():
    if(random.randint(0,1)):
        return 'Toads'
    else:
        return 'Froads'
@app.route('/serverpack_download')
def server_pack():
    with open("./server_pack.zip", "r") as f:
        data = f.read(os.path.getsize("./server_pack.zip"))
    return data
