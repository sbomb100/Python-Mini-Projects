#CRUD operations (Create, Read, Update, Delete)
from flask import Flask, jsonify, request

app = Flask(__name__)

#fake database
books = [
    {"id": 1, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

#@app.route('x', methods=["y"])
#def do_thing():

#@app.route is for the url where x is the url exension (example.com/x or localhost:3000/x)
#methods is the http methods to use with data
# notice since the web part is just an exension of the fake database, all these methods are just
#to show how we can interact with the database using CURL methods.
#the actual database management is done in file here.

#jsonify is used to format the database to the given url/extension

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()  # get the JSON data from the request body
    if 'title' not in new_book or 'author' not in new_book:
        return jsonify({"error": "Missing title or author"}), 400

    new_book['id'] = books[-1]['id'] + 1 if books else 1 
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    updated_data = request.get_json()
    book.update(updated_data)
    return jsonify(book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    title = book.get("title")
    books.remove(book)
    return jsonify({"message": f"{title} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

#curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"title": "Brave New World", "author": "Aldous Huxley"}'
#curl -X PUT http://127.0.0.1:5000/books/1 -H "Content-Type: application/json" -d '{"title": "1984 (Updated)", "author": "George Orwell"}'
#curl -X DELETE http://127.0.0.1:5000/books/1