from pygame import Rect
from pygame.math import Vector2
from scripts.animacaoManager import AnimacaoManager
 
class Entidade():
	def __init__(self, x, y, jogo):
		self.animacaoManager = AnimacaoManager(jogo.spriteManager)

		self.eJogador = False
		self.andarAutomatico = 0
		self.largura = 1
		self.moverCount = 0
		self.moveuCount = 0
		self.altura = 1
		self.x = x
		self.y = y
		self.xMovendo = x
		self.warpPraIr = None
		self.yMovendo = y
		self.movendo = [False, [0, 1]]
		self.dentroDeWarp = None #id do warp que usou para nao entrar num warp enquanto sai dele.
	
	def updateAnimacao(self):
		if self.movendo[0]:
			if self.movendo[1][0]==1 and self.animacaoManager.animacaoNome!="andar direita":
				self.animacaoManager.ativar("andar direita")
			elif self.movendo[1][0]==-1 and self.animacaoManager.animacaoNome!="andar esquerda":		
				self.animacaoManager.ativar("andar esquerda")
			elif self.movendo[1][1]==1 and self.animacaoManager.animacaoNome!="andar baixo":
				self.animacaoManager.ativar("andar baixo")
			elif self.movendo[1][1]==-1 and self.animacaoManager.animacaoNome!="andar cima":
				self.animacaoManager.ativar("andar cima")
		else:
			if self.movendo[1][0]==1 and self.animacaoManager.animacaoNome!="parado direita":
				self.animacaoManager.ativar("parado direita")
			elif self.movendo[1][0]==-1 and self.animacaoManager.animacaoNome!="parado esquerda":		
				self.animacaoManager.ativar("parado esquerda")
			elif self.movendo[1][1]==1 and self.animacaoManager.animacaoNome!="parado baixo":
				self.animacaoManager.ativar("parado baixo")
			elif self.movendo[1][1]==-1 and self.animacaoManager.animacaoNome!="parado cima":
				self.animacaoManager.ativar("parado cima")
				
	def mover(self, x, y, jogo, continuarMovendo=False):
#		if x and y:
#			self.x += int(x*1.5)
#			self.y += int(y*1.5)
#		else:
		if x!=0 or y!=0:
			vec = Vector2(x, y)
			vec.scale_to_length(3)
			self.x += int(vec.x)
			self.y += int(vec.y)
		
	def podeMover(self, x, y, jogo):
		pass
		
	def updateMovimento(self, jogo):
		pass
		
	def emWarp(self, jogo, rect, entrar=True):
		pass
						
	def update(self, jogo):
		self.updateAnimacao()
		self.animacaoManager.update()
		self.updateMovimento(jogo)

	def show(self, display, camera, offsetX, offsetY):
		x = self.xMovendo-camera.x
		y = self.yMovendo-camera.y-4
		display.blit(self.animacaoManager.conseguirSprite(), (x, y))