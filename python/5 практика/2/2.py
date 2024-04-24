def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Получаем координаты точек от пользователя
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

# Вызываем функцию и выводим результат
result = distance(x1, y1, x2, y2)
print("Расстояние между точками:", result)