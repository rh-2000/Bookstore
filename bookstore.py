import sqlite3
# creating a new database
db = sqlite3.connect('data/ebookstore')

cursor = db.cursor()


#  === CREATING & POPULATING TABLE ===

# implemented a check using .fetchall() if the database has already been populated from a previous run of the program
if cursor.execute('''SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'books';''').fetchall() == []:

    cursor.execute('''CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')
    db.commit()

    id1 = 3001
    title1 = 'A Tale of Two Cities'
    author1 = 'Charles Dickens'
    qty1 = 30

    id2 = 3002
    title2 = 'Harry Potter and the Philosopher`s stone'
    author2 = 'J.K. Rowling'
    qty2 = 40

    id3 = 3003
    title3 = 'The Lion, the Witch and the Wardrobe'
    author3 = 'C.S. Lewis'
    qty3 = 25

    id4 = 3004
    title4 = 'The Lord of the Rings'
    author4 = 'J.R.R. Tolkien'
    qty4 = 37

    id5 = 3005
    title5 = 'Alice in Wonderland'
    author5 = 'Lewis Carroll'
    qty5 = 12

    # inserting above data for each row/entry using dictionary method
    cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                        VALUES(:id,:Title,:Author,:Qty)''',
                        {'id':id1, 'Title':title1, 'Author':author1, 'Qty':qty1})
    print('Book 1 inserted.')


    cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                        VALUES(:id,:Title,:Author,:Qty)''',
                        {'id':id2, 'Title':title2, 'Author':author2, 'Qty':qty2})
    print('Book 2 inserted.')

    cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                        VALUES(:id,:Title,:Author,:Qty)''',
                        {'id':id3, 'Title':title3, 'Author':author3, 'Qty':qty3})
    print('Book 3 inserted.')

    cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                        VALUES(:id,:Title,:Author,:Qty)''',
                        {'id':id4, 'Title':title4, 'Author':author4, 'Qty':qty4})
    print('Book 4 inserted.')

    cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                        VALUES(:id,:Title,:Author,:Qty)''',
                        {'id':id5, 'Title':title5, 'Author':author5, 'Qty':qty5})
    print('Book 5 inserted.')

    db.commit()

elif cursor.execute('''SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'books';''').fetchall() != []:
    print('Table already populated')
    pass


#  === USER MENU ===

while True:
    menu = f'''\nPlease select from the following menu\n
    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    0. Exit'''
    menu_choice = int(input(f'''{menu}\nChoice: '''))

    # adding a new book using dict method
    if menu_choice == 1:
        # implementing some try/except blocks to check for value errors when entering int inputs
        while True:
            try:
                new_id = int(input('Enter the ID: '))
                break
            except ValueError:
                print('Invalid input. Enter using integers only.')
        new_title = input('Title: ')
        new_author = input('Author: ')
        while True:
            try:
                new_qty = int(input('Quantity: '))
                break
            except ValueError:
                print('Invalid input. Enter using integers only.')
        cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                    VALUES(:id,:Title,:Author,:Qty)''',
                    {'id':new_id, 'Title':new_title, 'Author':new_author, 'Qty':new_qty})
        print('Book added successfully.')
        db.commit()

    # updating an existing book
    elif menu_choice == 2:
        # searching for the book first using unique id
        # for each id check a counter has been implemented where an id match increases counter by 1
        # if counter == 0 by the end of the for loop iterations then the input id is invalid
        find_id = int(input('Enter the ID of the book you wish to view/access: '))
        book_found = 0
        cursor.execute('''SELECT id, Title, Author, Qty FROM books''')
        for row in cursor:
            if row[0] == find_id:
                print('\nBook selected: ID{0} {1}, {2} (Qty: {3})'.format(row[0], row[1], row[2], row[3]))
                book_found += 1
            # using a while loop and if/elif statements to check which data needs changed until user exits
            # id cannot be changed since this is a primary key which needs to remain constant for search purposes
                while True:
                    update_choice = int(input('''Which data would you like to update?
                                                1. Title
                                                2. Author
                                                3. Qty
                                                0. Nothing (exit)
                                                Choice: '''))
                    if update_choice == 1:
                        title_update = int(input('Enter new title: '))
                        cursor.execute('''UPDATE books SET Title = ? WHERE id = ?''', (title_update, find_id))
                        print('Title updated successfully.')
                        db.commit()
                    elif update_choice == 2:
                        author_update = int(input('Enter new author: '))
                        cursor.execute('''UPDATE books SET Author = ? WHERE id = ?''', (author_update, find_id))
                        print('Author updated successfully.')
                        db.commit()
                    elif update_choice == 3:
                        qty_update = int(input('Enter new quantity: '))
                        cursor.execute('''UPDATE books SET Qty = ? WHERE id = ?''', (qty_update, find_id))
                        print('Quantity updated successfully.')
                        db.commit()
                    elif update_choice == 0:
                        break
        if book_found == 0:
            print('Invalid ID.')

    # using id search again as a reference point for the row to be deleted
    elif menu_choice == 3:
        find_id = int(input('Enter the ID of the book you wish to view/access: '))
        book_found = 0
        cursor.execute('''SELECT id, Title, Author, Qty FROM books''')
        for row in cursor:
            if row[0] == find_id:
                print('\nBook selected: ID{0} {1}, {2} (Qty: {3})'.format(row[0], row[1], row[2], row[3]))
                book_found += 1
                delete_confirm = input('Delete this book? Y/N: ').upper()
                while True:
                    if delete_confirm == 'Y':
                        cursor.execute('''DELETE FROM books WHERE id = ?''', (find_id,))
                        print('Book has been deleted.')
                        db.commit()
                        break
                    elif delete_confirm == 'N':
                        print('Deletion has been cancelled.')
                        break
                    else:
                        print('Invalid response. Please only enter Y or N.')
                        delete_confirm = input('Delete this book? Y/N: ').upper()
                        continue
        if book_found == 0:
            print('Invalid ID.')

    # search for books using unique id
    elif menu_choice == 4:
        find_id = int(input('Enter the ID of the book you wish to view/access: '))
        book_found = 0
        cursor.execute('''SELECT id, Title, Author, Qty FROM books''')
        for row in cursor:
            if row[0] == find_id:
                print('\nBook selected: ID{0} {1}, {2} (Qty: {3})'.format(row[0], row[1], row[2], row[3]))
                book_found += 1
        if book_found == 0 :
            print('Invalid ID.')
    
    # exit menu
    elif menu_choice == 0:
        print('Exiting.')
        break