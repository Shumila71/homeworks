def main(input_table):
    # Транспонировать список данных
    transposed_data = list(map(list, zip(*input_table)))
    sorted_data = sorted(transposed_data, key=lambda x: x[2])
    transposed_data = list(map(list, zip(*sorted_data)))
    # Вернуть отсортированные данные
    return transposed_data

print(main([['2002-01-10', '2002-07-01', '2002-01-05'], ['Шузов, Г.В.', 'Кифев, Д.Ц.', 'Рецовин, Д.О.'], ['german94', 'david33', 'dmitrij79'], ['0.5510', '0.1530', '0.1700']]))