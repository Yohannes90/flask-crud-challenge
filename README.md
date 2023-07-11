# flask-crud-challenge
# Implement Simple CRUD API

Your task is to implement simple CRUD API using a simple in-memory data structure.

# Details:
  Create a Flask application that allows users to perform CRUD (Create, Read, Update, Delete) operations on a list of books. The application should have the following routes:

  1. **GET** _/books_: This route should return a list of all books.
  2. **GET** _/books/:id_: This route should return the details of a specific book identified by its ID.
  3. **POST** _/books_: This route should allow users to add a new book to the list.
  4. **PUT** _/books/:id_: This route should allow users to update the details of a specific book identified by its ID.
  5. **DELETE** _/books/:id_: This route should allow users to delete a specific book identified by its ID.

  The book details should include the following attributes.
  1.  _id_ - unique identifier (string) generated on server side
  2.  _title_ - book's title (string, **required**)
  3.  _author_ - book's auther name (string, **required**)
  4.  _publication_year_ - date and year of the book's publicaiton (date, **required**)  
