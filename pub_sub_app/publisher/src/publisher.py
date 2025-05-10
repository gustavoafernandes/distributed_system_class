import logging
import redis

from flask import Flask, request, jsonify

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# cria uma instância do serviço
app = Flask(__name__)

# cria uma instância do Redis (mesma do subscriber)
db = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

@app.route("/publish", methods=["POST"])
def publish():
    # abre a requisição e busca por "topic" e "message"
    data = request.get_json()
    topic = data.get("topic")
    message = data.get("message")
    if not topic or not message:
        return jsonify({"error": "Both 'topic' and 'message' required"}), 400

    # publica topico/mensagem para o Redis
    db.publish(topic, message)

    # retorna qual topico foi publicado
    return jsonify({"status": f"Message published to '{topic}'"}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
