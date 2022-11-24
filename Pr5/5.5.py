data = {'2017-03-01': '55', '2017-03-02': '53', '2017-03-03': '54', "T2017-03-04": '59'} 
input_data = input("Введите дату или число ")

def data_search(data,input_data):
    for v, k in data.items():
          if v == input_data:
            return v,k
    else:
        for v, k in data.items():
          if k == input_data:
            return v,k

print(data_search(data,input_data))
        