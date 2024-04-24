import hypothesis.strategies as st
from hypothesis import given
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
# Определяем стратегию для генерации целых чисел
coordinates = st.integers()

# Задаем стратегию для генерации набора параметров (x1, y1, x2, y2)
coordinates_sets = st.tuples(coordinates, coordinates, coordinates, coordinates)

# Используем декоратор @given для указания стратегии генерации данных
@given(coordinates_sets)
def test_distance(coordinates):
    x1, y1, x2, y2 = coordinates
    assert distance(x1, y1, x2, y2) == ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Запускаем тесты
test_distance()