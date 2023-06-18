from logic import is_win
from decouple import config

start_money = config('MY_MONEY', default=5, cast=int)

def game_play():
    money = start_money

    while True:
        print(f'Ваш баланс: {money}$')

        slot = int(input(f'Выберите слот от 1 до 30: '))
        if not slot in range(1,31):
            print('Не правильный слот!')
            continue

        bid = int(input(f'Ваша ставка: '))
        if money < bid:
            print('У вас не достаточно денег!')
            continue

        result = is_win(slot)

        if result:
            print(f'Ваша ставка выиграла! +{bid}$')
            money += bid
        else:
            print(f'Ваша ставка не выиграла! -{bid}$')
            money -= bid

        if money <= 0:
            print(f'ТВОЙ БАЛАНС ПУСТ! НЕ ИГРАЙ В КАЗИК! НЕУДАЧНИК!')
            break

        continue_play = input(f'Хотите ли вы сыграть еще? (введите Y чтобы закончить): ')
        print('-----------------------------------------------------------------------------')

        if continue_play.lower() == 'y':
            break

    print(f'Ваш баланс {money}')

    if money - start_money > 0:
        print(f'Вы вышли в плюс на {money - start_money}$')
    else:
        print(f'Вы вышли в минус на {money - start_money}$')

game_play()
