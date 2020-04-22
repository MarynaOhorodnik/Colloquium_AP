'''
Змінній t привласнити значення істина, якщо максимальний елемент одновимірного масиву єдиний і не перевищує наперед
заданого числа а.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    a = randint(5, 10)  # визначаємо рандомно число а
    N = randint(10, 20)   # визначаємо рандомно розмір масиву в межах від 10 до 20
    A = np.zeros(N, dtype=int)  # ініціалізуємо масив нулями розміром N
    for i in range(N):  # циклічно заповнюємо масив випадковими числами в межах від -10 до 10
        A[i] = randint(-10, 10)
    print(A)
    # вводимо змінну t, значення якої буде змінюватися, якщо максимальний елемент єдиний і не перевищує число а
    t = False
    # вводимо зміну max_val для визначення максимального елемента в масиві за допомогою функції max()
    # вводимо зміну count для обрахунку кількості максимальних елементів
    max_val, count = max(A), 0
    for j in range(N):    # циклічно обходимо всі елементи масиву
        if A[j] == max_val:   # первіряємо, чи відповідає максимальному значенню елемент
            count += 1     # якщо значення елементу задовільняє умову, збільшуємо count на одиницю
    if count == 1 and max_val < a:   # перевіряємо умову задачі
        t = True     # якщо умова спрацювала, то змінюємо t на True
    print(f'Максимальний елемент масиву {max_val} єдиний і не перевищує число {a}: {t}')

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break