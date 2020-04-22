'''
Перетин даху має форму півкола з радіусом R м.
Сформувати таблицю, яка містить довжини опор, які встановлюються через кожні R / 5 м.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
import math     # імпортуємо бібліотеку math для роботии з математичними функціями
while True:
    while True:
        try:     # перевіряємо на правильність введенні дані
            R = int(input('R = '))    # отримуємо значення радіума від користувача
            break
        except ValueError:
            print('Це не число')
    interval = R / 5  # визначаємо через який інтервал будуть встановлютися опори
    k = interval     # змінну k будемо збільшувати на кожній ітерації для обрахунку довжин всіх опор
    N = int(2*R / interval - 1)   # визначаємо розмір масиву (кількість необхідних опор)
    A = np.zeros(N)  # ініціалізуємо масив нулями розміром N
    for i in range(N):  # циклічно заповнюємо масив, використовуючи теорему Піфагора
        A[i] = round(math.sqrt(R**2 - ((R - k)**2)), 2)
        k += interval    # збільшуємо k на одиницю, щоб обрахувти довжину наступної опори
    for j in range(N):    # циклічно виводимо усі значення
        print(f'{j + 1}. {A[j]}')

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break