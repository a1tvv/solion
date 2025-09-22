data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
data_tuple = list(data_tuple)

letters = []
numbers = []

# юзаем цикл фор
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
     
     
     
#  удаляем 6.13 и добавляем тру в леттер   
numbers.remove(6.13)
numbers.remove(True)
letters.append(True)

# сортировка чисел
numbers.sort()

# меняем буквы местами и создаём нужные значения
letters.reverse()
letters[1] = 's'
letters[3] = 'e'

letters = [letters[0], letters[1], letters[3], letters[2]]

print(numbers)
print(letters)
