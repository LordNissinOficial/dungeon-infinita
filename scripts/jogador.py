import pygame as pg
from scripts.entidade import Entidade

class Jogador(Entidade):
	def __init__(self, x, y, jogo):
		Entidade.__init__(self, x, y, jogo)
		self.img = pg.image.load("recursos/sprites/jogador.png").convert_alpha()
		self.movendo[1] = [1, 0]
		self.eJogador = True
		
	def update(self, jogo):
		pass
		
	def show(self, display, camera):
#		x = 5
#		y = 10
		x, y = (self.x-camera.x, self.y-camera.y)
		display.blit(self.img, (x, y))