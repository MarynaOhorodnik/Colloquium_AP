'''
З 8 до 20 години температура повітря вимірювалася щогодини. Відомо, що протягом цього часу температура знижувалася.
Визначте, о котрій годині було вперше зафіксовано від'ємну температуру.
Огороднік Марина Олександрівна, І курс, група 122А
'''
# створюємо словник з значеннями 'час:температура'
T = {'8:00': 17, '9:00': 16, '10:00': 15, '11:00': 12, '12:00': 10, '13:00': 9, '14:00': 6, '15:00': 2, '16:00': 1,
     '17:00': -2, '18:00': -6, '19:00': -8, '20:00': -12}

for i in sorted(T.keys()):     # обходимо циклом всі ключі словника
    if T[i] < 0:     # якщо знайдено перший від'ємний елемент, то завершуємо цикл,
        break        # а в змінній 'i' буде ключ першого від'ємного значення температури
print(f'о {i} годині вперше зафіксовано від`ємну температуру {T[i]}')
