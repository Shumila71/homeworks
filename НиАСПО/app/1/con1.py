from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://container2:8181/data')
    data_from_container2 = response.json()

    return jsonify(data_from_container2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)