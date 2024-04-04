from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    data = {'message': 'Its a message from second container dadadada :)'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181)
