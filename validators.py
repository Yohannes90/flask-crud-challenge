from datetime import datetime


# Validate the book data
def validate_book(data):
    required_fields = ['title', 'author', 'price', 'category', 'publication_year']
    for field in required_fields:
        if field not in data:
            return {"error": f"'{field}' is a required field."}, 400

    if not isinstance(data['title'], str):
        return {"error": "'title' must be a string."}, 400

    if not isinstance(data['author'], str):
        return {"error": "'author' must be a string."}, 400

    if not isinstance(data['price'], int):
        return {"error": "'price' must be an integer."}, 400

    if not isinstance(data['category'], list) or not all(isinstance(cat, str) for cat in data['category']):
        return {"error": "'category' must be an array of strings."}, 400

    try:
        pub_year = int(data['publication_year'])
        if pub_year > datetime.now().year:
            return {"error": "'publication_year' cannot be in the future."}, 400
    except ValueError:
        return {"error": "'publication_year' must be a valid year (integer)."}, 400

    return None
