

from menu import *
from versus import *

while not keyboard.key_pressed("ESC"):
    main_menu()
    tutorial()
    versus_mode()
    window.update()
    update_sprites()


