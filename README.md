# :zap:book-CRUD
Asing this Flask API one can
<li>add books</li>
<li>issue books</li>
<li>search books based on book id, year, author</li>
<br>


# Setting it up

If you plan to use or contribute, below are the steps you need to follow.

### :arrow_right: Fork, and clone the repository.

If you have SSH keys, use -
```sh
    $ git clone git@github.com:<username>/book-CRUD
```
If you don't, use HTTPS instead -
```sh
    $ git clone https://github.com/<username>/book-CRUD
```
where, `<username>` is your own GitHub username.

### :arrow_right: Navigate to project root
Next, `cd book-CRUD/` to get inside the project directory.

### :arrow_right: Create and activate a virtual environment (optional / recommended)

To create a virtual environment, run:

    $ python3 -m venv venv
(or use `virtualenv` instead).

To activate it in Linux-based systems -

    $ source venv/bin/activate

To activate it in Windows -

    $ \venv\Scripts\activate.bat

### Install dependencies.
```
$ pip install -r requirements.txt
```
### Run the application.
```
$ python3 master.py
```
### Navigate to http://127.0.0.1:5000/
