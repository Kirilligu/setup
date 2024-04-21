import math
def calculate_rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Длина и ширина должны быть неотрицательными.")
    return length * width

if __name__ == "__main__":
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    area = calculate_rectangle_area(length, width)
    print("Площадь прямоугольника с длиной", length, "и шириной", width, "равна", area)
