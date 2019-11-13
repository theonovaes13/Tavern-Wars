from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sound import *
from math import fabs
from math import sin
from math import cos
GAMESTATE = 2

contadorvidas1 = 0
contadorvidas2 = 0

abebebikila = 0
vidas1 = 3
vidas2 = 3

angulomira = 0
vez = 1
atirar = 1
atirou = 0
biri = 0
lancabomba = 0
power1 = 0
gravidade = 0
libera1 = 0
libera2 = 0

janela = Window(1280,700)
janela.set_title("TAVERN WARS")

rato = Window.get_mouse()
teclado = Window.get_keyboard()

#cenadomenu
placadomeio = Sprite("spritesheet/menu/placa central.png")
versus = Sprite("spritesheet/menu/bandeira esq.png")
challenge = Sprite("spritesheet/menu/bandeira dir.png")
botaoAudio = Sprite("spritesheet/menu/audio.png")
fundoMenu = GameImage("spritesheet/menu/fundomenu.png")
howtoplay = Sprite("spritesheet/menu/howto.png")
mudo = Sprite("spritesheet/menu/noaudio.png")
mousecima = Sprite("spritesheet/menu/mousecima.png")
play = Sprite("spritesheet/menu/play.png")
mouseplay = Sprite("spritesheet/menu/playcima.png")


#cenatutorial
fundohowto = Sprite("spritesheet/howtoplay/bg.png")
angulo = Sprite("spritesheet/howtoplay/angulo.png")
texto = Sprite("spritesheet/howtoplay/texto.png")
botaopower = Sprite("spritesheet/howtoplay/botaopower.png")
setas = Sprite("spritesheet/howtoplay/setadireita.png")
barra = Sprite("spritesheet/howtoplay/spacebar.png")
voltar = Sprite("spritesheet/howtoplay/config.png")
voltarselecionado = Sprite("spritesheet/howtoplay/voltarselecionado.png")

#versus
arvore1 = Sprite("spritesheet/gameplay/tileset/campos/arvore1.png")
chaoesquerda = Sprite("spritesheet/gameplay/tileset/campos/chao1.png")
chaodireita =  Sprite("spritesheet/gameplay/tileset/campos/chao1.png")
pedraesq = Sprite("spritesheet/gameplay/tileset/campos/pedraesq.png")
pedradir = Sprite("spritesheet/gameplay/tileset/campos/pedradir.png")
mesa = Sprite("spritesheet/gameplay/tileset/campos/mesa.png")
marcador = Sprite("spritesheet/gameplay/marcador.png")

player1idle = Animation("spritesheet/gameplay/idle pirata.png", 34, True)
player1idle.set_sequence_time(0,34, 60, True)
player1attack = Animation("spritesheet/gameplay/attack pirata.png", 12, True)
player1attack.set_sequence_time(0,12, 60, True)
player1dano = Animation("spritesheet/gameplay/danopirata.png", 8, True)
player1dano.set_sequence_time(0,8, 30, True)
player1attack.hide()
player1dano.hide()

player2idle = Animation("spritesheet/gameplay/pepino idle.png", 36, True)
player2idle.set_sequence_time(0, 35, 60, True)
player2attack = Animation("spritesheet/gameplay/pepino ataca.png", 11, True)
player2attack.set_sequence_time(0,11, 60, True)
player2dano = Animation("spritesheet/gameplay/danopepino.png", 8, True)
player2dano.set_sequence_time(0,8, 30, True)
player2attack.hide()
player2dano.hide()

bomba = Sprite("spritesheet/gameplay/bomba.png")

#versus - HUD
vida1 = Sprite("spritesheet/gameplay/HUD/barradevida1.png")
vida2 = Sprite("spritesheet/gameplay/HUD/barradevida2.png")
vida1.set_position(10,10)
vida2.set_position((janela.width - vida2.width)- 10, 10)

mira = Sprite("spritesheet/gameplay/mira.png")

#background
ceu = Sprite("spritesheet/gameplay/tileset/background/ceu.png")
nuvens = Sprite("spritesheet/gameplay/tileset/background/nuvens.png")









#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~









#menu
placadomeio.set_position((janela.width - placadomeio.width)/2, 0)
versus.set_position(0, 40)
challenge.set_position(placadomeio.width + placadomeio.x + (placadomeio.x - versus.width), 40)
botaoAudio.set_position(5, janela.height - botaoAudio.height - 5)
howtoplay.set_position((janela.width - howtoplay.width)/2, placadomeio.height + 60)
mudo.set_position(botaoAudio.x, botaoAudio.y)
mousecima.set_position(howtoplay.x, howtoplay.y)
play.set_position((janela.width - play.width)/2,(howtoplay.y + howtoplay.height) + 10)
mouseplay.set_position(play.x, play.y)

#tutorial
angulo.set_position(40,40)
texto.set_position(angulo.x + 500, 100)

voltar.set_position(50, (janela.height - voltar.height - 50))
setas.set_position(texto.x, (texto.y + texto.height + 50))
barra.set_position((setas.x + setas.width + 50), setas.y + setas.height - barra.height)
voltarselecionado.set_position(voltar.x, voltar.y)

chaoesquerda.set_position(0, (janela.height - chaoesquerda.height))
pedraesq.set_position((chaoesquerda.x + chaoesquerda.width),
                      (chaoesquerda.y + chaoesquerda.height) - pedraesq.height)
mesa.set_position((pedraesq.x + pedraesq.width), (chaoesquerda.y + chaoesquerda.height) - mesa.height)
arvore1.set_position((mesa.x + mesa.width) - 20, (mesa.y + mesa.height) - arvore1.height)
pedradir.set_position((arvore1.x + arvore1.width) - 2, (chaoesquerda.y + chaoesquerda.height) - pedradir.height)
chaodireita.set_position((pedradir.x + pedradir.width), chaoesquerda.y)
ceu.set_position(0, 0)
nuvens.set_position(0, 0)

player1idle.set_position(chaoesquerda.x + 20, (chaoesquerda.y - player1idle.height) + 5)
player2idle.set_position((chaodireita.x + chaodireita.width) - 80, (chaoesquerda.y - player2idle.height)+ 5)
player1attack.set_position(player1idle.x, player1idle.y)
player2attack.set_position(player2idle.x, player2idle.y)


var = 0
poder = Sprite("spritesheet/gameplay/botaopower.png")
poder.set_position(player1idle.x, player1idle.y - 30)
marcador.set_position((poder.x + var), poder.y)

marcador2 = Sprite("spritesheet/gameplay/marcador.png")
poder2 = Sprite("spritesheet/gameplay/botaopower.png")
poder2.set_position(player2idle.x, player2idle.y - 30)
marcador2.set_position((poder2.x + var), poder2.y)

player1dano.set_position(player1idle.x, player1idle.y)
player2dano.set_position(player2idle.x, player2idle.y)


#endgame menu popup
bg = Sprite("spritesheet/endgame/bg.png")
fechar = Sprite("spritesheet/endgame/fechar.png")
mainmenuu = Sprite("spritesheet/endgame/main menu.png")
playagain = Sprite("spritesheet/endgame/playagain.png")
p1wins = Sprite("spritesheet/endgame/p1wins.png")
p2wins = Sprite("spritesheet/endgame/p2wins.png")

bg.set_position((janela.width - bg.width)/2, (janela.height - bg.height)/2)
fechar.set_position(((bg.x + bg.width) - fechar.width), bg.y)
mainmenuu.set_position((bg.x + bg.width) /2, (bg.y + bg.height)/2)
playagain.set_position(mainmenuu.x, (mainmenuu.y + mainmenuu.height + 30))
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

player1attack.stop()
player2attack.stop()

trilhaMenu = Sound("sons/africa.ogg")
trilhaMenu.set_repeat(True)
trilhaMenu.set_volume(75)
trilhaMenu.stop()

trilhaJogo = Sound("sons/principeali.ogg")
trilhaJogo.set_repeat(True)
trilhaJogo.set_volume(75)
trilhaJogo.stop()