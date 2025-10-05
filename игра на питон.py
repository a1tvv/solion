import random

rock = 'камень'
scissor = 'ножницы'
paper = 'бумага'

list = [rock, scissor, paper]

player_win = 0
pc_win = 0
draw = 0

rounds = int(input("🔥 Йо, это СУЛИФА-батл! Сколько раундов замутим? "))

for i in range(1, rounds + 1):
    pc = random.choice(list)
    player = input('👉 Твой ход: ' )
    
    if (pc == rock and player == 'камень') or (pc == scissor and player == 'ножницы') or (pc == paper and player == 'бумага'):
        print('😐 Ничья… так себе замес.')
        draw += 1
    
    elif (pc == scissor and player == 'камень') or (pc == paper and player == 'ножницы') or (pc == rock and player == 'бумага'):
        print('🔥 Раунд твой!')
        player_win += 1
    
    elif (pc == paper and player == 'камень') or (pc == rock and player == 'ножницы') or (pc == scissor and player == 'бумага'):
        print('💀 Компьютер тебя уделал… , это фиаско братан!')
        pc_win += 1
    else:
        print('Сходи к окулисту')
        
if player_win > pc_win:
    print('🏆 Поздравляю, ты чемпион! Машина в шоке от твоей мощи.')
    
elif player_win < pc_win:
    print('🤖 Компьютер победил! Восстание машин уже близко...')
    
elif player_win == pc_win:
    print('😐 Ничья. Ну, по крайней мере, никто не позорился.')
