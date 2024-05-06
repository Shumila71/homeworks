from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://app2:5001')
    return jsonify({'message': 'Hello from Container 1!', 'response_from_app2': response.json()})

if __name__ == '__main__':
    app.run(host='app1',port = 5000)
