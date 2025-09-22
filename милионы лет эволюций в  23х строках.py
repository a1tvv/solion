flags = {
    'ru': {'red', 'blue', 'white'},
    'kg': {'red', 'yellow'},
    'ua': {'red', 'blue'},
    'uk': {'yellow', 'blue'},
    'kz': {'blue', 'yellow'},
    'ch': {'red', 'yellow'},
    'jp': {'white', 'red'},
    'us': {'blue', 'red', 'white'}
}


while True:
    user_input = input('Введите цвет на англ (или "exit" для выхода): ')
    
    if user_input == 'exit':
        break

    for key, value in flags.items():
        if user_input in value:
            print(key)