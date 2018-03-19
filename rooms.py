import player

class Room(object):
    def __init__(self):                 # Initialize room
        self.walls = 0                  # With no walls (outside)
        self.roof = 0                   # With no roof (outside)

    def endofroom(self, player):
        player.recharge()
        print('\033[94mEnd of room')
        print('HP: ' + str(player.health) + ' - STAM: ' + str(player.stamina))
        print('Bag:'),
        for key in player.bag:
            print(key + '(' + str(player.bag[key]) + ')'),
        print('\033[0m ')
        print(' ')
        
    def outside(self, player):
        print('\033[92mYou leave your car.\033[0m')
        where = raw_input('Go back to car, or enter the building? (Car/Enter) : ')
        where = where.lower()           # Make where upper case

        if where == 'car':
            player.loc = 'car'          # Set location to car
            player.stamina -= 1
        elif where == 'enter':    
            player.loc = 'reception'    # Set location to reception
            player.stamina -= 1
        else:
            print('\033[91mInput invalid.\033[0m')

        return player                   # Update player

    def car(self, player):
        x = 1
        print('\033[92mYou noticed your car door was unlocked. Lucky you came back!\033[0m')
        while x == 1:
            option = raw_input('(Glovebox/Lights/Lock/Leave): ')
            option = option.lower()

            if option == 'glovebox':
                print('\033[92mYou rummage around in your car, and find your keyfob. Oops!\033[0m')
                player.bag['Keyfob'] = 1# Add keyfob to bag
                player.stamina -= 1
            elif option == 'lights':
                print('\033[93m\"Oh... My lights are on. Better switch those off!\"\033[0m')
                player.stamina -= 1
                player.lightson = False
            elif option == 'lock':
                print('\033[92mYou lock your car as you leave\033[0m')
                player.stamina -= 1
                player.carlock = True
                x = 0
            elif option != 'leave':
                print('\033[91mInput invalid.\033[0m')
            else:
                x = 0
                
        player.loc = 'outside'          # Set location to outside
        return player                   # Update player

    def reception(self, player):
        if 'Keyfob' in player.bag:      # Does player have keyfob?
            print('\033[92mYou walk into reception\033[0m')
            player.loc = 'hallway'      # Set location to hallway
            player.stamina -= 1
        else:
            print "\033[91mYou forgot your keyfob...\033[0m"
            player.health -= 40         # Player loses 40 health
            player.stamina -= 20        # Lose 20 stamina to go back outside
            player.loc = 'outside'
        return player                   # Update player

    def hallway(self, player):
        raw_input('\033[92mYou are in the hallway. The alarms are on. Don\'t move!\033[0m')
        player.health = 0
        return player
