from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello nanobox!"

if __name__ == "__main__":

    # nanobox configuration; most apps bind to localhost by default, however we
    # need to allow connections from the host into the container
    app.run(host='0.0.0.0', port=8080)
