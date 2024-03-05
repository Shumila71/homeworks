
#2.2
# a = 1
# b = 1
# c = 300000 # проверено в Python 3.11
# d = 300000
# print(a is b, c is d) A B - хранятся в 1 ячейке памяти, c d - в разных
# True False
# a, b = 'py', 'py'
# c = ''.join(['p', 'y'])
# print(a is b, a == c, a is c) A B хранятся в 1 ячейке, равенство по значению, с - новая ячейка изза join

#2.3
# i = 0
# b = 'much','code','wow'
# print(b.split(',')[i])



#2.4
# lst = ['a', 'b', 'c']
# lst += 'd' #расширение списка 
# print(lst)

# lst = lst + 'd' # Ошибка?! Сложение списка и стр
# print(lst)

# lst += 42
# print(lst) # Ошибка?! Добавление в список числа нельзя

import random
import string
import itertools
# #3.1
# s = ['1', '2', '3', '4', '5']
# s = list(map(int, s))
# print(s)
# #3.2
# s = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# unique_count = len(set(s))
# print(unique_count)
# #3.3
# s = [1, 2, 3, 4, 5]
# s.reverse()
# print(s)
# #3.4
# s = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# x = 3
# indices = [i for i, item in enumerate(s) if item == x]
# print(indices)
# #3.5
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = sum(s[::2])
# print(result)
# #3.6
# s = ['apple', 'banana', 'orange', 'strawberry']
# longest_string = max(s, key=len)
# print(longest_string)
# #3.7
# num = 18
# is_harshad = num % sum(int(digit) for digit in str(num)) == 0
# print(is_harshad)
# #3.8
# max_length = 100
# random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=max_length))
# print(random_string)
# #3.9
# rle_encode = lambda s: [(char, len(list(group))) for char, group in itertools.groupby(s)]
# result = rle_encode('ABBCCCDEF')
# print(result)


# def generate_groups():
#     groups = [f"ИКБО-{j}-{i}" for i in range(22, 24) for j in range(1,31)]
#     return groups
# groups = generate_groups()
# print(groups)

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

# decrypted_message = []
# for i in range(0, len(encrypted_message), 2):
#     chunk = encrypted_message[i:i+2]
#     decrypted_chunk = decrypt(chunk, key)
#     decrypted_message.extend(decrypted_chunk)
# for chunk in decrypted_message:
#     print(hex(chunk), end=' ')



# #5.1
# def ham_dist(num1, num2):
#     return bin(num1 ^ num2).count('1')
# print(ham_dist(0b1100, 0b0011))

# #5.2
# def encode_val(repeat, length, value):
#     encoded_value = 0
#     for i in range(length):
#         bit = (value >> i) & 1
#         encoded_value |= (bit << (i * repeat))
#     return encoded_value

# def decode_val(repeat, length, encoded_value):
#     decoded_value = 0
#     for i in range(length):
#         decoded_value |= ((encoded_value >> (i * repeat)) & 1) << i
#     return decoded_value

# def correct_errors(repeat, length, values):
#     corrected_values = []
#     for value in values:
#         corrected_values.append(decode_val(repeat, length, value))
#     return corrected_values

# encoded_values = [
#     815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912,
#     2067455, 2093116, 1044928, 2064407, 6262776, 2027968, 4423680, 2068231,
#     2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903,
#     2067967, 2068456
# ]

# corrected_values = correct_errors(3, 8, encoded_values)

# for value in corrected_values:
#     print(bin(value))
    
    


# #5.3
# from functools import cache
# @cache
# def lev_dist(s1, s2):
#     if not s1:
#         return len(s2)
#     if not s2:
#         return len(s1)
#     if s1[-1] == s2[-1]:
#         cost = 0
#     else:
#         cost = 1
#     return min(
#         lev_dist(s1[:-1], s2) + 1,
#         lev_dist(s1, s2[:-1]) + 1,
#         lev_dist(s1[:-1], s2[:-1]) + cost
#     )
# print(lev_dist('столб', 'слон')) 

# #5.4
# @cache
# def lev_dist_ops(a, b, i=None, j=None):
#     if i is None:
#         i = len(a)
#     if j is None:
#         j = len(b)

#     if i == 0 or j == 0:
#         return max(i, j), []

#     if a[i-1] == b[j-1]:
#         dist, ops = lev_dist_ops(a, b, i-1, j-1)
#         return dist, ops
#     else:
#         insert_dist, insert_ops = lev_dist_ops(a, b, i, j-1)
#         delete_dist, delete_ops = lev_dist_ops(a, b, i-1, j)
#         replace_dist, replace_ops = lev_dist_ops(a, b, i-1, j-1)

#         min_dist = min(insert_dist, delete_dist, replace_dist)

#         if min_dist == insert_dist:
#             return 1 + insert_dist, insert_ops + ['вставка']
#         elif min_dist == delete_dist:
#             return 1 + delete_dist, delete_ops + ['удаление']
#         else:
#             return 1 + replace_dist, replace_ops + ['замена']

# distance, operations = lev_dist_ops('столб', 'слон')
# print(operations)

# #5.6
# from collections import Counter
# from functools import cache

# def load_dictionary(file_path):
#     dictionary = {}
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             word, frequency = line.strip().split()
#             dictionary[word] = int(frequency)
#     return dictionary

# file_path = 'd:\code\_4\python\words.txt'
# dictionary = load_dictionary(file_path)

# @cache

# def lev_dist(s1, s2):
#     if not s1:
#         return len(s2)
#     if not s2:
#         return len(s1)

#     cost = 0 if s1[-1] == s2[-1] else 1

#     return min(lev_dist(s1[:-1], s2) + 1,
#                lev_dist(s1, s2[:-1]) + 1,
#                lev_dist(s1[:-1], s2[:-1]) + cost)


# def spell(word):
#     if word in dictionary:
#         return word

#     similar_words_lev1 = [w for w in dictionary if lev_dist(w, word) == 1]
#     if similar_words_lev1:
#         most_popular_lev1 = max(similar_words_lev1, key=lambda x: dictionary[x])
#         return most_popular_lev1

#     similar_words_lev2 = [w for w in dictionary if lev_dist(w, word) == 2]
#     if similar_words_lev2:
#         most_popular_lev2 = max(similar_words_lev2, key=lambda x: dictionary[x])
#         return most_popular_lev2

#     return word
# text = 'каравэлла убижала в бурлин'
# corrected_text = ' '.join(spell(word) for word in text.split())
# print(corrected_text)

#5.7
# from collections import Counter
# from functools import cache

# # Замены английских букв на русские и перестановки пар соседних символов
# transpositions = {
#     'a': 'а',
#     'c': 'с',
#     'e': 'е',
#     'o': 'о',
#     'p': 'р',
#     'x': 'х',
#     'y': 'у',
#     'k': 'к'
# }

# def load_dictionary(file_path):
#     dictionary = {}
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             word, frequency = line.strip().split()
#             dictionary[word] = int(frequency)
#     return dictionary

# file_path = 'd:\code\_4\python\words.txt'
# dictionary = load_dictionary(file_path)

# @cache
# def lev_dist(s1, s2):
#     if not s1:
#         return len(s2)
#     if not s2:
#         return len(s1)

#     # Учитываем замены и перестановки
#     cost = 0 if s1[-1] == s2[-1] or s1[-1] in transpositions and transpositions[s1[-1]] == s2[-1] else 1

#     return min(lev_dist(s1[:-1], s2) + 1,
#                lev_dist(s1, s2[:-1]) + 1,
#                lev_dist(s1[:-1], s2[:-1]) + cost)


# def spell(word):
#     if word in dictionary:
#         return word

#     similar_words_lev1 = [w for w in dictionary if lev_dist(w, word) == 1]
#     if similar_words_lev1:
#         most_popular_lev1 = max(similar_words_lev1, key=lambda x: dictionary[x])
#         return most_popular_lev1

#     similar_words_lev2 = [w for w in dictionary if lev_dist(w, word) == 2]
#     if similar_words_lev2:
#         most_popular_lev2 = max(similar_words_lev2, key=lambda x: dictionary[x])
#         return most_popular_lev2

#     return word

# text = 'каравэлла убижала в бурлин'
# corrected_text = ' '.join(spell(word) for word in text.split())
# print(corrected_text)


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


#7.1-7.2
class Labyrinth:
    def __init__(self, filename='d:\code\_4\python\labirint.txt'):
        self.rooms = []
        with open(filename, 'r') as file:
            while True:
                data = file.readline().rstrip().split()
                if data[0] == '0':
                    break
                room_data = list(map(int, data))
                self.rooms.append(Room(room_data[0], *room_data[1:]))


class Room:
    def __init__(self, num, *paths):
        self.num = num
        self.paths = paths


def run(labyrinth):
    directions = ['Север', 'Запад', 'Юг', 'Восток']
    current_room = labyrinth.rooms[0]
    print('Начало лабиринта. Вы в начале лабиринта. Сможете из него выбраться?')
    while True:
        print(f'\nКомната №{current_room.num}\nВы находитесь в комнате №{current_room.num}')
        print("1 проход на Север\n2 проход на Запад\n3 проход на Юг\n4 проход на Восток")
        valid_choices = [index for index, path in enumerate(current_room.paths) if path != -1]
        try:
            user_choice = int(input('Выберите направление: ')) - 1
            if user_choice in valid_choices:
                next_room_index = current_room.paths[user_choice]
                if next_room_index == 0:
                    print('Поздравляю, победа!')
                    break
                current_room = labyrinth.rooms[next_room_index - 1]
            else:
                print('Некорректный выбор. Попробуйте еще раз.')
        except ValueError:
            print('Ошибка. Введите число.')

if __name__ == '__main__':
    lab = Labyrinth()
    run(lab)
