def arab(num):
    x = ''
    arab = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    for key, value in arab.items():
        x += num // key * value
        num %= key
    return x
num = int(input("Введите число"))
print(arab(num))
