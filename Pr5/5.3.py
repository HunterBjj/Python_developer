rates = {'Sberbank': 55.8, 'VTB24': 53.91, 'MTS': 54, "TINKOFF": 59} 
min_rates = min(rates.values())

def get_key(rates, min_rates):
    for k, v in rates.items():
        if v == min_rates:
            return k


print(f"{get_key(rates,min_rates)} -> {min_rates}")