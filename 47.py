'''
У лінійному масиві знайти максимальний елемент. Вставте порядковий номер елемента за ним,
пересунувши всі залишилися на одну позицію вправо.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    N = randint(10, 20)   # визначаємо рандомно розмір масиву в межах від 10 до 20
    A = np.zeros(N, dtype=int)  # ініціалізуємо масив нулями розміром N
    for i in range(N):  # циклічно заповнюємо масив випадковими числами в межах від -20 до 20
        A[i] = randint(-20, 20)
    print(A)
    # вводимо зміну max_val для визначення максимального елемента в масиві за допомогою функції max()
    # вводимо зміну max_index для запису індексу знайденого максимального елемента в масиві
    max_val, max_index = max(A), 0
    for j in range(N):    # циклічно обходимо всі елементи масиву
        if A[j] == max_val:   # якщо знайдено максимальний елемент
            max_index = j     # то в змінну max_index записуємо індекс максимального елемента
            A[j + 1], val = max_index, A[j + 1]  # замінюємо наступний елемент номером максимального елемента
            A.resize(N + 1)     # збільшуємо розмір масиву на один, щоб можна було перезаписати усі елементи (вправо)
            for i in range(j + 2, N + 1):  # перезаписуємо циклічно усі елементи на одну позицію вправо
                A[i], val = val, A[i]
            break  # виходимо з циклу
    print(A)

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break