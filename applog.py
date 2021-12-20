from flask import Flask    
import logging
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world rajesh is here'

if __name__== "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)
