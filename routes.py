from flask import Blueprint, jsonify, request
from uuid import uuid4
from validators import validate_book


book_routes = Blueprint('book_routes', __name__)

# In-memory data structure
books = []


@book_routes.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books), 200


@book_routes.route('/books/<string:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book), 200

    return jsonify({"error": "Book not found"}), 404


@book_routes.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided."}), 400

    validation_error = validate_book(data)
    if validation_error:
        return jsonify(validation_error), validation_error[1]

    new_book = {
        'id': str(uuid4()),
        'title': data['title'],
        'author': data['author'],
        'price': data['price'],
        'category': data['category'],
        'publication_year': data['publication_year']
    }
    books.append(new_book)

    return jsonify(new_book), 201


@book_routes.route('/books/<string:book_id>', methods=['PUT'])
def update_book_by_id(book_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided."}), 400

    validation_error = validate_book(data)
    if validation_error:
        return jsonify(validation_error), validation_error[1]

    for book in books:
        if book['id'] == book_id:
            book.update(data)
            return jsonify(book), 200

    return jsonify({"error": "Book not found"}), 404


@book_routes.route('/books/<string:book_id>', methods=['DELETE'])
def delete_book_by_id(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"}), 200

    return jsonify({"error": "Book not found"}), 404


@book_routes.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


@book_routes.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400


@book_routes.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An internal error occurred"}), 500






