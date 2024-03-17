import random

name = input('Какое Ваше имя?   ')

win = 0
lose = 0
nich = 0
g_c = 0
count_1 = 0
count_2 = 0
win_g = ''

g_f = input('Вы хотите заранее выбрать количевство игр? 1 --- Да   2 --- Нет   ')

if int(g_f) == 1:
    count_2 = int(input('Сколько игр Вы хотите сыграть?(Число)   '))

while count_2 > count_1:
    if int(g_f) == 2:
        input('Введите что-нибудь для начала игры: ')

    if int(g_f) == 1:
        count_1 += 1

    g_c += 1
    com_1 = random.randint(1, 6)
    com_2 = random.randint(1, 6)
    com_r = com_1 + com_2
    print(f'У компьютера выпало: {com_1} и {com_2}.Сумма бросок компьютера: ',com_r)

    pl_1 = random.randint(1, 6)
    pl_2 = random.randint(1, 6)
    pl_r = pl_1 + pl_2
    print(f'У Вас выпало: {pl_1} и {pl_2}.Сумма Ваших бросков: ',pl_r)
    if com_r == pl_r:
        print('Ничья')
        nich += 1
    elif com_r > pl_r:
        print('Поражение')
        lose += 1
    else:
        print('Победа')
        win += 1
    print()
    print(f'Сыграно игр:  {g_c}')
    print()
    print(f'Очки {name}: {win}')
    print(f'Очки Computer:  {lose}')
    print(f'Было ничьи:  {nich}')
    if win == lose:
        win_g = 'Ничья'
    elif win < lose:
        win_g = 'побеждает Computer'
    else:
        win_g = 'побеждает ' + name
    print(f'Итог: {win_g}')
    print()