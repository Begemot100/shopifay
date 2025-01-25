from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Добро пожаловать на сервер Flask!"

@app.route('/location', methods=['POST', 'GET'])
def location():
    if request.method == 'GET':
        return "Этот маршрут поддерживает только POST запросы.", 405

    if request.method == 'POST':
        data = request.json
        if data:
            print(f"Координаты: {data}")
            return jsonify({"status": "success", "message": "Coordinates received"}), 200
        return jsonify({"status": "error", "message": "No data received"}), 400

if __name__ == '__main__':
    app.run(debug=True)