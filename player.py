import main

class Player(object):
    def __init__(self, name, health, stamina, food, coffee, difficulty):
        self.name = name                # Set name
        self.deaths = 0                 # Initialize death counter
        self.dead = False               # Player is already dead - don't output 'you died' screen
        self.maxhp = health             # Set maximum health
        self.maxstam = stamina          # Set maximum stamina
        self.health = health            # Set health
        self.stamina = stamina          # Set stamina
        self.rapport = 0                # Set rapport
        self.bag = { 'Keyfob':0, 'Food':int(food), 'Coffee':int(coffee) }
        self.loc = 'outside'            # Where are they?
        self.isalive = True             # Are they alive?
        self.difficulty = difficulty    # What is their difficulty?
        self.carlock = False            # Is their car locked?
        self.lightson = True            # Are their car lights left on?

    @staticmethod
    def setup():
        "Return name, health, stamina, food and coffee based on difficulty selection"
        name = raw_input('\033[92mWhat would you like to be called?: \033[92m')
        while 1:
            difficulty = raw_input('\033[92mPlease choose difficulty (\033[92mEasy, \033[93mHard, \033[91mInsane\033[0m\033[92m): ')
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
                print('\033[91mInput invalid.\033[0m')

        print(' ')                          # Output empty line to break things up

        return name, health, stamina, food, coffee, difficulty # H/S/F/C/D returned by function
        
    @property
    def health(self):
        #print 'health Getter'         # Uncomment for debug
        return self._health

    @health.setter
    def health(self, health):
        #print 'health Setter'         # Uncomment for debug
        self._health = int(health)

        if self._health > self.maxhp:
            self._health = self.maxhp
        
        if self._health <= 0:
            self.isalive = False       # Kill them
        else:
            self.isalive = True        # They live... for now

    @property
    def stamina(self):
        #print 'stamina Getter'        # Uncomment for debug
        return self._stamina

    @stamina.setter
    def stamina(self, stamina):
        #print 'stamina Setter'        # Uncomment for debug
        self._stamina = int(stamina)

        if self._stamina > self.maxstam:
            self._stamina = self.maxstam

    def recharge(self):
        #print "recharge"              # Uncomment for debug
        if self.health < 0:            # If damage took player into the negatives
            self.health = 0            # Kill them

        if self.stamina < 0:           # If action took player into the negatives
            self.stamina = 0           # No energy
            
        if self.health != 0:           # If dead, don't recharge
            if self.health != self.maxhp or self.stamina != self.maxstam:  
                if self.difficulty == "easy":
                    self.health += 1.5
                    self.stamina += 1.5
                elif self.difficulty == "hard":
                    self.health += 1
                    self.stamina += 1
                else:
                    self.health += 0.5
                    self.stamina += 0.5


