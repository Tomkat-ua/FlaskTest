from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    return jsonify({"message": "Secure JSON response"})


if __name__ == "__main__":
    # HTTPS запуск із сертифікатами
    app.run(
        host="0.0.0.0",
        port=8443,
        ssl_context=("cert.pem", "key.pem")  # tuple: (cert, key)
    )
