from flask import Flask

from logging.config import fileConfig

app = Flask(__name__)

fileConfig('logging.cfg')

@app.route('/')
def hello_world():
    app.logger.info('Processing default request')
    return 'Rajesh Here'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
