from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import firestore

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://chat.openai.com"]}}, supports_credentials=True)

API_KEY = "chingasa"
db = firestore.Client()

@app.before_request
def require_api_key():
    auth = request.headers.get("Authorization") or request.args.get("key", "")
    if auth != f"Basic {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

@app.route('/')
def index():
    return "Hexengine online. Accessing table vault."

@app.route('/get/<doc_id>', methods=['GET'])
def get_table_entry(doc_id):
    doc = db.collection('hex_generation_log').document(doc_id).get()
    return jsonify(doc.to_dict()) if doc.exists else ("Not found", 404)

@app.route('/post/<doc_id>', methods=['POST'])
def post_table_entry(doc_id):
    data = request.json
    db.collection('hex_generation_log').document(doc_id).set(data)
    return jsonify({"status": "written", "doc": doc_id})

@app.route('/list', methods=['GET'])
def list_table_ids():
    docs = db.collection('hex_generation_log').stream()
    return jsonify([doc.id for doc in docs])

if __name__ == "__main__":
    app.run(port=5002)
