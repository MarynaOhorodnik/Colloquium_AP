'''
Дано лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по спаданню.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
from random import randint     # імпортуємо функцію randint() для генерування випадкових чисел
while True:
    N = randint(5, 10)     # визначаємо рандомно розмір масиву в межах від 5 до 10
    A = np.zeros(N, dtype=int)    # ініціалізуємо масив нулями розміром N
    for i in range(N):     # циклічно заповнюємо масив випадковими числами в межах від 0 до 5
        A[i] = randint(0, 5)
    print(A)
    flag = True    # вводимо змінну flag, для визначення упорядкованості масиву
    for i in range(1, N):     # циклічно обходимо всі елементи масиву, починаючи не з нульового, а першого
        if A[i - 1] < A[i]:  # якщо поточний і попередній елемент будуть заперечувати умову спадання
            flag = False     # змінюємо flag на False
            break            # виходимо з циклу
    # виводимо результат, враховуючи змінну flag
    print(f'Масив упорядкований по спаданню' if flag == True else f'Масив неупорядкований по спаданню')

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break