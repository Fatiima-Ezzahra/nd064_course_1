from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    return {"result": "OK - healthy"}

@app.route("/metrics")
def metrics():
    data = {"UserCount": 140, "UserCountActive": 23}
    return {"data": data}

if __name__ == "__main__":
    app.run(host='0.0.0.0')
