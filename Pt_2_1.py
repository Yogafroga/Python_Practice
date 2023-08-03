import random

colors = ["Красный", "Синий", "Зеленый", "Желтый", "Фиолетовый"]
selected_color = random.choice(colors)

while True:
    print("Выберите один из цветов ниже:")
    for color in colors:
        print(color)

    user_color = input("Введите выбранный цвет: ")

    if user_color == selected_color:
        print("Отлично!")
        break
    else:
        print("Неверно! Попробуйте еще раз.")
        print("Подсказка: Название цвета начинается на букву", selected_color[0])
