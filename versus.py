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


def bomb_aim():
    global keyboard, aim_angle, crosshair
    if vez == 1:
        crosshair.set_position((player_1["idle"].x) + (100 * cos(aim_angle)),
                          (player_1["idle"].y + player_1["idle"].height)- (50) + (100 * sin(aim_angle)))
        if aim_angle >= -1.5 and aim_angle <= 0:
            if keyboard.key_pressed("UP"):
                aim_angle -= 0.025
            elif keyboard.key_pressed("DOWN"):
                aim_angle += 0.025
        if aim_angle < -1.5:
            aim_angle = -1.5
        if aim_angle > 0:
            aim_angle = 0
        crosshair.draw()
    if vez == 2:
        crosshair.set_position((player_2["idle"].x) + (100 * cos(aim_angle)),
                          (player_1["idle"].y + player_1["idle"].height)- (50) + (100 * sin(aim_angle)))
        if aim_angle >= -3 and aim_angle <= -1.5:
            if keyboard.key_pressed("UP"):
                aim_angle += 0.025
            elif keyboard.key_pressed("DOWN"):
                aim_angle -= 0.025
        if aim_angle > -1.5:
            aim_angle = -1.5
        if aim_angle < -3:
            aim_angle = -3
        crosshair.draw()

    return

def attack():
    global keyboard, vez, atirar, atirou, gauged_power, lancabomba, power1, vertical_velocity, \
        horizontal_velocity, gravidade, vidas2, vidas1, libera1, libera2, DAMAGE_COUNTER
    vertical_velocity = power1 * sin(aim_angle) + fabs(gravidade)
    horizontal_velocity = power1 * cos(aim_angle)
    power_gauge = 1
    if vez == 1:
        if keyboard.key_pressed("SPACE") and atirar == 1:
            marcador.set_position(marcador.x + power_gauge, marcador.y)
            if marcador.x >= (poder.x + poder.width):
                marcador.x = poder.x + poder.width
            gauged_power += 0.5
            poder.draw()
            marcador.draw()
            atirou = 1
            power1 = gauged_power
        
        if not keyboard.key_pressed("SPACE") and atirou == 1:
            atirar = 0
            atirou = 0
            gauged_power = 0
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
            bomba.set_position(bomba.x + horizontal_velocity, bomba.y + vertical_velocity)
            gravidade += 0.5
            if (bomba.y + bomba.height) >= chaoesquerda.y or (bomba.x + bomba.width) >= player_2["idle"].x:
                if bomba.collided(player_2["idle"]):
                    dor.play()
                    player_2["damage"].set_curr_frame(0)
                    libera2 = 1
                    lancabomba = 0
                    DAMAGE_COUNTER["player_two"] += 1
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
            gauged_power += 0.5
            poder2.draw()
            marcador2.draw()
            atirou = 1
            power1 = gauged_power
        elif not keyboard.key_pressed("SPACE") and atirou == 1:
            atirar = 0
            atirou = 0
            gauged_power = 0
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
            bomba.set_position(bomba.x + horizontal_velocity, bomba.y + vertical_velocity)
            gravidade += 0.5
            if (bomba.y + bomba.height) >= chaoesquerda.y or (bomba.x + bomba.width) >= player_2["idle"].x:
                if bomba.collided(player_1["idle"]):
                    dor.play()
                    player_1["damage"].set_curr_frame(0)
                    libera1 = 1
                    lancabomba = 0
                    DAMAGE_COUNTER["player_one"] += 1
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
    global DAMAGE_COUNTER, mouse, GAMESTATE, vez, abebebikila, vidas2, vidas1, vez
    if DAMAGE_COUNTER["player_two"] == 3 or DAMAGE_COUNTER["player_one"] == 3:
        endgame_background_button.draw()
        close_button.draw()
        main_menu_button.draw()
        if DAMAGE_COUNTER["player_one"] == 3:
            player_two_wins.draw()
        if DAMAGE_COUNTER["player_two"] == 3:
            player_one_wins.draw()
        if mouse.is_over_object(main_menu_button):
            if mouse.is_button_pressed(1):
                abebebikila = 1
                DAMAGE_COUNTER["player_one"] = 0
                DAMAGE_COUNTER["player_two"] = 0
                vidas1 = 3
                vidas2 = 3
                vez = 1
                hud()
                trilhaJogo.stop()
                trilhaMenu.play()
                return abebebikila
        if mouse.is_over_object(close_button):
            if mouse.is_button_pressed(1):
                window.close()
    return

def update_sprites():
    player_1["idle"].update()
    player_1["attack"].update()
    player_1["damage"].update()
    player_2["idle"].update()
    player_2["attack"].update()
    player_2["damage"].update()
    return

def reset_game_values():
    return

