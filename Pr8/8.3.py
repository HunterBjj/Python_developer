"""
3. Рефакторинг.
Дано: неоптимальный код.
Задание: оптимизировать следующий код.

Для того, чтобы проверить время выполнения до рефакторинга и после, расскоментируйте код, который представлен ниже
"""
import time
start_time = time.perf_counter()
sentences = ['капитан джек воробей, капитан дальнего плавания,ваша лодка готова, капитан']
sentences_split = sentences.split()
sentences_count = sentences_split.count()
print(sentences_count.count('капитан'))
end_time = time.perf_counter()
print(f"Время после рефакторинга: {end_time - start_time:.8f} seconds")
#Итератор хранит только указатель на следующий элемент,мы всегда храним только один элемент в памяти, а не всю коллекцию, поэтому использовать генератор в данном случаи быстрее быстрее
start_time1 = time.perf_counter()

cap_count1 = 0
for sentence in sentences:
    cap_count1 += sentence.count('капитан')

print(cap_count1)
end_time1 = time.perf_counter()
print(f" Время до рефакторинга: {end_time1 - start_time1:.8f} seconds")

