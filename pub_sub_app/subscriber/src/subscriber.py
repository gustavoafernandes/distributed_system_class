import logging
import os
import threading
import redis

from flask import Flask, jsonify

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
messages = []  # armazena In-memory as mensagens recebidas

# cria uma instância do Redis (mesma do publisher)
db = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

# cria um objeto pusub do redis
pubsub = db.pubsub()

# Topics para subscrição
topics = os.getenv("TOPICS", "sports,tech,entertainment").split(",")
pubsub.subscribe(*topics) # subscreve aos tópicos

def listener():
    # função para rodar em background
    for msg in pubsub.listen(): # aguarda alguma publicação
        if msg['type'] == 'message':
            # extrai a mensagem e add na lista de mensagens
            record = {"topic": msg['channel'], "message": msg['data']}
            messages.append(record)
            logger.info(f"[subscriber] Received on '{msg['channel']}': {msg['data']}")

# Iniciar uma thread (não bloqueia o subscriber)
t = threading.Thread(target=listener, daemon=True)
t.start()

@app.route("/messages", methods=["GET"])
def get_messages():
    """Retorna a lista de mensagens recebidas pelos tópicos de interesse"""
    return jsonify(messages)

@app.route("/subscriptions", methods=["GET"])
def get_subscriptions():
    """Retorna a lista de tópicos assinados"""
    return jsonify({"subscriptions": topics}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051, debug=True)
