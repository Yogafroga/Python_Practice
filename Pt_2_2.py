shows = ("Show 1", "Show 2", "Show 3", "Show 4")
shows = list(shows)
print("Current shows:")
for show in shows:
    print(show)

newshow = input("Enter the name of a new show: ")
position = int(input("Enter the position of the show (1 to 5): "))

shows.insert(position - 1, newshow)
shows = tuple(shows)
print("Updated shows:")
for show in shows:
    print(show)
