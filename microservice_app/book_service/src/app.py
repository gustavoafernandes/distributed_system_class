import logging
import redis

from flask import Flask, request, abort, render_template, redirect, url_for

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# cria uma instância do serviço
app = Flask(__name__)

# cria uma instância do Redis
db = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# --- helper functions
def initialize_books() -> None:
    """
    Inicializa o Redis com alguns livros, caso não existam.
    """
    if db.scard("books") == 0:
        # verifica o número de elementos armazenados no set 'books'

        sample_books = [
            {
                "title": "Flask Web Development: Developing Web Applications with Python",
                "author": "Miguel Grinberg",
                "published": "2018"
            },
            {
                "title": "Docker: Up & Running: Shipping Reliable Containers in Production",
                "author": "Sean P Kane, Karl Matthias",
                "published": "2018"
            },
            {
                "title": "Learning SQL: Generate, Manipulate, and Retrieve Data",
                "author": "Alan Beaulieu",
                "published": "2020"
            }
        ]
        for book in sample_books:

            # Incrementa em 1 o valor de uma chave. 
            # Se a chave não existe, será criada com valor inicial 1.
            new_id = db.incrby("book:id")

            book["id"] = new_id

            # armazena um hash para cada chave de cada livro
            db.hmset(f"book:{new_id}", book)

            # add o livro no set 'books'
            db.sadd("books", new_id)

def get_book_by_id(book_id) -> dict:
    """
    Retorna um livro da lista pelo seu ID.

    Args:
        book_id (int): Um identificador único do livro a ser recuperado.

    Returns:
        book (dict or None): Um livro, se encontrado; caso contrário, se não existe 
        um livro com o ID especificado, retorna None.
    """

    # recupera um elemento pelo hash da chave fornecida
    book = db.hgetall(f"book:{book_id}")

    if not book:
        return None
    book["id"] = int(book["id"])
    return book

def get_all_books() -> list:
    """
    Recupera todos os livros armazenados no Redis.

    Returns:
        books (list): Uma lista ordenada de dicionários.
    """
    # retorna todos os elementos do set 'livros'
    book_ids = db.smembers("books")

    books = []
    for book_id in book_ids:

        # recupera um elemento pelo hash da chave
        book = db.hgetall(f"book:{book_id}")
        if book:
            book["id"] = int(book["id"])
            books.append(book)
    return sorted(books, key=lambda b: b["id"])

# -- Rotas
@app.route('/books')
def home():
    """
    Default endpoint que retorna a página index do app.

    Returns:
        template (str): template index.html renderizado.
    """
    books = get_all_books()
    return render_template('index.html', books=books)

# cria um novo recurso (livro) no serviço
@app.route('/books/new', methods=['GET', 'POST'])
def create_book():
    """
    Cria um novo livro usando os dados do formulário.

    Returns:
        response (Flask Response): Renderiza o formulário para requisições GET,
        ou redireciona para o home após criar um novo livro.
    """
    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        published = request.form.get("published")
        if not title or not author or not published:
            logger.error("Missing required fields: title, author, published")
            return redirect(url_for("create_book"))

        new_id = db.incrby("book:id")
        book = {"id": new_id, "title": title, "author": author, "published": published}
        db.hmset(f"book:{new_id}", book)
        db.sadd("books", new_id)

        logger.info("Book added successfully!")
        return redirect(url_for("home"))

    return render_template("create_book.html")

# atualiza um livro existente
@app.route('/books/<int:book_id>/edit', methods=['GET', 'POST'])
def update_book(book_id):
    """
    Atualiza um livro existente pelo seu ID usando dados do formulário.

    Args:
        book_id (int): Identificador único do livro a ser atualizado.
    
    Returns:
        response (Flask Response): Renderiza o formulário de atualização
        para requisições GET, ou redireciona para a home após atualizar
        o livro com dados do formulário.
    """
    book = get_book_by_id(book_id)
    if book is None:
        abort(404, description="Book not found")

    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        published = request.form.get("published")
        if title:
            # atualiza um campo do elemento baseado no hash
            db.hset(f"book:{book_id}", "title", title)
        if author:
            db.hset(f"book:{book_id}", "author", author)
        if published:
            db.hset(f"book:{book_id}", "published", published)

        logger.info("Book updated successfully!")
        return redirect(url_for("home"))
    
    return render_template("update_book.html", book=book)

# remove um livro
@app.route('/books/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    """
    Remove um livro existente pelo seu ID.

    Args:
        book_id (int): Identificador único do livro a ser removido.
    
    Returns:
        response (Flask Response): Redireciona para a home após remover
        o livro.
    """
    book = get_book_by_id(book_id)
    if book is None:
        abort(404, description="Book not found")

    # remove o hash de um elemento
    db.delete(f"book:{book_id}")

    # remove o elemento pelo seu ID
    db.srem("books", book_id)

    logger.info("Book deleted successfully!")
    return redirect(url_for("home"))


if __name__ == "__main__":
    initialize_books()
    app.run(debug=True, host='0.0.0.0', port=5050)