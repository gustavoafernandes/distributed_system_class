from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated "database" for topics, subscribers, and messages
topics = {'sports', 'tech', 'entertainment'}  # Available topics
subscribers = [] # List of subscribers
messages = {}  # Key: topic, Value: list of messages


# Publisher endpoint (should be a service)
@app.route('/publish', methods=['POST'])
def publish():
    data = request.json
    topic = data.get('topic')
    message = data.get('message')

    if topic not in topics:
      return jsonify({'error': 'Invalid topic'}), 400
        
    if topic not in messages:
        messages[topic] = []
    messages[topic].append(message)
    
    # Notify subscribers for the topic
    for subscriber in subscribers:
        if subscriber['topic'] == topic:
            # Simulate calling subscriber's callback URL with the message
            print(f"Notification for {subscriber['callback_url']}: {message}")
    
    return jsonify({'status': 'Message published to ' + topic})


# Subscriber registration endpoint (should be a service)
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    topic = data.get('topic')
    callback_url = data.get('callback_url')
    callback_url = f"http://example.com/{callback_url}"
    
    # Check if the topic exists
    if topic not in topics:
        return jsonify({'error': 'Invalid topic'}), 400
    
    subscribers.append({"topic": topic, "callback_url": callback_url})
    
    return jsonify({'status': 'Subscribed successfully to ' + topic})


# Endpoint to view subscribers and messages
@app.route('/info', methods=['GET'])
def get_info():
    info = {
        'topics': list(topics),
        'subscribers': subscribers,
        'messages': messages
    }
    return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
