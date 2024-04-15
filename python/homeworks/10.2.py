def main(x):
    x = [el for i, el in enumerate(x) if el not in x[:i] and el != [None]* 4]
    ans = [[], [], []]
    for el in x:
        ans[0].append(el[0].lower())
        second = el[1].split(":")
        second[0] = second[0].replace(".", "/")
        second[1] = second[1][second[1].find(" ") + 1:] + " " + second[1][:2]
        ans[1].append(second[0])
        ans[2].append(second[1])
        return ans


# from datetime import datetime


# def process_row(row):
#     processed_row = []
    
#     date_obj = datetime.strptime(row[0], "%Y.%m.%d")
#     processed_row.append(date_obj.strftime("%Y-%m-%d"))
    
#     names = row[1].split('|')
#     sorted_names = sorted(names, key=lambda name: name.split(' ')[-1])
#     formatted_names = [name.split(' ')[-1] + ', ' + ''.join([n[0] + '.' for n in name.split(' ')[:-1]]) for name in sorted_names]
#     processed_row.extend(formatted_names)

#     sorted_emails = sorted(row[2].split('|'), key=lambda email: email.split('@')[0])
#     formatted_emails = [email.split('[')[0] for email in sorted_emails] 
#     processed_row.extend(formatted_emails)

#     return processed_row


# def transpose_table(table):
#     transposed_data = []
#     for i in range(len(table[0])):
#         transposed_data.append([row[i] for row in table])
#     return transposed_data


# def sort_table(table, column_index):
#     sorted_table = sorted(table, key=lambda x: x[column_index])
#     return sorted_table


# def replace_commas_and_spaces(table):
#     table[-1] = [val.replace(',', '0').replace(' ', '') for val in table[-1]]
#     return table


# def main(input_table):
#     processed_table = [process_row(row) for row in input_table]
    
#     sorted_table = sort_table(processed_table, 3)
    
#     replaced_table= transpose_table(sorted_table)
    
#     replaced_table = list(map(list, zip(*sorted_table)))
#     replaced_table.insert(3, replaced_table.pop(1))
#     replaced_table[-1] = [val.replace(',', '0') for val in replaced_table[-1]]
#     replaced_table[-1] = [val.replace(' ', '') for val in replaced_table[-1]]
#     return replaced_table



input_table = [['2001.10.01', 'Егор Р. Цуший|0.339', 'zusij58[at]yandex.ru'], ['1999.05.17', 'Леонид Ц. Чозугук|0.016', 'cozuguk99[at]rambler.ru'], ['2001.05.04', 'Савва И. Цидатич|0.850', 'zidatic93[at]gmail.com']]
#[
#     ['2001.12.21', 'Владимир Д. Фелов|0.079', 'vladimir94[at]yandex.ru'],
#     ['2002.02.01', 'Родион Ф. Согин|0.243', 'rodion30[at]rambler.ru'],
#     ['2000.09.17', 'Макар Е. Дочяк|0.696', 'makar65[at]yandex.ru'],
#     ['1999.01.06', 'Марк О. Гагев|0.656', 'gagev37[at]yandex.ru']
# ]

print(main(input_table))