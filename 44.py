'''
Підрахуйте кількість елементів одновимірного масиву, які збігаються зі своїм номером і при цьому кратні 3.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    N = randint(10, 20)   # визначаємо рандомно розмір масиву в межах від 10 до 20
    A = np.zeros(N, dtype=int)  # ініціалізуємо масив нулями розміром N
    for i in range(N):  # циклічно заповнюємо масив випадковими числами в межах від 0 до 20
        A[i] = randint(0, 20)
    print(A)
    count = 0   # вводимо зміну count для обрахунку кількості елементів, які збігаються зі своїм номером і кратні 3
    for j in range(N):    # циклічно обходимо всі елементи масиву
        if A[j] == j and A[j] % 3 == 0:   # перевіряємо, чи елемент збігаються зі своїм номером і кратний 3
            count += 1     # якщо значення елементу задовільняє умову, збільшуємо count на одиницю
    print(f'Кількість елементів, які збігаються зі своїм номером і при цьому кратні 3: {count}')

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break