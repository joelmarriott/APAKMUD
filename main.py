import rooms
import player

def selDiff():
    "Return health, stamina, food and coffee based on difficulty selection"
    while 1:
        difficulty = raw_input('Please choose difficulty (\033[92mEasy, \033[93mHard, \033[91mInsane\033[0m): ')
        difficulty = difficulty.lower()
        if difficulty == 'easy':        # On easy
            health = 100                # Health is 100
            stamina = 100               # Stamina is 100
            food = 10                   # There are 10 pieces of food
            coffee = 10                 # There are 10 cups of coffee
            break
        elif difficulty == 'hard':      # On hard
            health = 50                 # Health is 50
            stamina = 50                # Stamina is 50
            food = 5                    # There are 5 pieces of food
            coffee = 5                  # There are 5 cups of coffee
            break
        elif difficulty == 'insane':    # On insane
            health = 10                 # Health is 10
            stamina = 10                # Stamina is 10
            food = 1                    # There is 1 lot of food
            coffee = 1                  # There is 1 cup of coffee
            break
        else:
            print("\033[91mInput invalid.\033[0m")
    print(' ')                           # Output empty line to break things up
    return health, stamina, food, coffee, difficulty # H/S/F/C/D returned by function

if __name__ == '__main__':              # If program is "main"
    deaths = 0                          # Initialize death count [ADD TO PLAYER]
    while 1:
        
        health, stamina, food, coffee, difficulty = selDiff()
        p1 = player.Player(health, stamina, food, coffee, difficulty)
        r1 = rooms.Room()               # Create an instance of a room
        while p1.isalive == True:       # Check for death
            nextrm = getattr(r1, p1.loc)# Get room
            p1 = nextrm(p1)             # Go to next room
            rooms.Room.endofroom(r1, p1)

        deaths += 1                     # [ADD TO PLAYER]
        raw_input("\033[91mYou died. You have died " + str(deaths) + " times. Continue?\033[0m")
