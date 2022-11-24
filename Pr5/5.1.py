txt = input("Введите текст ")
char_txt = list(txt)
spisok = {}
for i in range(len(txt)):
    symbol = txt.count(char_txt[i])
    spisok[txt[i]] = symbol
    
print(spisok)
