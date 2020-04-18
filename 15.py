'''
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву - 20.
Заповнення масиву здійснити випадковими числами від 100 до 200.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    A = np.zeros(20, dtype=int)    # ініціалізуємо масив нулями розміром 20
    for i in range(20):     # циклічно заповнюємо масив випадковими числами в межах від -10 до 10
        A[i] = randint(100, 200)
    print(A)
    sum = 0     # вводимо змінну для знаходження суми парних елементів
    for j in range(20):     # циклічно обходимо всі елементи масиву
        if A[j] % 2 == 0:   # перевірка на парність: якщо остача від ділення на 2 дорівнює нулю
            sum += A[j]     # додаємо елементи, що задовільняють умову
    print(f'Сума парних елементів = {sum}')

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break
