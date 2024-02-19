from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Book:
    def __init__(self, title, author, isbn, publication_year, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.status = status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def update_book_status(self, isbn, new_status):
        for book in self.books:
            if book.isbn == isbn:
                book.status = new_status
                return True
        return False

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "available":
                    book.status = "borrowed"
                    return True
                else:
                    return False
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "borrowed":
                    book.status = "available"
                    return True
                else:
                    return False
        return False

    def search_books(self, query):
        query_lower = query.lower()
        results = []
        for book in self.books:
            if (query_lower in book.title.lower() or
                query_lower in book.author.lower() or
                query_lower in str(book.publication_year)):
                results.append(book)
        return results

library = Library()

@app.route('/')
def index():
    return render_template('index.html', books=library.books)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    isbn = request.form['isbn']
    publication_year = request.form['publication_year']
    new_book = Book(title, author, isbn, publication_year)
    library.add_book(new_book)
    return redirect(url_for('index'))

@app.route('/update_status', methods=['POST'])
def update_status():
    isbn = request.form['isbn']
    new_status = request.form['status']
    if library.update_book_status(isbn, new_status):
        return redirect(url_for('index'))
    else:
        return "Book not found", 404

@app.route('/remove_book', methods=['POST'])
def remove_book():
    isbn = request.form['isbn']
    if library.remove_book(isbn):
        return redirect(url_for('index'))
    else:
        return "Book not found", 404

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    isbn = request.form['isbn']
    if library.borrow_book(isbn):
        return redirect(url_for('index'))
    else:
        return "Book not available for borrowing or not found", 404

@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    query = ''
    if request.method == 'POST':
        query = request.form.get('query', '')
        if query:
            results = library.search_books(query)
    print("Results:", results)  # Add this line to print the results
    return render_template('search.html', results=results, query=query)


@app.route('/return_book', methods=['POST'])
def return_book():
    isbn = request.form['isbn']
    if library.return_book(isbn):
        return redirect(url_for('index'))
    else:
        return "Book not available for returning or not found", 404

if __name__ == '__main__':
    app.run(debug=True)
