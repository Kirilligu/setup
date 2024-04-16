def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

triangle_area = calculate_triangle_area(3, 4, 5)
print("Площадь треугольника равна:", triangle_area)

