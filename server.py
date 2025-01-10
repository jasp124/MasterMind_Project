from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/get-results')
def get_results():
    results = []
    try:
        with open('results.txt', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    result, date = parts
                    results.append({'result': result, 'date': date})
    except FileNotFoundError:
        pass
    return jsonify(results)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
