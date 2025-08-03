from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Список дозволених API-ключів і відповідних HWID
AUTHORIZED_CLIENTS = {
    "abc123": "DESKTOP-TEST01",
    "xyz789": "LAPTOP-USER"
}

@app.route('/api/data', methods=['GET'])
def get_data():
    api_key = request.headers.get("X-API-KEY")
    hwid = request.headers.get("X-HWID")

    if not api_key or not hwid:
        abort(403, description="Missing API key or HWID")

    if AUTHORIZED_CLIENTS.get(api_key) != hwid:
        abort(403, description="Invalid API key or HWID")

    return jsonify({
        "status": "success",
        "source": hwid,
        "data": [1, 2, 3, 4]
    })

if __name__ == '__main__':
    app.run(host='192.168.10.9', port=5000)
