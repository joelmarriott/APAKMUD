class Player(object):
    def __init__(self, health, stamina, food, coffee, difficulty):
        self.health = health           # Set health
        self.stamina = stamina         # Set stamina
        self.maxhp = health            # Set maximum health
        self.maxstam = stamina         # Set maximum stamina
        self.bag = { 'Keyfob':0, 'Food':int(food), 'Coffee':int(coffee) }
        self.loc = 'outside'           # Where are they?
        self.isalive = True            # Are they alive?
        self.difficulty = difficulty   # What is their difficulty?
        self.carlock = False           # Is their car locked?
        self.lightson = True           # Are their car lights left on?

    @property
    def health(self):
        #print 'health Getter'         # Uncomment for debug
        return self._health

    @health.setter
    def health(self, health):
        #print 'health Setter'         # Uncomment for debug
        self._health = int(health)

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

                if self.health > self.maxhp:
                    self.health = self.maxhp

                if self.stamina > self.maxstam:
                    self.stamina = self.maxstam
