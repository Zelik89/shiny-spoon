from flask import Flask, request, jsonify
import secrets
import os

app = Flask(__name__)
registrations = {}

@app.route("/registration", methods=["POST"])
def registration():
    raw_data = request.data.decode("utf-8")  # read body as string
    print("Received raw data:", raw_data)

    # Try to parse JSON manually
    import json
    try:
        data = json.loads(raw_data)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON"}), 400

    if "uid" not in data:
        return jsonify({"error": "Missing uid"}), 400

    uid = data["uid"]
    import secrets
    code = secrets.token_hex(3).upper()
    registrations[uid] = code
    return jsonify({"code": code})

def start_flask():
    """Starts the Flask app"""
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Optional: allow running Flask directly
if __name__ == "__main__":
    start_flask()
