import rooms
import player

def menu(player):
    while 1:
        option = raw_input('\033[92mSelect menu option (\033[96m[E]\033[92mat, ' +
                           '\033[96m[D]\033[92mrink, \033[96m[Enter]\033[92m to continue): ')
        option = option.lower()
    
        if option == 'e':
            if player.bag['Food'] >= 1:
                player.bag['Food'] -= 1
                player.health += (player.maxhp / 3)
                print('\033[92mHealth restored by ' + str((player.maxhp / 3)) + ' \033[0m')
            else:
                print('\033[91mYou do not have any food\033[0m')
        elif option == 'd':
            if player.bag['Coffee'] >= 1:
                player.bag['Coffee'] -= 1
                player.stamina += (player.maxstam / 3)
                print('\033[92mStamina restored by ' + str((player.maxstam / 3)) + ' \033[0m')
            else:
                print('\033[91mYou do not have any coffee\033[0m')
        else:
            print(' ')
            break
        return player

if __name__ == '__main__':              # If program is "main"
    players = []
    while 1:
        pcount = raw_input('\033[92mSelect number of players: \033[0m')
        pcount = int(pcount)        
        try:
            if pcount < 1:
                raise ValueError, 'Less than 1 player?'
                break
        except (ValueError, TypeError):
            print('Number of players must be greater than 0')
            break
            
        for p in range(pcount):
            n, h, s, f, c, d = player.Player.setup()
            players.append(player.Player(n, h, s, f, c, d))
        break

    while 1:
        pcount = len(players)
        for t in range(pcount):
            for isalive in str(players[t].isalive):
                room = rooms.Room()               # Create an instance of a room
                if players[t].isalive:
                    print('                              \033[93mIt is ' + players[t].name + '\'s turn\033[0m')
                    print('')                         # show name
                    nextrm = getattr(room, players[t].loc)  # Get room
                    players[t] = nextrm(players[t])             # Go to next room
                    rooms.Room.endofroom(room, players[t])
                    if players[t].health > 0:
                        menu(players[t])
                elif players[t].dead == False:
                    print('                              \033[91m' + players[t].name + ' is dead.\033[0m')
                    break
                else:
                    players[t].deaths += 1                     # [ADD TO PLAYER]
                    raw_input("\033[91mYou died. You have died " + str(players[t].deaths) + " times. Continue?\033[0m")
                    players[t].dead == True
                break
