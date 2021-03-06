'''
Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте місцями прізвища брокерів: першого і останнього,
другого і передостаннього, третього з початку і третього від кінця і т.д.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import numpy as np     # імпортуємо бібліотеку numpy для роботи з масивами
import random     # імпортуємо функцію randint() для генерування випадкових чисел
# ініціалізуємо масив з прізвищами, для випадкового заповнення вихідного масиву
L = np.array(['Smith', 'Brown', 'Miller', 'Thomas', 'Martin', 'Clark', 'Allen', 'Scott', 'Nelson', 'Campbell', 'Parker'])
while True:
    N = random.randint(10, 15)   # визначаємо розмір масиву випадковим значенням у межах від 10 до 20
    A = np.random.choice(L, size=N)  # заповнюємо масив рандомними значення зі списку L розміром N
    print(A)
    for i in range(N//2):  # циклічно обходимо половину елементів масиву
        A[i], A[N - i - 1] = A[N - i - 1], A[i]   # міняємо елементи перший і останній, другий та предостанній і т.д.
    print(A)

    answer = input('Бажаєте запустити ще раз (+) чи за завершити програму (будь-що)? ')
    if answer == '+':
        print('')
        continue
    else:
        break
