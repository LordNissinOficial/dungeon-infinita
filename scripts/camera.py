from pygame.math import Vector2
from scripts.config import *

class Camera:
	def __init__(self):
		self.x = 0
		self.xAntigo = 0
		self.y = 0
		self.yAntigo = 0

		self.largura = int(DISPLAY_TAMANHO[0]//16)
		self.altura = int(DISPLAY_TAMANHO[1]//16)
		print(self.largura, self.altura)
	
	def moverPara(self, x, y):

		self.xAntigo = self.x
		self.yAntigo = self.y
		novoX = (self.x - (x-DISPLAY_TAMANHO[0]//2))
		novoY = (self.y - (y-DISPLAY_TAMANHO[1]//2))	
		self.x -= novoX/5
		self.y -= novoY/5
		if abs(novoX)<1:
			self.x -= novoX
		if abs(novoY)<1:
			self.y -= novoY
		self.x = int(self.x)
		self.y = int(self.y)
		
	def mudouPosicao(self):
		x = self.x//16
		xAntigo = self.xAntigo//16
		y = self.y//16
		yAntigo = self.yAntigo//16
		return xAntigo!=x or yAntigo!=y