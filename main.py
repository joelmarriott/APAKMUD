from player import warrior

while 1:
  difficulty = raw_input("Welcome, please choose difficulty [Easy/Hard/Insane]: ")
  difficulty = difficulty.upper()
  
  if difficulty == 'EASY':
    health, stamina = 100, 100
    bag = {'Potions':10}
  elif difficulty == 'HARD':
    health, stamina = 50, 50
    bag = {'Potions':5}
  elif difficulty == 'INSANE':
    health, stamina = 25, 25
    bag = {'Potions':2}
  else:
      print("Input incorrect")
      
  location = "outside"
  p1 = warrior(health, stamina, bag, location)
  
  print("Health: {}, Stamina: {}. You are located {}").format(p1.health, p1.stamina, p1.location)
  print("Bag:")
  for a, b in p1.bag.items():
    print("{} of {}").format(b, a)
