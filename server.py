from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the main page!"

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    return jsonify({"status": "success", "data": data})

if __name__ == "__main__":
    app.run(debug=True)