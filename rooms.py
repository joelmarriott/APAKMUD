class Room(object):
    def __init__(self):                 # Initialize room
        self.walls = 0                  # With no walls (outside)
        self.roof = 0                   # With no roof (outside)
        
    def outside(self, player):
        where = raw_input('Go back to car, or enter the building? (Car/Enter) : ')
        where = where.lower()           # Make where upper case

        if where == 'car':
            player.loc = 'car'          # Set location to car
        else:    
            player.loc = 'reception'    # Set location to reception
        print('End of room (Health, Stamina, {Bag Item: Amount}): ')
        print(str(player.health) + ', ' + str(player.stamina) + ', ' + str(player.bag))
        return player                   # Update player

    def car(self, player):
        print('You rummage around in your car, and find your keyfob. Oops!')
        player.bag['Keyfob'] = 1        # Add keyfob to bag
        player.loc = 'reception'        # Set location to reception
        print('End of room (Health, Stamina, {Bag Item: Amount}): ')
        print(str(player.health) + ', ' + str(player.stamina) + ', ' + str(player.bag))
        return player                   # Update player

    def reception(self, player):
        if 'Keyfob' in player.bag:      # Does player have keyfob?
            print "You walk into reception"
            player.loc = 'hallway'      # Set location to hallway
        else:
            print "You forgot your keyfob..."
            player.health = 0           # Player 'dies'
        print('End of room (Health, Stamina, {Bag Item: Amount}): ')
        print(str(player.health) + ', ' + str(player.stamina) + ', ' + str(player.bag))
        return player                   # Update player

    def hallway(self, player):
        raw_input("You are in the hallway. The alarms are on. Don't move!")
        player.health = 0
        print('End of room (Health, Stamina, {Bag Item: Amount}): ')
        print(str(player.health) + ', ' + str(player.stamina) + ', ' + str(player.bag))
        return player
