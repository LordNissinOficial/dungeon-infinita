import pygame as pg
from scripts.entidade import Entidade

class Jogador(Entidade):
	def __init__(self, x, y, jogo):
		Entidade.__init__(self, x, y, jogo)
		self.img = pg.image.load("recursos/sprites/jogador.png").convert_alpha()
#		self.img2 = pg.image.load("recursos/sprites/jogador2.png").convert_alpha()
#		self.img3 = pg.image.load("recursos/sprites/jogador1.png").convert_alpha()
		self.movendo[1] = [1, 0]
		self.eJogador = True
		
	def update(self, jogo):
		pass
		
	def show(self, display, camera):
#		x = 5
#		y = 10
		x, y = (self.x-camera.x, self.y-camera.y)
		display.blit(self.img, (x, y))
#		display.blit(self.img2, (x+16, y+8))
#		display.blit(self.img3, (x+16+24, y))