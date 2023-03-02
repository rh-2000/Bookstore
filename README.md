# Bookstore software

This is a bookstore software solution that offers functions to search, update, delete, and enter book data to a database. The `bookstore.py` file contains the main functionality of the program and uses an SQLite database to store and retrieve book information.

## Table of Contents
- Usage
- Creating and Populating Table
- User Menu

## Usage
To use the bookstore software, simply run the `bookstore.py` file in your terminal or IDE. The program will present a menu of options for the user to select from. The user can enter books into the database, update existing book data, delete books from the database, or search for books based on title, author, or ID.

## Creating and Populating Table
The program first checks if a table called `books` exists in the database. If the table does not exist, it creates the table with the following columns:
- `id` (INTEGER PRIMARY KEY): a unique ID for each book
- `Title` (TEXT): the title of the book
- `Author` (TEXT): the author of the book
- `Qty` (INTEGER): the quantity of the book in stock

The program then inserts some sample data into the table, including the following books:
- A Tale of Two Cities by Charles Dickens
- Harry Potter and the Philosopher's Stone by J.K. Rowling
- The Lion, the Witch and the Wardrobe by C.S. Lewis
- The Lord of the Rings by J.R.R. Tolkien
- Alice in Wonderland by Lewis Carroll

## User Menu
The program presents the user with a menu of options to choose from:

1. Enter book: allows the user to add a new book to the database
2. Update book: allows the user to update an existing book's data
3. Delete book: allows the user to delete a book from the database
4. Search books: allows the user to search for books based on title, author, or ID
5. Exit: exits the program

The user can select an option by entering the corresponding number. The program will prompt the user for any necessary information and execute the selected action. The program will continue to present the menu until the user selects the "Exit" option.
