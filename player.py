class Player(object):
  def __init__(self, health, stamina, potions):
    self.health = health
    self.stamina = stamina
    self.bag = { 'Potions':int(potions) }
    self.location = outside
