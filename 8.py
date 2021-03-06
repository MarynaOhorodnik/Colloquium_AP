'''
Створіть цілочисельний масив А [1..15] за допомогою генераторавипадкових чисел з елементами від -15 до 30
і виведіть його на екран. Визначте найбільший елемент масиву і його індекс.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    A = np.zeros(15, dtype=int)  # ініціалізуємо одновимірний масив нулями розміром 15
    for i in range(15):  # циклічно заповнюємо масив випадковими числами в межах від -15 до 30
        A[i] = randint(-15, 30)
    max, index = A[0], 0  # вводимо зміні для визначення максимального елемента та його індексу
    # припускаємо, що перший елемент - максимальний
    for i in range(1, 15):
        if A[i] > max:  # якщо елемент масиву більший за максимальний, перезаписуємо максимальний елемент та його індекс
            max, index = A[i], i
    print(f'{A}\nмаксимальний елемент = {max}, індекс = {index}')  # виводимо масив, максимальний елемент та його індекс

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break
