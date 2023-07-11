from flask import Flask, jsonify, request

app = Flask(__name__)

books = []

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'})

@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        'id': len(books) + 1,
        'title': request.json['title'],
        'author': request.json['author'],
        'publication_year': request.json['publication_year']
    }
    books.append(new_book)
    return jsonify({'message': 'Book added successfully'})

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book['title'] = request.json.get('title', book['title'])
        book['author'] = request.json.get('author', book['author'])
        book['publication_year'] = request.json.get('publication_year', book['publication_year'])
        return jsonify({'message': 'Book updated successfully'})
    return jsonify({'error': 'Book not found'})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'error': 'Book not found'})

if __name__ == '__main__':
    app.run()
