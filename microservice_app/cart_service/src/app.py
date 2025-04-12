import logging
import redis

from flask import Flask, request, abort, render_template, redirect, url_for

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

cart_db = redis.Redis(host='redis', port=6379, db=1, decode_responses=True)

@app.route('/cart', methods=['GET'])
def view_cart():
    user_id = request.args.get("user_id", "default")

    # recupera o carrinho do usuario
    cart_items = cart_db.hgetall(f"cart:{user_id}")

    cart = {book_id: int(quantity) for book_id, quantity in cart_items.items()}

    return render_template('cart.html', cart=cart)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    user_id = request.form.get("user_id", "default")
    book_id = request.form.get("book_id")

    if not book_id:
        abort(400, description="Missing book_id")
    
    # incrementa em 1 unidade o livro no carrinho do usuário
    cart_db.hincrby(f"cart:{user_id}", book_id)

    return redirect(url_for("view_cart"))

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    user_id = request.form.get("user_id", "default")
    book_id = request.form.get("book_id")

    if not book_id:
        abort(400, description="Missing book_id")

    # recupera do carrinho do usuário, a qtde de um livro
    current_qty = int(cart_db.hget(f"cart:{user_id}", book_id) or 0)
    
    if current_qty <= 1:
        # deleta do carrinho do usuário o livro
        cart_db.hdel(f"cart:{user_id}", book_id)
    else:
        # decrementa em 1 unidade o livro no carrinho do usuário
        cart_db.hincrby(f"cart:{user_id}", book_id, -1)

    return redirect(url_for("view_cart"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5051)
