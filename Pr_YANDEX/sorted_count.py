"""
Дана кодировка UTF-8.
Найти самый часто встречающий элемент, если несколько символов встречается одинаково часто, то вывести любой.
"""
text = list(input('Enter text '))


def count_char(text):
    count_char = {}
    max_num = 0
    for i in text:
        if i not in count_char:
            count_char[i] = 1
        else:
            count_char[i] += 1
        if count_char[i] > max_num:
            char = i
    num_max = max(count_char.values())
    return char, num_max


result = count_char(text)
print(f'{result:}')