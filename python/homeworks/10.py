from datetime import datetime


def process_row(row):
    processed_row = []
    
    date_obj = datetime.strptime(row[0], "%Y.%m.%d")
    processed_row.append(date_obj.strftime("%Y-%m-%d"))
    
    names = row[1].split('|')
    formatted_names = [name.split(' ')[-1] + ', ' + ''.join([n[0] + '.' for n in name.split(' ')[:-1]]) for name in names]
    sorted_names = sorted(formatted_names)
    processed_row.extend(sorted_names)

    sorted_emails = sorted([email.split('@')[0] for email in row[2].split('|')]) 
    formatted_emails = [email.split('[')[0] for email in sorted_emails] 
    processed_row.extend(formatted_emails)

    return processed_row


def main1(input_table):
    ret_list = [process_row(row) for row in input_table]

    transposed_table = list(map(list, zip(*ret_list)))
    transposed_table = sorted(transposed_table, key=lambda x: x[1].split(', ')[0])

    transposed_table.insert(3, transposed_table.pop(0))
    transposed_table.insert(2, transposed_table.pop(1))
    
    for i in range(len(transposed_table)):
        transposed_table[i] = list(reversed(transposed_table[i]))
    return transposed_table
def main(input_table):
    result = main1(input_table)
    transposed_data = list(map(list, zip(*result)))
    sorted_data = sorted(transposed_data, key=lambda x: x[2])
    transposed_data = list(map(list, zip(*sorted_data)))
    result=transposed_data
    result[-1] = [val.replace(',', '0') for val in result[-1]]
    result[-1] = [val.replace(' ', '') for val in result[-1]]
    return result

input_table = [['2001.10.01', 'Егор Р. Цуший|0.339', 'zusij58[at]yandex.ru'], ['1999.05.17', 'Леонид Ц. Чозугук|0.016', 'cozuguk99[at]rambler.ru'], ['2001.05.04', 'Савва И. Цидатич|0.850', 'zidatic93[at]gmail.com']]
#[
#     ['2001.12.21', 'Владимир Д. Фелов|0.079', 'vladimir94[at]yandex.ru'],
#     ['2002.02.01', 'Родион Ф. Согин|0.243', 'rodion30[at]rambler.ru'],
#     ['2000.09.17', 'Макар Е. Дочяк|0.696', 'makar65[at]yandex.ru'],
#     ['1999.01.06', 'Марк О. Гагев|0.656', 'gagev37[at]yandex.ru']
# ]

print(main(input_table))
