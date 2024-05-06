from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://app1:5000')
    return jsonify({'message': 'Hello from Container 3!', 'response_from_app1': response.json()})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5002)
