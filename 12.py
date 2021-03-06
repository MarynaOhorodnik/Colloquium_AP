'''
Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
# створюємо масив зі списку значень температури за декаду вересня (декада місяця - 10 днів)
T = np.array([2, 5, 3, 6, 9, 7, 8, 3, 0, -2])
middle = sum(T) / 10     # знаходимо середню температуру за декаду грудня ()сумуємо всі елементи і ділимо на 10
count = 0     # вводимо змінну-лічильник для обрахунку разів, коли температура була вище середньою за цю декаду
for i in range(10):     # циклічно обходимо всі елементи масиву
    if T[i] > middle:   # якщо значення елементу більше за середнє, то збільшуємо лічильник на одиницю
        count += 1

print(f'Кількість разів, коли температура була вище середньої за декаду грудня: {count}')
