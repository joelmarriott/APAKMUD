import player

def outside(player):
    where = raw_input('Go back to car, or enter the building? (Car/Enter) : ')
    where = where.upper()

    if where == 'CAR':           ## Make a car location
        print("You rummage around in your car, and find your keyfob. Oops!")
        player.bag['Keyfob'] = 1
        player.location = reception
    print 'End of room (Health, Stamina, Potions): ', health, stamina, potions
    return player

def reception(player):
    if 'Keyfob' in player.bag:
        print "You walk into reception"
        player.location = hallway
    else:
        print "You forgot your keyfob..."
        player.health = 0
    return player

def selDiff():
    "Return health, stamina and potions based on difficulty selection"
    while 1:
        difficulty = raw_input('Please choose difficulty, (\033[92mEasy, \033[93mHard, \033[91mInsane\033[0m): ')
        difficulty = difficulty.upper()
        if difficulty == 'EASY':
            health = 100
            stamina = 100
            potions = 10
            break
        elif difficulty == 'HARD':
            health = 50
            stamina = 50
            potions = 5
            break
        elif difficulty == 'INSANE':
            health = 10
            stamina = 10
            potions = 1
            break
        else:
            print("Input invalid.")
    return health, stamina, potions

if __name__ == '__main__':
    deaths = 0
    while 1:
        
        health, stamina, potions = selDiff()
        p1 = Player(health, stamina, potions)
        while health > 0:
            p1 = p1.location(p1)
