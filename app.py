from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route("/")
def hello():
    return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
