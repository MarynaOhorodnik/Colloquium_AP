'''
Змінній t привласнити значення істина, якщо в одновимірному масиві є хоча б одне від’ємне і парне число.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    N = randint(10, 20)     # визначаємо рандомно розмір масиву в межах від 10 до 20
    A = np.zeros(N, dtype=int)    # ініціалізуємо масив нулями розміром N
    for i in range(N):     # циклічно заповнюємо масив випадковими числами в межах від -20 до 20
        A[i] = randint(-20, 20)
    print(A)
    t = False  # вводимо змінну t, значення якої буде змінюватися, якщо знайдеться хоча б одне від’ємне і парне число
    for i in range(N):     # циклічно обходимо всі елементи масиву і перевіряємо чи є елемент від'ємним і парним
        if A[i] < 0 and A[i] % 2 == 0:
            t = True     # якщо елемент задовільняє умову, змінюємо значення змінної t на True
    print(t)

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break