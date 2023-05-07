from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sound import *

window = Window(1280,700)
window.set_title("TAVERN WARS")

mouse = Window.get_mouse()
keyboard = Window.get_keyboard()

GAMESTATE = 2

damage_counter = {
    "player_one": 0,
    "player_two": 0
}

abebebikila = 0

player_lives = {
    "player_one": 3,
    "player_two": 3
}
vidas1 = 3
vidas2 = 3

aim_angle = 0
vez = 1
atirar = 1
atirou = 0
gauged_power = 0
lancabomba = 0
power1 = 0
gravidade = 0
libera1 = 0
libera2 = 0


#cenadomenu
placadomeio = Sprite("spritesheet/menu/placa central.png")
versus = Sprite("spritesheet/menu/Bandeira esq.png")
challenge = Sprite("spritesheet/menu/Bandeira dir.png")
botaoAudio = Sprite("spritesheet/menu/audio.png")
fundoMenu = GameImage("spritesheet/menu/fundomenu.png")
howtoplay = Sprite("spritesheet/menu/howto.png")
mudo = Sprite("spritesheet/menu/noaudio.png")
mousecima = Sprite("spritesheet/menu/mousecima.png")
play = Sprite("spritesheet/menu/play.png")
mouseplay = Sprite("spritesheet/menu/playcima.png")


#cenatutorial
tutorial_background = Sprite("spritesheet/howtoplay/bg.png")
tutorial_angle_example = Sprite("spritesheet/howtoplay/angulo.png")
tutorial_text = Sprite("spritesheet/howtoplay/texto.png")
power_button = Sprite("spritesheet/howtoplay/botaopower.png")
arrow_keys = Sprite("spritesheet/howtoplay/setadireita.png")
spacebar = Sprite("spritesheet/howtoplay/spacebar.png")
back_button = Sprite("spritesheet/howtoplay/config.png")
selected_back_button = Sprite("spritesheet/howtoplay/voltarselecionado.png")

#versus
arvore1 = Sprite("spritesheet/gameplay/tileset/campos/arvore1.png")
chaoesquerda = Sprite("spritesheet/gameplay/tileset/campos/chao1.png")
chaodireita =  Sprite("spritesheet/gameplay/tileset/campos/chao1.png")
pedraesq = Sprite("spritesheet/gameplay/tileset/campos/pedraesq.png")
pedradir = Sprite("spritesheet/gameplay/tileset/campos/pedradir.png")
mesa = Sprite("spritesheet/gameplay/tileset/campos/mesa.png")
marcador = Sprite("spritesheet/gameplay/marcador.png")

player_1 = {
    "idle": Animation("spritesheet/gameplay/idle_pirata.png", 34, True),
    "attack": Animation("spritesheet/gameplay/attack_pirata.png", 12, True),
    "damage": Animation("spritesheet/gameplay/danopirata.png", 8, True)
}

player_2 = {
    "idle": Animation("spritesheet/gameplay/pepino_idle.png", 36, True),
    "attack": Animation("spritesheet/gameplay/pepino_ataca.png", 11, True),
    "damage": Animation("spritesheet/gameplay/danopepino.png", 8, True)
}

player_1["idle"].set_sequence_time(0,34, 60, True)
player_1["attack"].set_sequence_time(0,12, 60, True)
player_1["damage"].set_sequence_time(0,8, 30, True)

player_2["idle"].set_sequence_time(0, 35, 60, True)
player_2["attack"].set_sequence_time(0,11, 60, True)
player_2["damage"].set_sequence_time(0,8, 30, True)

player_1["attack"].hide()
player_1["damage"].hide()

player_2["attack"].hide()
player_2["damage"].hide()

bomba = Sprite("spritesheet/gameplay/bomba.png")

#versus - HUD
vida1 = Sprite("spritesheet/gameplay/HUD/barradevida1.png")
vida2 = Sprite("spritesheet/gameplay/HUD/barradevida2.png")
vida1.set_position(10,10)
vida2.set_position((window.width - vida2.width)- 10, 10)

crosshair = Sprite("spritesheet/gameplay/mira.png")

#background
ceu = Sprite("spritesheet/gameplay/tileset/background/ceu.png")
nuvens = Sprite("spritesheet/gameplay/tileset/background/nuvens.png")









#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~









#menu
placadomeio.set_position((window.width - placadomeio.width)/2, 0)
versus.set_position(0, 40)
challenge.set_position(placadomeio.width + placadomeio.x + (placadomeio.x - versus.width), 40)
botaoAudio.set_position(5, window.height - botaoAudio.height - 5)
howtoplay.set_position((window.width - howtoplay.width)/2, placadomeio.height + 60)
mudo.set_position(botaoAudio.x, botaoAudio.y)
mousecima.set_position(howtoplay.x, howtoplay.y)
play.set_position((window.width - play.width)/2,(howtoplay.y + howtoplay.height) + 10)
mouseplay.set_position(play.x, play.y)

#tutorial
tutorial_angle_example.set_position(40,40)
tutorial_text.set_position(tutorial_angle_example.x + 500, 100)

back_button.set_position(50, (window.height - back_button.height - 50))
arrow_keys.set_position(tutorial_text.x, (tutorial_text.y + tutorial_text.height + 50))
spacebar.set_position((arrow_keys.x + arrow_keys.width + 50), arrow_keys.y + arrow_keys.height - spacebar.height)
selected_back_button.set_position(back_button.x, back_button.y)

chaoesquerda.set_position(0, (window.height - chaoesquerda.height))
pedraesq.set_position((chaoesquerda.x + chaoesquerda.width),
                      (chaoesquerda.y + chaoesquerda.height) - pedraesq.height)
mesa.set_position((pedraesq.x + pedraesq.width), (chaoesquerda.y + chaoesquerda.height) - mesa.height)
arvore1.set_position((mesa.x + mesa.width) - 20, (mesa.y + mesa.height) - arvore1.height)
pedradir.set_position((arvore1.x + arvore1.width) - 2, (chaoesquerda.y + chaoesquerda.height) - pedradir.height)
chaodireita.set_position((pedradir.x + pedradir.width), chaoesquerda.y)
ceu.set_position(0, 0)
nuvens.set_position(0, 0)

player_1["idle"].set_position(chaoesquerda.x + 20, (chaoesquerda.y - player_1["idle"].height) + 5)
player_2["idle"].set_position((chaodireita.x + chaodireita.width) - 80, (chaoesquerda.y - player_2["idle"].height)+ 5)
player_1["attack"].set_position(player_1["idle"].x, player_1["idle"].y)
player_2["attack"].set_position(player_2["idle"].x, player_2["idle"].y)


var = 0
poder = Sprite("spritesheet/gameplay/botaopower.png")
poder.set_position(player_1["idle"].x, player_1["idle"].y - 30)
marcador.set_position((poder.x + var), poder.y)

marcador2 = Sprite("spritesheet/gameplay/marcador.png")
poder2 = Sprite("spritesheet/gameplay/botaopower.png")
poder2.set_position(player_2["idle"].x, player_2["idle"].y - 30)
marcador2.set_position((poder2.x + var), poder2.y)

player_1["damage"].set_position(player_1["idle"].x, player_1["idle"].y)
player_2["damage"].set_position(player_2["idle"].x, player_2["idle"].y)


#endgame menu popup
bg = Sprite("spritesheet/endgame/bg.png")
fechar = Sprite("spritesheet/endgame/fechar.png")
main_menuu = Sprite("spritesheet/endgame/main menu.png")
playagain = Sprite("spritesheet/endgame/playagain.png")
p1wins = Sprite("spritesheet/endgame/p1wins.png")
p2wins = Sprite("spritesheet/endgame/p2wins.png")

bg.set_position((window.width - bg.width)/2, (window.height - bg.height)/2)
fechar.set_position(((bg.x + bg.width) - fechar.width), bg.y)
main_menuu.set_position((bg.x + bg.width) /2, (bg.y + bg.height)/2)
playagain.set_position(main_menuu.x, (main_menuu.y + main_menuu.height + 30))
p1wins.set_position((((bg.x + bg.width) - p1wins.width) /2) + 50, bg.y + 50)
p2wins.set_position((((bg.x + bg.width) - p1wins.width) /2) + 50, bg.y + 50)

chute = Sound("sons/chute.ogg")
dor = Sound("sons/HURT.ogg")
chute.load("sons/chute.ogg")
dor.load("sons/HURT.ogg")
chute.set_volume(100)
dor.set_volume(100)
chute.set_repeat(0)
dor.set_repeat(0)

player_1["attack"].stop()
player_2["attack"].stop()

trilhaMenu = Sound("sons/africa.ogg")
trilhaMenu.set_repeat(True)
trilhaMenu.set_volume(75)
trilhaMenu.stop()

trilhaJogo = Sound("sons/principeali.ogg")
trilhaJogo.set_repeat(True)
trilhaJogo.set_volume(75)
trilhaJogo.stop()