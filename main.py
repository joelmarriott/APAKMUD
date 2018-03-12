import rooms
import player

def selDiff():
    "Return health, stamina and potions based on difficulty selection"
    while 1:
        difficulty = raw_input('Please choose difficulty, (\033[92mEasy, \033[93mHard, \033[91mInsane\033[0m): ')
        difficulty = difficulty.upper()
        if difficulty == 'EASY':        # On easy
            health = 100                # Health is 100
            stamina = 100               # Stamina is 100
            potions = 10                # There are 10 potions
            break
        elif difficulty == 'HARD':      # On hard
            health = 50                 # Health is 50
            stamina = 50                # Stamina is 50
            potions = 5                 # There are 5 potions
            break
        elif difficulty == 'INSANE':    # On insane
            health = 10                 # Health is 10
            stamina = 10                # Stamina is 10
            potions = 1                 # There is 1 potion
            break
        else:
            print("Input invalid.")     # Unrecognised phrase
    return health, stamina, potions     # H/S/P returned by function

if __name__ == '__main__':              # If program is "main"
    deaths = 0                          # Initialize death count
    while 1:
        
        health, stamina, potions = selDiff()
        p1 = player.Player(health, stamina, potions)
        r1 = rooms.Room()               # Create an instance of a room
        while p1.isalive == True:       # Check for death
            nextrm = getattr(r1, p1.loc)# Get room
            p1 = nextrm(p1)             # Go to next room

        deaths += 1
        raw_input("You died. You have died " + str(deaths) + " times. Continue?")
