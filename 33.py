'''
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    N = randint(10, 20)     # визначаємо рандомно розмір масиву в межах від 10 до 20
    A = np.zeros(N, dtype=int)    # ініціалізуємо масив нулями розміром N
    for i in range(N):     # циклічно заповнюємо масив випадковими числами в межах від 0 до 5
        A[i] = randint(0, 5)
    print(A)
    prod = 1     # вводимо зміну prod для обрахунку добутку ненульових елементів
    for i in range(N):     # циклічно обходимо всі елементи масиву і перевіряємо чи є ненульовим
        if A[i] != 0:
            prod *= A[i]     # домножуємо елемент, який задовільняє умову, в змінну prod
    print(f'Добуток всіх ненульових елементів масиву: {prod}')

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break