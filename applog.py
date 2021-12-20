from flask import Flask    
import logging

log = logging.getLogger(__name__)

def do_something():
    log.debug("Doing something!")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
