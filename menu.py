from objetos import *
from versus import *



def main_menu():
        global GAMESTATE, contadorvidas2, contadorvidas1
        if GAMESTATE == 2:
            trilhaMenu.play()
            contadorvidas2 = 0
            contadorvidas1 = 0
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

            return contadorvidas1, contadorvidas2


def tutorial():
    global GAMESTATE
    if GAMESTATE == 3:
        botaopower.set_position(angulo.x, (angulo.y + angulo.height + 100))
        fundohowto.draw()
        angulo.draw()
        texto.draw()
        barra.draw()
        botaopower.draw()
        setas.draw()
        voltar.draw()
        if mouse.is_over_object(voltar):
            voltarselecionado.draw()
            if mouse.is_button_pressed(1):
                GAMESTATE = 2

        return GAMESTATE




def versus_mode():
    global GAMESTATE, abebebikila, vidas1, vidas2, contadorvidas1, contadorvidas2
    if abebebikila == 1:
        GAMESTATE = 2
        abebebikila = 0
        window.delay(20)
        vidas1 = 3
        vidas2 = 3
        contadorvidas1 = 0
        contadorvidas2 = 0
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
        miratiro1()
        tiro1()
        animacaoDano()
        controle()
        abebebikila = endgame()
        hud()

    return


