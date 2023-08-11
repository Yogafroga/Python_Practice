import csv

start_year = input('Введите начальный год: ')
end_year = input('Введите конечный год: ')

try:
    start_year = int(start_year)
    end_year = int(end_year)
except ValueError:
    print('Некорректный запрос.')
    exit()

if start_year > end_year:
    print('Некорректный запрос.')
    exit()

with open('books.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    books = []
    for row in reader:
        year = int(row[3])
        if start_year <= year <= end_year:
            books.append(row[1])

    if len(books) == 0:
        print('В заданном промежутке времени нет выпущенных книг.')
    else:
        print('Книги, выпущенные c', start_year, 'по', end_year, ':')
        for book in books:
            print(book)
