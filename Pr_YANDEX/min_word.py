"""
Дана последовательность слов
Вывести все самые короткие слова через пробел
"""

def min_words(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(words)
    ans = []
    for word in words:
        if len(word) == minlen:
            ans.append(word)
    return ' '. join(ans)