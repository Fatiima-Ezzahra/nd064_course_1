from flask import json
from flask import Flask
import logging
import time
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("%s, / endpoint was reached" % time.time())
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(response=json.dumps({"result": "OK - healthy"}), status=200, mimetype="application/json")
    app.logger.info("%s, /status endpoint was reached" % time.time())
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(response=json.dumps({"status": "success", "code":0, "data":{"UserCount": 140, "UserCountActive": 23}}), status=200, mimetype="application/json")
    app.logger.info("%s, /metrics endpoint was reached" % time.time())
    return response

if __name__ == "__main__":
    logging.basicConfig(filename="app.log", level=logging.DEBUG)
    app.run(host='0.0.0.0')
