import pygame as pg
from scripts.mapaManager import MapaManager
import random
tela = pg.display.set_mode((1920, 1080))
display = pg.Surface((100, 100)).convert()
mapaManager = MapaManager()
mapaManager.gerarLevel()
while True:
	for event in pg.event.get():
		if event.type==pg.MOUSEBUTTONUP:
			mapaManager.gerarLevel()
	for y in range(100):
			for x in range(100):
#				random.seed()
				r = random.randint(30, 240)
				#cor = (r, r, r) if mapaManager.mapa[y][x][0] else (50, 50, 80)
		#		if type(mapaManager.mapa[y][x])==list:
#					display.set_at((x, y), mapaManager.mapa[y][x][1])
#				else:
					display.set_at((x, y), (mapaManager.mapa[y][x]*215, 0, 0))
		
	tela.blit(pg.transform.scale(display, (100*10, 100*10)), (200, 20))
	pg.display.update()