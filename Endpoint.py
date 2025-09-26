from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)
registrations = {}  # In-memory store for registration codes

@app.route("/registration", methods=["POST"])
def registration():
    data = request.get_json()
    if not data or "uid" not in data:
        return jsonify({"error": "Missing uid"}), 400

    uid = data["uid"]
    code = secrets.token_hex(3).upper()
    registrations[uid] = code
    print(f"[Registration] UID: {uid} -> Code: {code}")
    return jsonify({"code": code})
