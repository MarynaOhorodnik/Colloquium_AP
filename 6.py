'''
Створіть масив А [1..8] за допомогою генератора випадкових чисел з елементами від -10 до 10 і виведіть його на екран.
Підрахуйте кількість від’ємних елементів масиву.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    A = np.zeros(8, dtype=int)  # ініціалізуємо одновимірний масив нулями розміром 8
    count = 0  # вводимо змінну-лічильник для обрахунку від'ємних елементів
    for i in range(8):  # циклічно заповнюємо масив випадковими числами в межах від -10 до 10
        A[i] = randint(-10, 10)
        if A[i] < 0:
            count += 1  # збільлшуємо на одиницю, якщо знайдено від'ємний елемент

    print(f'{A}\nВід`ємних елементів в масиві: {count}')  # виводимо масив і кількість від'ємних елементів

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break
