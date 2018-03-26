# APAKMUD
Multi(Single) User Dungeon based on APAK.

# To-do
- Find a way of implementing username to make player instances truly independant of one another
- Reception: Add 'Office(Downstairs)', greet, wait, meeting
- Office(Downstairs): Add stationary, board office, air con, 
- Hallway: Add coffee machine, toilets, cupboard, upstairs, tech
- Whatever crazy thing you can think of

# 26/03/2018
- Added a menu to consume food/drink & continue
- Fixed a bug where menu came up even after hp hits 0
- Rooms can now have inventories (Keyfob is taken from inv and given to player.bag)
- Added logic to room to switch lights back on, unlock car on return, keyfob can only be found if present.
- End of room panel display improvements (HP/STAM displays current/max, bag display tidied up)

# 19/03/2018
- Colorised things: Narration (Green), Speech (Yellow), Errors/Death Messages (Red), End of Room (Blue)
- Spacing improvements to text
- End of Room text split out to it's own function, cutting down lines in each room.
- Potions changed to 'Food'
- Coffee added to items
- Stamina reduced by 1 every time you perform an action
- Health and Stamina recharged depending on difficulty every time you enter a new room
- Bag display on end of room is a lot less cluttered.
- Car room added, has options which can effect the game.

# 12/03/2018
- Seperated out rooms in order to allow easy collaboration
- Fixed spelling mistakes
- Added incremental death counter