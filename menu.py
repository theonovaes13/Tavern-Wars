from objetos import *
from versus import *



def main_menu():
        global GAMESTATE, damage_counter
        if GAMESTATE == 2:
            trilhaMenu.play()
            damage_counter["player_two"] = 0
            damage_counter["player_one"] = 0
            fundoMenu.draw()
            placadomeio.draw()
            versus.draw()
            challenge.draw()
            howtoplay.draw()
            play.draw()
            if mouse.is_over_object(howtoplay):
                mousecima.draw()
                if mouse.is_button_pressed(1):
                    GAMESTATE = 3
            if mouse.is_over_object(play):
                mouseplay.draw()
                if mouse.is_button_pressed(1):
                    GAMESTATE = 4
                    trilhaMenu.stop()
                    trilhaJogo.play()

            return damage_counter


def tutorial():
    global GAMESTATE
    if GAMESTATE == 3:
        power_button.set_position(tutorial_angle_example.x, (tutorial_angle_example.y + tutorial_angle_example.height + 100))
        tutorial_background.draw()
        tutorial_angle_example.draw()
        tutorial_text.draw()
        spacebar.draw()
        power_button.draw()
        arrow_keys.draw()
        back_button.draw()
        if mouse.is_over_object(back_button):
            selected_back_button.draw()
            if mouse.is_button_pressed(1):
                GAMESTATE = 2

        return GAMESTATE




def versus_mode():
    global GAMESTATE, abebebikila, vidas1, vidas2, damage_counter
    if abebebikila == 1:
        GAMESTATE = 2
        abebebikila = 0
        window.delay(20)
        vidas1 = 3
        vidas2 = 3
        damage_counter["player_one"] = 0
        damage_counter["player_two"] = 0
    if GAMESTATE == 4:
        ceu.draw()
        nuvens.draw()
        chaoesquerda.draw()
        chaodireita.draw()
        pedradir.draw()
        pedraesq.draw()
        arvore1.draw()
        mesa.draw()
        player_1["idle"].draw()
        player_2["idle"].draw()
        player_1["attack"].draw()
        player_2["attack"].draw()
        bomb_aim()
        attack()
        animacaoDano()
        controle()
        abebebikila = endgame()
        hud()

    return


