'''
Введіть з клавіатури п'ять цілочисельних елементів масиву X.
Виведіть на екран значення коріння і квадратів кожного з елементів масиву.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
import math     # імпортуємо бібліотеку math для роботи з математичними функціями (корінь квадратний)
while True:
    X = np.zeros(5, dtype=int)  # ініціалізуємо одновимірний масив нулями розміром 5
    for i in range(5):  # циклічно заповнюємо масив елементами, отриманими з клавіатрури
        while True:
            try:  # перевіряємо, що користувач вводить лише цифри
                X[i] = int(input(f'X[{i + 1}] = '))
                break
            except ValueError:
                print('It is not a number. Try again')

    for i in range(5):  # циклічно виводимо значення для кожного елементу: квадратний корінь і ступінь в квадраті
        print(f'A[{i + 1}] sqrt({X[i]}) = {math.sqrt(X[i])}, {X[i]}**2 = {X[i] ** 2}')

    answer = input('Бажаєте продовжити (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break
