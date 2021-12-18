from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello_world():
    app.logger.info('Processing default request')
    return 'Hello Rajesh Here'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
