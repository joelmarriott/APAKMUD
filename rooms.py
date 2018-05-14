from random import randint

import player

class Room(object):
    def __init__(self):                 # Initialize room
        self.inv = {}                   # Initialize inventory
        self.walls = 0                  # With no walls (outside)
        self.roof = 0                   # With no roof (outside)
        self.inv['Keyfob'] = 1

    def endofroom(self, player):
        player.recharge()
        print('\033[94mEnd of room')
        print('HP: ' + str(player.health) + '/' + str(player.maxhp) + ' - STAM: ' + str(player.stamina) + '/' + str(player.maxstam))
        print('Bag:'),
        for key in player.bag:
            print(key + '(' + str(player.bag[key]) + ')'),
        print('\033[0m ')
        print(' ')
        
    def outside(self, player):
        print('\033[92mYou leave your car.\033[0m')
        x = 1
        while x == 1:
            option = raw_input('\033[92m(\033[96m[C]\033[92mar, \033[96m[E]\033[92mnter): ')
            option = option.lower()           # Make where upper case

            if option == 'c':
                player.loc = 'car'          # Set location to car
                player.stamina -= 1
                x = 0
            elif option == 'e':    
                player.loc = 'reception'    # Set location to reception
                player.stamina -= 1
                x = 0
            else:
                print('\033[91mInput invalid.\033[0m')

        return player                   # Update player

    def car(self, player):
        x = 1
        if player.carlock == False:
            print('\033[92mYou noticed your car door was unlocked. Lucky you came back!\033[0m')
        else:
            print('\033[92mYou unlock your car and get in.\033[0m')
            player.carlock = False      # Unlock car
        while x == 1:
            option = raw_input('\033[92m(\033[96m[G]\033[92mlovebox, \033[96m[Li]\033[92mghts, ' +
                               '\033[96m[Lo]\033[92mck, \033[96m[L]\033[92meave): ')
            option = option.lower()

            if option == 'g':
                if self.inv['Keyfob'] >= 1:
                    print('\033[92mYou rummage around in your car, and find your keyfob. Oops!\033[0m')
                    self.inv['Keyfob'] -= 1  # Remove keyfob from room inventory
                    player.bag['Keyfob'] += 1 # Add keyfob to bag
                else:
                    print('\033[92mYou rummage around in your car, but find nothing.\033[0m')
                player.stamina -= 1
            elif option == 'li':
                if player.lightson == True:
                    print('\033[93m\"Oh... My lights are on. Better switch those off!\"\033[0m')
                    player.lightson = False # Turn lights off
                else:
                    print('\033[92mYou turn your lights on.\033[0m')
                    player.lightson = True # Turn lights on
                player.stamina -= 1
                
            elif option == 'lo':
                print('\033[92mYou lock your car as you leave\033[0m')
                player.stamina -= 1
                player.carlock = True   # Lock car
                x = 0
            elif option != 'l':
                print('\033[91mInput invalid.\033[0m')
            else:
                x = 0
                
        player.loc = 'outside'          # Set location to outside
        return player                   # Update player

    def reception(self, player):
        if player.bag['Keyfob'] == 0:      # Does player have keyfob?
            print "\033[91mYou forgot your keyfob...\033[0m"
            player.health -= 40         # Player loses 40 health
            player.stamina -= 20        # Lose 20 stamina to go back outside
            player.loc = 'outside'
        else:
            print('\033[92mYou walk into reception\033[0m')
            x = 1
            while x == 1:
                option = raw_input('\033[92m(\033[96m[M]\033[92meeting, \033[96m[H]\033[92mallway, ' +
                                   '\033[96m[G]\033[92mreet):\033[0m ')
                option = option.lower()

                if option == 'm':
                    player.loc = 'meeting'
                    x = 0
                elif option == 'h':
                    player.loc = 'hallway'
                    x = 0
                elif option == 'g':
                    print('         \033[93mYou: \033[97mGood morning!')
                    print('\033[93mReceptionist: \033[97mGood morning.' +
                          ' I could really use a \033[96m[C]\033[97moffee...')
                    print('              \033[97mAt this point, the machine in the hallway will do!\033[0m')
                elif option == 'c':
                    if player.bag['Coffee'] >= 1:
                        print('\033[92mYou hand the receptionist a coffee\033[0m')
                        player.bag['Coffee'] -= 1
                        print('\033[93mReceptionist: \033[97mThanks! I\'ve been so busy, I couldn\'t leave my desk!')
                        player.rapport += 1
                    else:
                        print('\033[91mYou do not have any coffee to give the receptionist!\033[0m')
                else:
                    print('\033[91mInput invalid.\033[0m')
        return player                   # Update player

    def hallway(self, player):
        x = 1
        while x == 1:
            option = raw_input('\033[92m(\033[96m[M]\033[92meeting, \033[96m[R]\033[92meception, ' +
                               '\033[96m[T]\033[92mechnical Services):\033[0m ')
            option = option.lower()
            
            if option == 'c':
                roll = randint(1, 10) # Roll a 10 sided dice
                player.bag['Coffee'] += 1
                if roll >= 6:
                    player.maxstam -= 1
                    print('The amount of coffee you have been drinking has led to heart palpatations. Lose 1 max stamina')
                print('\033[92mYou gained one coffee')
            elif option == 'r':
                player.loc = 'reception'
                x = 0
            elif option == 't':
                player.loc = 'tech'
                x = 0
            elif option == 'm':
                player.loc = 'meeting'
                x = 0
            elif option == 'cu':
                print('\033[92mSomething to do with the cupboard')
            else:
                print('\033[91mInput invalid.\033[0m')
                
        return player

    def meeting(self, player):
        print('You are in the meeting room.')
        option = raw_input('\033[92m(\033[96m[H]\033[92mallway, \033[96m[R]\033[92meception: ')
        option = option.lower

        if option == 'h':
            player.loc = 'hallway'
            player.stam -= 1
        elif option == 'r':
            player.loc = 'reception'
            player.stam -= 1
        else:
            print('\033[91mInput invalid.\033[0m')
        return player

    def tech(self, player):
        print('You are in technical services.')
        option = raw_input('\033[92m(\033[96m[H]\033[92mallway, \033[96m[M]\033[92meeting: ')
        option = option.lower

        if option == 'h':
            player.loc = 'hallway'
            player.stam -= 1
        elif option == 'm':
            player.loc = 'meeting'
            player.stam -= 1
        else:
            print('\033[91mInput invalid.\033[0m')
        return player
