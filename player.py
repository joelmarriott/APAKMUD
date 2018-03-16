class Player(object):
    def __init__(self, health, stamina, food, coffee, difficulty):
        self.health = health
        self.stamina = stamina
        self.maxhp = health
        self.maxstam = stamina
        self.bag = { 'Food':int(food), 'Coffee':int(coffee) }
        self.loc = 'outside'
        self.isalive = True
        self.difficulty = difficulty

    @property
    def health(self):
        #print 'health Getter'         # Uncomment for debug
        return self._health

    @health.setter
    def health(self, health):
        #print 'health Setter'         # Uncomment for debug
        self._health = int(health)

        if self._health <= 0:
            self.isalive = False
        else:
            self.isalive = True

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
        if self.health != self.maxhp or self.stamina != self.maxstam:  
            if self.difficulty == "EASY":
                self.health += 1.5
                self.stamina += 1.5
            elif self.difficulty == "HARD":
                self.health += 1
                self.stamina += 1
            else:
                self.health += 0.5
                self.stamina += 0.5

            if self.health > self.maxhp:
                self.health = self.maxhp

            if self.stamina > self.maxstam:
                self.stamina = self.maxstam

            if self.health < 0:
                self.health = 0

            if self.stamina < 0:
                self.stamina = 0
