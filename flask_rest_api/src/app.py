from flask import Flask, request, jsonify, abort
from flasgger import Swagger

# cria uma instância do serviço
app = Flask(__name__)

# Inicializa o Swagger
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

# helper function: localiza um livro pelo id
def get_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

# -- Rotas
@app.route('/')
def home():
    """
    Home endpoint returning a welcome message.
    ---
    responses:
      200:
        description: A welcome message.
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
def get_books():
    """
    Retrieve all books.
    ---
    responses:
      200:
        description: A list of books.
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
                example: '2025'
    """
    return jsonify(books)

# recupera um único livro
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """
    Retrieve a specific book by its ID.
    ---
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
        description: The ID of the book to retrieve.
    responses:
      200:
        description: Book details.
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
              example: '2025'
      404:
        description: Book not found.
    """
    book = get_book_by_id(book_id)
    if book is None:
        abort(404, description="Book not found")
    return jsonify(book)
    
# cria um novo recurso (livro) no serviço
@app.route('/books', methods=['POST'])
def create_book():
    """
    Create a new book.
    ---
    parameters:
      - in: body
        name: book
        description: The book data.
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
              example: '2025'
    responses:
      201:
        description: The created book.
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
              example: '2025'
      400:
        description: Invalid input.
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
    return jsonify(new_book), 201

# atualiza um livro existente
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    Update an existing book.
    ---
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
        description: The ID of the book to update.
      - in: body
        name: book
        description: The book data to update.
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
              example: '2025'
    responses:
      200:
        description: The updated book.
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
              example: '2025'
      400:
        description: Invalid input.
      404:
        description: Book not found.
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
    
    return jsonify(book)

'''
Você deverá criar uma rota para deletar um item da base.
A rota deve ser no formato "/books/<int:book_id>". Atente-se à variável
'book_id'. A requisição é somente para DELETE. Implemente toda lógica
necessária para a remoção do item. Dica: veja os métodos 
.index() [1], pop() [2] e remove() [3].
[1] https://www.programiz.com/python-programming/methods/list/index
[2] https://www.programiz.com/python-programming/methods/list/pop
[3] https://www.programiz.com/python-programming/methods/list/remove
'''
# remove um livro
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Delete an existing book.
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
    ## TODO: Implemente toda lógica:
    ## - Use a funcao get_book_by_id qndo necessario.
    ## - Use abort(404, description="Book not found") qndo necessario.
    
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)