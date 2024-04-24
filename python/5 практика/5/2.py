import hypothesis.strategies as st
from hypothesis import given
def encode_rle(data):
    def _encode_single(char, count):
        return bytes([char, count])

    encoded = bytes()
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded += _encode_single(data[i - 1], count)
            count = 1
    encoded += _encode_single(data[-1], count)
    return encoded

def decode_rle(data):
    decoded = bytes()
    i = 1
    while i < len(data):
        count = data[i]
        char = data[i - 1]
        decoded += bytes([char] * count)
        i += 5
    return decoded

# Определяем стратегию для генерации случайной последовательности байтов
byte_sequence = st.binary(min_size=1)

# Тестирование функции encode_rle
@given(byte_sequence)
def test_encode_rle(data):
    encoded_data = encode_rle(data)
    assert len(encoded_data) % 2 == 0  # Проверяем, что длина закодированной последовательности четная

# Тестирование функции decode_rle
@given(byte_sequence)
def test_decode_rle(data):
    encoded_data = encode_rle(data)
    decoded_data = decode_rle(encoded_data)
    assert len(decoded_data) == len(data)  # Проверяем, что длина декодированной последовательности равна исходной

    # Проверяем, что декодированная последовательность совпадает с исходной
    assert decoded_data == data

# Запуск тестов
if __name__ == "__main__":
    test_encode_rle()
    test_decode_rle()
