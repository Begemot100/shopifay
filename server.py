from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Добро пожаловать на сервер Flask!"

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    if data:
        print(f"Координаты: {data}")
        return jsonify({"status": "success", "message": "Coordinates received"}), 200
    return jsonify({"status": "error", "message": "No data received"}), 400

if __name__ == '__main__':
    app.run(debug=True)