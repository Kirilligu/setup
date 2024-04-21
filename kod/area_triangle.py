def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Get the side lengths from the user.
a = float(input("Введите длину a: "))
b = float(input("Введите длину b: "))
c = float(input("Введите длину c: "))

triangle_area = calculate_triangle_area(a, b, c)

print("Площадь треугольника равна:", triangle_area)
