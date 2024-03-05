import itertools
import string
import random

# # 1.1
# '''
# stdin:4:1: W293 blank line contains whitespace
# stdin:4:5: W292 no newline at end of file
# if True:
#     print(1)
#     print(2)
# '''
#
# # 1
# '''
# stdin:2:2: E111 indentation is not a multiple of 4
# def main():
#  print(5)
# '''
# '''
# stdin:4:1: E122 continuation line missing indentation or outdented
# my_list = [
#     1,
#     2,
# 3
# ]
# '''
# '''
# stdin:2:5: E125 continuation line with same indent as next logical line
# if condition1 \
#     and condition2:
#     something()
# '''
#
# # 2
# '''
# stdin:1:10: E201 whitespace after '('
# function( arg1 , arg2 )
# '''
# '''
# stdin:2:14: E203 whitespace before ','
# list = [1 , 2 , 3]
# '''
# '''
# stdin:1:22: E202 whitespace before ')'
# if ( condition ):
#     something()
# '''
#
# # 3
# '''
# stdin:4:5: E301 expected 1 blank line, found 0
# class MyClass(object):
#     def func1():
#         pass
#     def func2():
#         pass
# '''
# '''
# stdin:3:1: E302 expected 2 blank lines, found 0
# def function():
#     return True
# def another_function():
#     return False
# '''
# '''
# stdin:6:1: E303 too many blank lines (3)
# def function():
#     return True
#
#
#
# def another_function():
#     return False
# '''
#
# # 4
# '''
# stdin:1:19: E401 multiple imports on one line
# import collections, os, sys
# '''
# '''
# stdin:5:1: E402 module level import not at top of file
# import locale
#
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
#
# import sys
# '''
#
# # 5
# '''
# stdin:1:80: E501 line too long (162 > 79 characters)
# print('Four score and seven years ago our fathers brought forth, upon this continent, a new nation, conceived in liberty, and dedicated to the proposition that ')
# '''
# '''
# stdin:1:60: E502 the backslash is redundant between brackets
# print('Four score and seven years ago our fathers brought '\
#       'forth, upon this continent, a new nation, conceived '\
#       'in liberty, and dedicated to the proposition that '\
#       '"all men are created equal."')
# '''
# # 2.1
# # print([0xfor _ in 'abc'])
#
# # 2.2
# a = 1
# b = 1
# c = 300000  # проверено в Python 3.11
# d = 300000
# print(a is b, c is d)
#
# a, b = 'py', 'py'
# c = ''.join(['p', 'y'])
# print(a is b, a == c, a is c)
#
# # 2.3
# i = 0
# b = 'much,code,wow'
# print(b.split(',')[i])
# # 2.4
# lst = ['a', 'b', 'c']
# lst += 'd'
# print(lst)
#
# # lst = lst + 'd' # Ошибка?!
# # Unexpected type(s): (str) Possible type(s): (list[str]) (list[_S])
# # print(lst)
# # lst += 42
# # TypeError: 'int' object is not iterable
# # print(lst) # Ошибка?!
#
# # 3.1
# s = ["1", "2", "3", "4", "5"]
# s = list(map(int, s))
# # 3.2
# print(f"Элементы:{len(set(s))}")
# # 3.3
# print(s[::-1])
# # 3.4
# x = 2
# print([i for i, value in enumerate(s) if value == x])
# # 3.5
# print(sum(s[i] for i in range(0, len(s), 2)))
# # 3.6
# print(max(['apple', 'banana', 'orange', 'strawberry'], key=len))
# # 3.7
# is_harshad = lambda number: number > 0 and number % sum(map(int, str(number))) == 0
# number_to_check = 18
# result = is_harshad(number_to_check)
# print(result)
# # 3.8
# print(''.join(random.choice(string.ascii_lowercase) for i in range(8)))
# 3.9
# rle_encode = lambda s: [(char, len(list(group))) for char, group in itertools.groupby(s)]
# result = rle_encode('ABBCCCDEF')
# print(result)


# 4.1

# def generate_groups():
#     groups = [f"ИКБО-{j}-{i}" for i in range(22, 24) for j in range(1, 31)]
#     return groups
#
#
# groups = generate_groups()
# print(groups)


# 4.2
# def decrypt(v, k):
#     v0, v1 = v
#     sum = 0xC6EF3720
#     delta = 0x9E3779B9
#     k0, k1, k2, k3 = k
#     for i in range(32):
#         v0 -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1)
#         v1 -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3)
#         sum -= delta
#     return [v0, v1]
#
#
# encrypted_message = [
#     0xE3238557, 0x6204A1F8, 0xE6537611, 0x174E5747,
#     0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,
#     0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF,
#     0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418,
#     0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,
#     0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7,
#     0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,
#     0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,
#     0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F,
#     0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637
# ]
# key = [0, 4, 5, 1]
#
# decrypted_message = []
# for i in range(0, len(encrypted_message), 2):
#     chunk = encrypted_message[i:i + 2]
#     decrypted_chunk = decrypt(chunk, key)
#     decrypted_message.extend(decrypted_chunk)
# for chunk in decrypted_message:
#     print(chunk, end=' ')


#5.1
#наивная
def ham_dist_naive(num1, num2):
    bin_str1 = bin(num1)[2:].zfill(max(len(bin(num1)), len(bin(num2))))
    bin_str2 = bin(num2)[2:].zfill(max(len(bin(num1)), len(bin(num2))))
    distance = sum(bit1 != bit2 for bit1, bit2 in zip(bin_str1, bin_str2))

    return distance

#однострочка
ham_dist_oneliner = lambda num1, num2: sum(bit1 != bit2 for bit1, bit2 in
                                           zip(bin(num1)[2:].zfill(max(len(bin(num1)), len(bin(num2)))),
                                               bin(num2)[2:].zfill(max(len(bin(num1)), len(bin(num2))))))
print(ham_dist_naive(0b10, 0b11))
print(ham_dist_naive(0b1100, 0b0011))

print(ham_dist_oneliner(0b10, 0b11))
print(ham_dist_oneliner(0b1100, 0b0011))

#5.2
def encode_val(repeat, n, value):
    bin_str = bin(value)[2:].zfill(8)
    encoded_str = ''.join(bin_str[i] * repeat for i in range(8))
    return int(encoded_str, 2)

def decode_val(repeat, n, encoded_value):
    encoded_str = bin(encoded_value)[2:].zfill(8 * repeat)
    decoded_str = ''.join(max(encoded_str[i:i+repeat], key=encoded_str[i:i+repeat].count) for i in range(0, 8 * repeat, repeat))
    return int(decoded_str, 2)

values = [815608, 2064837, 2093080, 2063879, 196608, 2067983,
          10457031, 1830912, 2067455, 2093116, 1044928, 2064407,
          6262776, 2027968, 4423680, 2068231, 2068474, 1999352,
          1019903, 2093113, 2068439, 2064455, 1831360, 1936903, 2067967, 2068456]
decoded_values = [decode_val(3, 8, val) for val in values]
print(decoded_values)

#5.3
from functools import cache

@cache
def lev_dist(a, b, i=None, j=None):
    if i is None:
        i = len(a)
    if j is None:
        j = len(b)

    if i == 0 or j == 0:
        return max(i, j)

    if a[i-1] == b[j-1]:
        return lev_dist(a, b, i-1, j-1)
    else:
        return 1 + min(
            lev_dist(a, b, i, j-1),
            lev_dist(a, b, i-1, j),
            lev_dist(a, b, i-1, j-1)
        )
result = lev_dist('столб', 'слон')
print(result)


#5.4
@cache
def lev_dist_ops(a, b, i=None, j=None):
    if i is None:
        i = len(a)
    if j is None:
        j = len(b)

    if i == 0 or j == 0:
        return max(i, j), []

    if a[i-1] == b[j-1]:
        dist, ops = lev_dist_ops(a, b, i-1, j-1)
        return dist, ops
    else:
        insert_dist, insert_ops = lev_dist_ops(a, b, i, j-1)
        delete_dist, delete_ops = lev_dist_ops(a, b, i-1, j)
        replace_dist, replace_ops = lev_dist_ops(a, b, i-1, j-1)

        min_dist = min(insert_dist, delete_dist, replace_dist)

        if min_dist == insert_dist:
            return 1 + insert_dist, insert_ops + ['вставка']
        elif min_dist == delete_dist:
            return 1 + delete_dist, delete_ops + ['удаление']
        else:
            return 1 + replace_dist, replace_ops + ['замена']

distance, operations = lev_dist_ops('столб', 'слон')
print(operations)

#6.1
def digital_economy_report_generator(data, paragraphs=3, sentences_per_paragraph=3):
    for _ in range(paragraphs):
        paragraph = ''
        for _ in range(sentences_per_paragraph):
            row = [random.choice(row) for row in data]
            paragraph += ' '.join(row) + ' '
        yield paragraph

import random

table_data = [
    ["Коллеги,", "В то же время,", "Однако,", "Тем не менее,", "Следовательно,", "Соответственно,", "Вместе с тем,", "С другой стороны,"],
    ["парадигма цифровой экономики", "контекст цифровой трансформации", "диджитализация бизнес-процессов", "прагматичный подход к цифровым платформам", "совокупность сквозных технологий", "программа прорывных исследований", "ускорение блокчейн-транзакций", "экспоненциальный рост Big Data"],
    ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски", "расширяет горизонты", "заставляет искать варианты", "не оставляет шанса для", "повышает вероятность", "обостряет проблему"],
    ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта", "компрометации конфиденциальных", "универсальной коммодитизации", "несанкционированной кастомизации", "нормативного регулирования", "практического применения"],
    ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.", "опасных экспериментов.", "государственно-частных партнёрств.", "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
]

report = digital_economy_report_generator(table_data)

for _ in range(3):
    print(next(report))

#6.2
import re

def sent_tokenize(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences

def word_tokenize(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return words

def generate_table(text):
    sentences = sent_tokenize(text)

    table_data = [word_tokenize(sentence) for sentence in sentences]

    return table_data

input_text = """
Коллеги, парадигма цифровой экономики открывает новые возможности для дальнейшего углубления знаний и компетенций. В то же время, контекст цифровой трансформации выдвигает новые требования бюджетного финансирования непроверенных гипотез. 
Однако, диджитализация бизнес-процессов несёт в себе риски синергетического эффекта волатильных активов. 
Тем не менее, прагматичный подход к цифровым платформам расширяет горизонты компрометации конфиденциальных опасных экспериментов. 
Следовательно, совокупность сквозных технологий заставляет искать варианты универсальной коммодитизации государственно-частных партнёрств. 
Соответственно, программа прорывных исследований не оставляет шанса для несанкционированной кастомизации цифровых следов граждан. 
Вместе с тем, ускорение блокчейн-транзакций повышает вероятность нормативного регулирования нежелательных последствий. 
С другой стороны, экспоненциальный рост Big Data обостряет проблему практического применения внезапных открытий.
"""


table_data = generate_table(input_text)


for row in table_data:
    print(row)

#6.3
import random

def generate_random_full_name():
    common_names = ["Данил", "Роман", "Лев", "Ильдар", "Николай", "Данила", "Семен", "Самир", "Тамерлан", "Святослав", "Герман", "Назар", "Степан", "Леонид"]
    first_name = random.choice(common_names)
    last_name = generate_random_last_name()
    patronymic_initial = random.choice("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЭЮЯ")
    full_name = f"{first_name} {patronymic_initial}. {last_name}"

    return full_name

def generate_random_last_name():
    last_names = ["Фуций", "Фецачли", "Шолодяк", "Тачасяк", "Мугодич", "Табян", "Черев", "Тифомский", "Гузянц", "Набян", "Семидяк", "Башко", "Кунарий", "Гидский", "Сабин"]

    return random.choice(last_names)

for _ in range(15):
    print(generate_random_full_name())

#6.4
def train_language_model(text, prefix_length):
    model = {}
    for i in range(len(text) - prefix_length):
        prefix = text[i:i + prefix_length]
        next_char = text[i + prefix_length]
        if prefix not in model:
            model[prefix] = {}
        if next_char not in model[prefix]:
            model[prefix][next_char] = 1
        else:
            model[prefix][next_char] += 1
    return model


def generate_text(model, prefix_length, length):
    start_index = random.randint(0, len(text) - prefix_length)
    current_prefix = text[start_index:start_index + prefix_length]
    generated_text = current_prefix

    for _ in range(length):
        if current_prefix not in model:
            break
        next_char = weighted_choice(model[current_prefix])
        generated_text += next_char
        current_prefix = current_prefix[1:] + next_char
        if current_prefix in model:
            print(f"{current_prefix}: {model[current_prefix]}")

    return generated_text


def weighted_choice(choices):
    total = sum(choices.values())
    threshold = random.uniform(0, total)
    cumulative_prob = 0
    for choice, freq in choices.items():
        cumulative_prob += freq
        if cumulative_prob > threshold:
            return choice

text = "На дворе трава, на траве дрова"
prefix_length = 3
model = train_language_model(text, prefix_length)

generated_text = generate_text(model, prefix_length, 100)
print(generated_text)
