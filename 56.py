'''
Якщо в одновимірному масиві є три поспіль однакових елемента, то змінній r привласнити значення істина.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    N = randint(10, 20)   # визначаємо рандомно розмір масиву в межах від 10 до 20
    A = np.zeros(N, dtype=int)  # ініціалізуємо масив нулями розміром N
    for i in range(N):  # циклічно заповнюємо масив випадковими числами в межах від 0 до 5
        A[i] = randint(0, 5)
    print(A)
    r = False  # вводимо змінну r, значення якої буде змінюватися, якщо є три поспіль однакових елемента
    for i in range(1, N - 1):    # циклічно обходимо всі елементи масиву
        if A[i - 1] == A[i] == A[i + 1]:   # перевіряємо, чи елемент збігаються з попереднім та наступним елементом
            r = True     # якщо умова спрацювала, то змінюємо r на True
            break     # виходимо з циклу
    print(f'У масиві є три поспіль однакових елемента: {r}')

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break