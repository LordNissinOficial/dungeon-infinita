from pygame import event
from pygame import (Surface, image, draw)
from pygame.font import (Font, init)
from pygame.transform import (scale, flip)
from enum import Enum
from scripts.jogo import Jogo
from scripts.transicao import (Transicao)
from scripts.spriteManager import SpriteManager

from scripts.config import *

init()

class CenaManager():
	
	"""classe principal que cuida do jogo atual"""	
	def __init__(self):
		self.scale = 6
		
		#self.setBotoes() 
		self.spriteManager = SpriteManager()
		self.transicao = Transicao()
		self.estados = {estado: ESTADOS.estadosClasses.value[estado](self) for estado in ESTADOS.estados.value}
		for estado in self.estados:
			self.estados[estado].cenaManager = self
		self.setJogo(ESTADOS.JOGO)
		self.rodando = 1	


	def fade(self, funcao=None):

		self.transicao = Transicao()
		if not self.transicao.fading:
			self.transicao.fadeOut(funcao)

	def fadeBatalha(self):
		self.transicao = TransicaoBatalha()
		if not self.transicao.fading:
			self.transicao.fadeOut(lambda: self.setJogo(ESTADOS.LUTA))
			
	def fadein(self):
		self.transicao.fadeIn()
		
	"""decide o jogo atual"""
	def setJogo(self, ESTADO):
		self.estado  = ESTADO.value
		self.estados[self.estado].setUp(self)
					
	"""updatea o jogo atual"""
	def update(self):
		if not self.rodando: return
		self.estados[self.estado].lidarEventos(event.get())
		self.estados[self.estado].update(self)
		if self.transicao.fading:
			if self.transicao.fadeout:
				self.transicao.update()
				if self.transicao.fadein:
					self.estados[self.estado].show()					
				return
			else:
				self.transicao.update()		

	
	"""desenha na tela o display do jogo atual"""
	def show(self, tela):
		if not self.rodando: return
		self.estados[self.estado].show()
		#self.showUi()
		if self.transicao.fading:			
			if self.transicao.fadeout:
				displayCopia = self.estados[self.estado].display.copy()
			else:
				self.estados[self.estado].show()
				#self.showUi()
				displayCopia = self.estados[self.estado].display.copy()

			self.transicao.show(displayCopia)
			scale(displayCopia, TELA_TAMANHO, tela)
			return
#		if self.aaa:
#			tela.fill((0, 0, 0))
#			tela.blit(scale(self.estados[self.estado].display, (int(256*self.scale), int(144*self.scale))), (int(1920-256*self.scale)/2, int(1080-144*self.scale)/2))
		#else:
		scale(self.estados[self.estado].display, TELA_TAMANHO, tela)

		
class ESTADOS(Enum):
	JOGO = 0
	estados = [JOGO]#, LUTA, MENUPRINCIPAL
	estadosClasses = [Jogo]#MenuPrincipal, MenuConfiguracoes]
		