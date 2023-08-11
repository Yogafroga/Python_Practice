import csv

author = input('Введите имя автора: ')

with open('books.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    books = []
    for row in reader:
        if len(row) >= 3 and row[2] == author:
            books.append(row[1])

    if len(books) == 0:
        print('В списке нет книг этого автора.')
    else:
        print('Книги автора', author + ':')
        for book in books:
            print(book)
