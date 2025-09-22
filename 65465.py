data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for i in data_tuple:
    if type(i)==str):
        letters.append(i)
    else:
        numbers.append(i)

# Убираем 6.13 из чисел
numbers.remove(6.13)

# Перемещаем True в список букв
numbers.remove(True)
letters.append(True)

# Сортируем числа
numbers.sort()

# Разворачиваем буквы
letters.reverse()

# Берём только нужные элементы (первые 5 и последний)
letters = letters[:5] + [letters[-1]]

print("Letters:", letters)
print("Numbers:", numbers)
