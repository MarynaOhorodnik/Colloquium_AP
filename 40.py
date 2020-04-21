'''
Обчислити суму парних елементів одновимірного масиву до першого зустрінутого нульового елемента.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    N = randint(10, 20)     # визначаємо рандомно розмір масиву в межах від 10 до 20
    A = np.zeros(N, dtype=int)    # ініціалізуємо масив нулями розміром N
    for i in range(N):     # циклічно заповнюємо масив випадковими числами в межах від -5 до 5
        A[i] = randint(-5, 5)
    print(A)
    sum_val = 0     # вводимо зміну sum_val для обрахунку суми парних елементів
    for i in range(N):     # циклічно обходимо всі елементи масиву
        if A[i] == 0:   # первіряємо, чи елемент дорівнює 0
            break       # якщо умова спрацювала, виходимо з циклу
        if A[i] % 2 == 0:     # якщо перша умова не спрацювала, то перевіряємо, чи елемент є парним
            sum_val += A[i]   # додаємо елемент, який задовільняє умову, в змінну sum_val
    print(f'Сума парних елементів до першого зустрінутого нульового елемента: {sum_val}')

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break