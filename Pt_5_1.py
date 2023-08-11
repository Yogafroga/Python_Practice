import csv

data = [
    ['1', 'Martin Iden', 'Jack London', '1909'],
    ['2', 'The Witcher: The last wish', 'Andrzej Sapkowski', '1993'],
    ['3', 'The Lord of the Rings: Fellowship of'
          ' the Ring', 'John Ronald Reuel Tolkien', '1954'],
    ['4', 'Perfume: The Story of a Murderer', 'Patrick Suskind', '1985'],
    ['5', 'Sacred and Terrible Air', 'Robert Curwitz', '2013'],
    ['6', 'The Sea-Wolf', 'Jack London', '1904']
]

header = ['Номер книги', 'Название книги', 'Автор книги', 'Год выпуска книги']

with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    writer.writerows(data)
