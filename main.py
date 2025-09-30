from flask import Flask, request, jsonify
import secrets
import os

app = Flask(__name__)
registrations = {}

@app.route("/registration", methods=["POST"])
def registration():
    try:
        # Attempt to parse JSON directly
        data = request.get_json(force=True)  # <-- force=True parses even if Content-Type is not application/json
    except Exception as e:
        print("Failed to parse JSON:", e)
        return jsonify({"error": "Invalid JSON"}), 400

    if not data or "uid" not in data:
        return jsonify({"error": "Missing uid"}), 400

    uid = data["uid"]
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
