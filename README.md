# flask-crud-challenge
# Implement Simple CRUD API

Your task is to implement simple CRUD API using a simple in-memory data structure.

# Details:
  - Create a Flask application that allows users to perform CRUD (Create, Read, Update, Delete) operations on a list of books. The application should have the following routes:

       1. **GET** _/books_: This route should return a list of all books.
       2. **GET** _/books/:id_: This route should return the details of a specific book identified by its ID.
       3. **POST** _/books_: This route should allow users to add a new book to the list.
       4. **PUT** _/books/:id_: This route should allow users to update the details of a specific book identified by its ID.
       5. **DELETE** _/books/:id_: This route should allow users to delete a specific book identified by its ID.

- The book details should include the following attributes.
  - _id_ - unique identifier (uuid, **required**) generated on server side
  - _title_ - book's title (string, **required**)
  - _author_ - book's auther name (string, **required**)
  - _price_ - book's price (int, **required**)
  - _category_ - book's category (_array_ of _strings_, **required**)
  - _publication_year_ - date and year of the book's publicaiton (date, **required**)


- Requests to non-existing endpoints (e.g. _/some-non/existing/resource_) should be handled.
- Internal server errors should be handled and processed correctly.
- Make sure the api is accesible by frontend apps hosted on a different domain (cross-site resource sharing)


---
---

# Simple Doc for Flask App [Version 1]

A lightweight Flask application that runs entirely in-memory, no database required! This app provides basic book management functionality with RESTful API routes.

## Features:
- Add, update, delete, and fetch books.
- Runs in-memory (no database required).
- Dockerized for easy deployment.

## Getting Started:

### Prerequisites:
- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)

### Run Locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Yohannes90/flask-crud-challenge.git
   cd flask-crud-challenge
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python -m flask --app app run
   ```

4. **Access the API**
   - Open your browser or Postman and visit: `http://127.0.0.1:5000/books`

### Run with Docker:

1. **Build the Docker image**
   ```bash
   docker build -t flask-app .
   ```

2. **Run the Docker container**
   ```bash
   docker run -p 5000:5000 flask-app
   ```

3. **Access the API**
   - Open your browser or Postman and visit: `http://localhost:5000/books`

---

## API Endpoints:
- **GET** `/books` - Retrieve all books.
- **GET** `/books/:id` - Retrieve a specific book by ID.
- **POST** `/books` - Add a new book.
- **PUT** `/books/:id` - Update an existing book by ID.
- **DELETE** `/books/:id` - Delete a book by ID.

---
