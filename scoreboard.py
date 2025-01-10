from flask import Flask, jsonify
import time

app = Flask(__name__)

def read_scores():
    scores = []
    with open('results.txt', 'r') as file:
        for line in file:
            result, date = line.strip().split(' ')
            scores.append({'result': result, 'date': date})
    return scores

@app.route('/scores', methods=['GET'])
def get_scores():
    return jsonify(read_scores())

if __name__ == '__main__':
    app.run(debug=True)