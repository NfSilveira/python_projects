import random

def lottery():
    game = []
    while len(game) < 6:
        num = random.randint(1, 60)
        if num in game:
            continue
        else:
            game.append(num)
    print(sorted(game))

lottery()