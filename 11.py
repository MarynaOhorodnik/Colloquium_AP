'''
Дані про температуру води на Чорноморському узбережжі за декаду вересня зберігаються в масиві.
Визначити, скільки за цей час було днів, придатних для купання.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
# придатна температура для купання 24 градуса та більше
# створюємо масив зі списку значень температури за декаду вересня (декада місяця - 10 днів)
T = np.array([25.3, 25.9, 25.2, 24.1, 23.9, 23.4, 24.5, 25.4, 24.3, 23.6])
count = 0     # вводимо змінну-лічильник для обрахунку днів, придатних для купання
for i in range(10):     # циклічно обхлдимо всі елементи маисву
    if T[i] >= 24:      # якщо температура придатна для купання, збільшуємо лічильник на одиницю
        count += 1

print(f'У декаді вересня було придатних днів для купання: {count}')
