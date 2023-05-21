"""
Дана кодировка UTF-8.
Найти самый часто встречающий элемент, если несколько символов встречается одинаково часто, то вывести любой.
"""

text = list(input('Enter text '))


def count_char(text):
    count_char = {}

    for i in text:
        if i not in count_char:
            count_char[i] = 1
        else:
            count_char[i] += 1

    result = max(count_char.values())

    for i in count_char:
        if count_char[i] == result:
            char = i

    return char, result


result = count_char(text)
print(result)