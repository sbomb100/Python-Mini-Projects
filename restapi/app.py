#CRUD operations (Create, Read, Update, Delete).from flask import Flask, jsonify, request
from flask import Flask, jsonify, request

app = Flask(__name__)

#fake database
books = [
    {"id": 1, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a specific book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()  # Get the JSON data from the request body
    if 'title' not in new_book or 'author' not in new_book:
        return jsonify({"error": "Missing title or author"}), 400

    new_book['id'] = books[-1]['id'] + 1 if books else 1  # Assign an ID
    books.append(new_book)
    return jsonify(new_book), 201

# Route to update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    updated_data = request.get_json()
    book.update(updated_data)
    return jsonify(book)

# Route to delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    title = book.get("title")
    books.remove(book)
    return jsonify({"message": f"{title} deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

#curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"title": "Brave New World", "author": "Aldous Huxley"}'
#curl -X PUT http://127.0.0.1:5000/books/1 -H "Content-Type: application/json" -d '{"title": "1984 (Updated)", "author": "George Orwell"}'
#curl -X DELETE http://127.0.0.1:5000/books/1