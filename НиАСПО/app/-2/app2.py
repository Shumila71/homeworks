from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data = {'mess':'Its a message from second container dadadada -/-'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='app2',port = 5001)
