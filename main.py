from pygame.font import (init, SysFont)
from pygame.time import Clock
from pygame.display import (set_mode, update)
from pygame.locals import (DOUBLEBUF, FULLSCREEN)
from scripts.cenaManager import CenaManager
from profilehooks import profile

init()

#@profile(filename="profile.prof")
def main():
	frame = 0
	fps = 300
	flags = DOUBLEBUF|FULLSCREEN
	tela = set_mode((1920, 1080), flags, 16)
	fonte = SysFont("Calibri", 16)
	cenaManager = CenaManager()
	tela.fill((203, 203, 203))
	clock = Clock()
	while cenaManager.rodando:
		cenaManager.update()
		cenaManager.show(tela)
		jogo = cenaManager.estados[cenaManager.estado]		
#		tela.blit(fonte.render(str(round(clock.get_fps())), 0, (237, 230, 200), (52, 49, 29)), (40, 40))
#		tela.blit(fonte.render(str((jogo.botoes["joystick"].poderX, jogo.botoes["joystick"].poderY)), 0, (100, 255, 255), (0, 0, 0)), (40, 60))
#		tela.blit(fonte.render(str((jogo.botoes["joystick"].handlerX, jogo.botoes["joystick"].handlerY)), 0, (100, 255, 255), (0, 0, 0)), (40, 80))
		update()
		clock.tick(fps)

main()