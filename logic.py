from random import randint

def is_win(slot):
    win_slot = randint(1,30)
    return win_slot == slot