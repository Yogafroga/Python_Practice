distance = float(input("Сколько километров хотите проехать на автомобиле? "))
fuelconsumption = float(input("Сколько литров топлива расходует автомобиль на 100 километров? "))
tankcapacity = float(input("Сколько литров топлива в вашем баке? "))

fuelneeded = (distance/100) * fuelconsumption

if fuelneeded <= tankcapacity:
    print("Вы сможете проехать желаемое расстояние.")
else:
    print("Вы не сможете проехать желаемое расстояние.")
