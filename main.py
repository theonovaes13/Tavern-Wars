

from menu import *

while 1:
    main_menu()
    tutorial()
    versus_mode()
    window.update()
    player_1["idle"].update()
    player_2["idle"].update()
    player_1["attack"].update()
    player_2["attack"].update()
    player_1["damage"].update()
    player_2["damage"].update()


