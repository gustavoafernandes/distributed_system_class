from flask import Flask, request, render_template, redirect, url_for
import redis

app = Flask(__name__)
db = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/', methods=['GET'])
def home():
    messages = db.lrange('messages', 0, -1)
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit_message():
    message = request.form['message']
    db.rpush('messages', message)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
