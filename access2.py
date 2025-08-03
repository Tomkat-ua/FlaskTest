from flask import Flask, request, jsonify,abort
from functools import wraps

app = Flask(__name__)

USERNAME = "excel_user"
PASSWORD = "s3cr3t"


AUTHORIZED_KEYS = {
    "key-abc-123": "FinanceDept",
    "key-def-456": "WarehouseApp"
}

@app.before_request
def check_api_key():
    api_key = request.headers.get("X-API-KEY")
    if api_key not in AUTHORIZED_KEYS:
        abort(403, description="Forbidden: Invalid API key")


def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({"message": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route("/api/data")
@require_auth
def get_data():
    return jsonify({"result": "вітання колегам, це дуже секретна інфа і ви її добули, вітаю !"})

if __name__ == '__main__':
    app.run(host='192.168.10.9', port=5000)
