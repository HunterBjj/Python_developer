rates = {'Sberbank': 55.8, 'VTB24': 53.91, 'MTS': 54, "TINKOFF": 59} 
min_rates = min(rates.values())

def reverse_key(rates):
    rates = dict(zip(rates.values(), rates.keys())) # zip функция берёт на вход несколько списков и создаёт из них список, Словарь (dict) — одна из таких структур, которая хранит данные в формате пар ключ-значение.
    return rates.items()


print(reverse_key(rates))
        