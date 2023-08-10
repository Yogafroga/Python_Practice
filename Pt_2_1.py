import random

colors = ["Red", "Blue", "Green", "Yellow", "Orange"]
selected_color = random.choice(colors)

while True:
    print("Choose a color from the following options:")
    for color in colors:
        print(color)

    user_color = input("Enter your choice: ")

    if user_color == selected_color:
        print("Отлично!")
        break
    else:
        print("Неверно! Попробуйте еще раз.")
        print("Подсказка: Название цвета на букву", selected_color[0])
