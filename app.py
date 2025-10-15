import json
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS

# ==== Initialization ====
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

# ==== Load FAQ data ====
with open("customer_support_faqs.json", "r") as f:
    faq_data = json.load(f)

# ==== Simple similarity function ====
def simple_similarity(query, faq_question):
    query_set = set(query.lower().split())
    faq_set = set(faq_question.lower().split())
    intersection = query_set.intersection(faq_set)
    union = query_set.union(faq_set)
    return len(intersection) / len(union) if union else 0

def retrieve_similar_faqs_local(query, top_k=3):
    scored = [(simple_similarity(query, faq["question"]), faq) for faq in faq_data]
    scored.sort(key=lambda x: -x[0])
    return [f for score, f in scored if score > 0][:top_k]

# ==== API endpoint for suggestions ====
@app.route("/api/suggest_faqs")
def suggest():
    q = request.args.get("q", "").lower().strip()
    if not q:
        return jsonify([])
    suggestions = [f["question"] for f in faq_data if q in f["question"].lower()]
    return jsonify(suggestions[:5])

# ==== SocketIO message handling ====
@socketio.on('message')
def handle_message(data):
    user_message = data.get('message')
    print('\n[DEBUG] Received:', user_message)
    top_faqs = retrieve_similar_faqs_local(user_message)
    if top_faqs:
        answer = top_faqs[0]['answer']
    else:
        answer = "Sorry, I couldn't find an answer to your question."
    emit('response', {'message': answer})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
