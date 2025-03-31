import logging
from flask import Flask, request, jsonify, abort
from flask_caching import Cache
from flasgger import Swagger

logger = logging.getLogger(__name__)

# cria uma instância do serviço
app = Flask(__name__)

# Configura cache server‑side: SimpleCache = in-memory cache
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

# Inicializa o Swagger via Flasgger
swagger = Swagger(app)

# data
books = [
    {
        "id": 0,
        "title": "Flask Web Development: Developing Web Applications with Python",
        "author": "Miguel Grinberg",
        "published": "2018"
     },
    {
        "id": 1,
        "title": "Docker: Up & Running: Shipping Reliable Containers in Production",
        "author": "Sean P Kane, Karl Matthias",
        "published": "2018"
        },
    {
        "id": 2,
        "title": "Learning SQL: Generate, Manipulate, and Retrieve Data",
        "author": "Alan Beaulieu",
        "published": "2020"
     }
]

# --- helper functions

def get_book_by_id(book_id):
    """
    Retorna um livro da lista pelo seu ID.

    Args:
        book_id (int): Um identificador único do livro a ser recuperado.

    Returns:
        book (dict or None): Um livro, se encontrado; caso contrário, se não existe 
        um livro com o ID especificado, retorna None.
    """
    for book in books:
        if book["id"] == book_id:
            return book
    return None

@app.after_request
def add_client_cache_headers(response):
    """
    Checa se uma requisição é um GET e, se for, add um
    Cache-Control que diz ao browser para armazenar a 
    resposta por 60 segundos. Com isso o browser reutiliza
    a mesma resposta da api.

    Args:
      response (flask.Response): O objeto de resposta HTTP.

    Returns:
        response (flask.Response): O objeto de resposta modificado 
        com o cabeçalho de cache apropriado.
    """
    if request.method == 'GET':
        # Instrui o cliente (browser) para cachear a resposta por 20 segundos.
        response.headers["Cache-Control"] = "public, max-age=20"
    return response

# -- Rotas
@app.route('/')
def home():
    """
    Default endpoint que retorna uma simples mensagem.
    ---
    responses:
      200:
        description: Mensagem de boas vindas.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Welcome to the Book Store API
    """
    return jsonify({'message': 'Welcome to the Book Store API'})

# recupera todos os livros
@app.route('/books', methods=['GET'])
@cache.cached(timeout=60) # server-side cache para 60 segundos
def get_books():
    """
    Recupera todos os livros.
    ---
    responses:
      200:
        description: Lista de livros.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 0
              title:
                type: string
                example: Title here
              author:
                type: string
                example: Author here
              published:
                type: string
                example: Year
    """
    logger.info("Getting all books")
    return jsonify(books)

# recupera um único livro
@app.route('/books/<int:book_id>', methods=['GET'])
@cache.cached(timeout=60)
def get_book(book_id):
    """
    Recupera um livro específico pelo seu ID.
    ---
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
        description: O ID do livro.
    responses:
      200:
        description: Detalhes do livro.
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 0
            title:
              type: string
              example: Title here
            author:
              type: string
              example: Author here
            published:
              type: string
              example: Year
      404:
        description: Livro não encontrado.
    """
    book = get_book_by_id(book_id)
    if book is None:
        abort(404, description="Book not found")
    return jsonify(book)
    
# cria um novo recurso (livro) no serviço
@app.route('/books', methods=['POST'])
def create_book():
    """
    Cria um novo livro.
    ---
    parameters:
      - in: body
        name: book
        description: Dados do livro.
        schema:
          type: object
          required:
            - title
            - author
            - published
          properties:
            title:
              type: string
              example: New Book Title
            author:
              type: string
              example: New Book Author
            published:
              type: string
              example: '2021'
    responses:
      201:
        description: O livro criado.
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 3
            title:
              type: string
              example: New Book Title
            author:
              type: string
              example: New Book Author
            published:
              type: string
              example: '2021'
      400:
        description: Entrada inválida.
    """
    if not request.json:
        abort(400, description="Request must be JSON")
    new_book = request.get_json()
    
    # valida alguns campos
    if "title" not in new_book or "author" not in new_book or "published" not in new_book:
        abort(400, description="Missing required fields: title, author, published")
    
    # atribui um único id
    new_book["id"] = books[-1]["id"] + 1 if books else 0
    books.append(new_book)

    # limpa o cache
    cache.delete_memoized(get_books)

    return jsonify(new_book), 201

# atualiza um livro existente
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    Atualiza um livro existente.
    ---
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
        description: O ID do livro para atualizar.
      - in: body
        name: book
        description: Os dados para atualizar do livro.
        schema:
          type: object
          properties:
            title:
              type: string
              example: Updated Book Title
            author:
              type: string
              example: Updated Book Author
            published:
              type: string
              example: '2022'
    responses:
      200:
        description: O livro atualizado.
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            title:
              type: string
              example: Updated Book Title
            author:
              type: string
              example: Updated Book Author
            published:
              type: string
              example: '2022'
      400:
        description: Entrada invalida.
      404:
        description: Livro não encontrado.
    """
    book = get_book_by_id(book_id)

    if book is None:
        abort(404, description="Book not found")

    if not request.json:
        abort(400, description="Request must be JSON")
    
    update_data = request.get_json()

    # atualiza os campos fornecidos ou mantém os valores atuais
    book["title"] = update_data.get("title", book["title"])
    book["author"] = update_data.get("author", book["author"])
    book["published"] = update_data.get("published", book["published"])

    # limpa o cache
    cache.delete_memoized(get_books)
    cache.delete_memoized(get_book, book_id)
    
    return jsonify(book)

# remove um livro
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Deleta um livro existente.
    ---
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
        description: The ID of the book to delete.
    responses:
      200:
        description: Deletion success.
        schema:
          type: object
          properties:
            result:
              type: boolean
              example: true
      404:
        description: Book not found.
    """
    book = get_book_by_id(book_id)

    if book is None:
        abort(404, description="Book not found")
    
    books.remove(book)

    # limpa o cache
    cache.delete_memoized(get_books)
    cache.delete_memoized(get_book, book_id)

    return jsonify({'result': True})

@app.route('/set_cookie', methods=['GET'])
def set_cookie():
    """
    Define um cookie no cliente.
    ---
    responses:
      200:
        description: Um cookie é criado no lado cliente.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Cookie has been set."
    """
    response = jsonify({"message": "Cookie has been set."})
    
    # Define um cookie de chave "favorite_book" com max-age de 300 segundos (5 min)
    response.set_cookie("favorite_book", "Flask Web Development", max_age=360)
    return response

@app.route('/get_cookie', methods=['GET'])
def get_cookie():
    """
    Recupera o valor do cookie 'favorite_book'.
    ---
    responses:
      200:
        description: Cookie 'favorite_book'.
        schema:
          type: object
          properties:
            favorite_book:
              type: string
              example: "Web Development"
    """
    favorite_book = request.cookies.get("favorite_book")
    return jsonify({"favorite_book": favorite_book})

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True, host='0.0.0.0', port=5050)