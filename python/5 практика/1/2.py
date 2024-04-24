import random

def testBucketsort():
    # Тест случай 1: Пустой массив
    arr = []
    sorted_arr = bucketsort(arr, 10)
    assert sorted_arr == []

    # Тест случай 2: Один элемент
    arr = [5]
    sorted_arr = bucketsort(arr, 10)
    assert sorted_arr == [5]

    # Тест случай 3: Уже отсортированный массив
    arr = [1, 2, 3, 4, 5]
    sorted_arr = bucketsort(arr, 10)
    assert sorted_arr == [1, 2, 3, 4, 5]

    # Тест случай 4: Массив отсортирован в обратном порядке
    arr = [5, 4, 3, 2, 1]
    sorted_arr = bucketsort(arr, 10)
    assert sorted_arr == [1, 2, 3, 4, 5]

    # Тест случай 5: Случайный массив
    arr = [random.randint(0, 100) for _ in range(100)]
    sorted_arr = bucketsort(arr, 101)
    assert sorted_arr == sorted(arr)

    # Тест случай 6: Случайный массив с повторяющимися элементами
    arr = [random.randint(0, 10) for _ in range(100)]
    sorted_arr = bucketsort(arr, 11)
    assert sorted_arr == sorted(arr)

    print("Тесты пройдены!")

def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

testBucketsort()