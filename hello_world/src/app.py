from flask import Flask, request, redirect, url_for

app = Flask(__name__)

message_store = {"message": "Olá, turma de Sistemas Distribuídos!"}

@app.route('/', methods=['GET'])
def home():
    # Display the current or default message
    return message_store["message"]

@app.route('/send', methods=['POST'])
def send_message():
    # Store the new message from the json data
    message = request.get_json(force=True)
    if message:
        message_store["message"] = message["message"]
    # Redirect back to the home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
