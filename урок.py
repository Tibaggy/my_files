spisok = []
u_game = input('Название игры. Если хотите закончить напишите - выход ')
r = input('Рейтинг этой игры ')
while u_game.lower() != 'выход':
    game = u_game, r
    spisok.append(game)
    print(spisok)
    u_game = input('Название игры. Если хотите закончить напишите - выход ')
    r = input('Рейтинг этой игры ')
    
