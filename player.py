class Player(object):
    def __init__(self, health, stamina, potions):
        self.health = health
        self.stamina = stamina
        self.bag = { 'Potions':int(potions) }
        self.loc = 'outside'
        self.isalive = True

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
