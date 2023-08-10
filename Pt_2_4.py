a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate discriminant
discriminant = b ** 2 - 4 * a * c

# Calculate square root of discriminant
if discriminant > 0:
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    print("Two real and distinct roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print("One real root:")
    print("Root:", root)
else:
    print("No real roots")
