'''
Розсортуйте заданий лінійний масив по зростанню.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    N = randint(10, 20)     # визначаємо рандомно розмір масиву в межах від 10 до 20
    A = np.zeros(N, dtype=int)    # ініціалізуємо масив нулями розміром N
    for i in range(N):     # циклічно заповнюємо масив випадковими числами в межах від -10 до 10
        A[i] = randint(-10, 10)
    print(A)
    # використаємо алгоритм сортування бульбашкою
    n, i = len(A), 0
    flag = True   # вводимо змінну flag, щоб завершити цикл, коли не буле здійснено жодного обміну
    while flag:
        flag = False
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                flag = True
        i += 1
    print(A)

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break