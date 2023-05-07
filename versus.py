from objetos import *
from math import fabs
from math import sin
from math import cos


def controle():
    global vez
    if lancabomba == 0:
        if vez == 1:
            bomba.set_position((player_1["idle"].x + player_1["idle"].width) ,
                               (player_1["idle"].y + player_1["idle"].height)- bomba.height)
        if vez == 2:
            bomba.set_position(player_2["idle"].x - bomba.width, ((player_2["idle"].y + player_2["idle"].height)- bomba.height))
    bomba.draw()
    return




def vidas(objeto, vidas):
    lista = []
    for x in range(vidas):
        coracao = Sprite('spritesheet/gameplay/HUD/coracao.png')
        coracao.set_position(50 + (objeto.x + (coracao.width* x)), objeto.y + 25)
        lista.append(coracao)
    return lista


def hud():
    global vidas1, vidas2

    vida2.draw()
    vida1.draw()
    nhami = vidas(vida1, vidas1)
    nhomi = vidas(vida2, vidas2)
    for coracao in nhami:
        coracao.draw()
    for coracao in nhomi:
        coracao.draw()
    return


def miratiro1():
    global keyboard, angulomira, mira
    if vez == 1:
        mira.set_position((player_1["idle"].x) + (100 * cos(angulomira)),
                          (player_1["idle"].y + player_1["idle"].height)- (50) + (100 * sin(angulomira)))
        if angulomira >= -1.5 and angulomira <= 0:
            if keyboard.key_pressed("UP"):
                angulomira -= 0.1
            elif keyboard.key_pressed("DOWN"):
                angulomira += 0.1
        if angulomira < -1.5:
            angulomira = -1.5
        if angulomira > 0:
            angulomira = 0
        mira.draw()
    if vez == 2:
        mira.set_position((player_2["idle"].x) + (100 * cos(angulomira)),
                          (player_1["idle"].y + player_1["idle"].height)- (50) + (100 * sin(angulomira)))
        if angulomira >= -3 and angulomira <= -1.5:
            if keyboard.key_pressed("UP"):
                angulomira += 0.1
            elif keyboard.key_pressed("DOWN"):
                angulomira -= 0.1
        if angulomira > -1.5:
            angulomira = -1.5
        if angulomira < -3:
            angulomira = -3
        mira.draw()

    return

def tiro1():
    global keyboard, vez, atirar, atirou, biri, lancabomba, power1, seno, coco, gravidade, vidas2, vidas1, libera1, libera2, contadorvidas1, contadorvidas2
    seno = power1 * sin(angulomira) + fabs(gravidade)
    coco = power1 * cos(angulomira)
    if vez == 1:
        if keyboard.key_pressed("SPACE") and atirar == 1:
            marcador.set_position(marcador.x + 1, marcador.y)
            if marcador.x >= (poder.x + poder.width):
                marcador.x = poder.x + poder.width
            biri += 0.5
            poder.draw()
            marcador.draw()
            atirou = 1
            power1 = biri
        elif not keyboard.key_pressed("SPACE") and atirou == 1:
            atirar = 0
            atirou = 0
            biri = 0
            marcador.set_position(poder.x, poder.y)
            player_1["attack"].set_curr_frame(0)
            player_1["attack"].unhide()
            player_1["attack"].play()
            player_1["idle"].hide()

        frame = player_1["attack"].get_curr_frame()
        if frame == 8:
            chute.play()

        if frame >= 11 and atirar == 0:
            player_1["attack"].hide()
            player_1["idle"].unhide()
            player_1["attack"].stop()
            lancabomba = 1
        if lancabomba == 1:
            bomba.set_position(bomba.x + coco, bomba.y + seno)
            gravidade += 0.5
            if (bomba.y + bomba.height) >= chaoesquerda.y or (bomba.x + bomba.width) >= player_2["idle"].x:
                if bomba.collided(player_2["idle"]):
                    dor.play()
                    player_2["damage"].set_curr_frame(0)
                    libera2 = 1
                    lancabomba = 0
                    contadorvidas2 += 1
                    vidas2 -= 1
                    vez = 2
                    atirar = 1
                    gravidade = 0
                if bomba.y + bomba.height >= chaoesquerda.y:
                    lancabomba = 0
                    gravidade = 0
                    vez = 2
                    atirar = 1




    if vez == 2:
        if keyboard.key_pressed("SPACE") and atirar == 1:
            marcador2.set_position(marcador2.x + 1, marcador2.y)
            if marcador2.x >= (poder2.x + poder2.width):
                marcador2.x = poder2.x + poder2.width
            biri += 0.5
            poder2.draw()
            marcador2.draw()
            atirou = 1
            power1 = biri
        elif not keyboard.key_pressed("SPACE") and atirou == 1:
            atirar = 0
            atirou = 0
            biri = 0
            marcador2.set_position(poder2.x, poder2.y)
            player_2["attack"].set_curr_frame(0)
            player_2["attack"].unhide()
            player_2["attack"].play()
            player_2["idle"].hide()
            framea = player_2["attack"].get_curr_frame()
            if framea == 8:
                chute.play()
        if player_2["attack"].get_curr_frame() >= 10 and atirar == 0:
            chute.play()
            player_2["attack"].hide()
            player_2["idle"].unhide()
            player_2["attack"].stop()
            lancabomba = 1
        if lancabomba == 1:
            bomba.set_position(bomba.x + coco, bomba.y + seno)
            gravidade += 0.5
            if (bomba.y + bomba.height) >= chaoesquerda.y or (bomba.x + bomba.width) >= player_2["idle"].x:
                if bomba.collided(player_1["idle"]):
                    dor.play()
                    player_1["damage"].set_curr_frame(0)
                    libera1 = 1
                    lancabomba = 0
                    contadorvidas1 += 1
                    vidas1 -= 1
                    vez = 1
                    atirar = 1
                    gravidade = 0
                if bomba.y + bomba.height >= chaoesquerda.y:
                    lancabomba = 0
                    gravidade = 0
                    vez = 1
                    atirar = 1

    return

def animacaoDano():
    global libera1, libera2
    if libera1 == 1:
        player_1["idle"].hide()
        player_1["damage"].unhide()
        if player_1["damage"].get_curr_frame() >= 7:
            player_1["idle"].unhide()
            player_1["damage"].hide()
            libera1 = 0
    if libera2 == 1:
        player_2["idle"].hide()
        player_2["damage"].unhide()
        if player_2["damage"].get_curr_frame() >= 7:
            player_2["idle"].unhide()
            player_2["damage"].hide()
            libera2 = 0
    return

def endgame():
    global contadorvidas1, contadorvidas2, mouse, GAMESTATE, vez, abebebikila, vidas2, vidas1, vez
    if contadorvidas2 == 3 or contadorvidas1 == 3:
        bg.draw()
        fechar.draw()
        main_menuu.draw()
        if contadorvidas1 == 3:
            p2wins.draw()
        if contadorvidas2 == 3:
            p1wins.draw()
        if mouse.is_over_object(main_menuu):
            if mouse.is_button_pressed(1):
                abebebikila = 1
                contadorvidas1 = 0
                contadorvidas2 = 0
                vidas1 = 3
                vidas2 = 3
                vez = 1
                hud()
                trilhaJogo.stop()
                trilhaMenu.play()
                return abebebikila
        if mouse.is_over_object(fechar):
            if mouse.is_button_pressed(1):
                window.close()
    return