from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    print(f"Received location: {data}")
    return jsonify({"status": "success", "message": "Location received"}), 200

if __name__ == "__main__":
    app.run(debug=True)