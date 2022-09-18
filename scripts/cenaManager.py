from pygame import event
from pygame import (Surface, image, draw)
from pygame.font import (Font, init)
from pygame.transform import (scale, flip)
from pygame.locals import (QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP)
from enum import Enum
from scripts.jogo import Jogo
from scripts.transicao import (Transicao)
from scripts.uiComponentes import Botao
from scripts.spriteManager import SpriteManager

from scripts.config import *

init()

class CenaManager():
	
	"""classe principal que cuida do jogo atual"""	
	def __init__(self):
		self.scale = 6
		self.botoes = {}
		self.setBotoes() 
		self.spriteManager = SpriteManager()
		self.transicao = Transicao()
		self.estados = {estado: ESTADOS.estadosClasses.value[estado](self) for estado in ESTADOS.estados.value}
		for estado in self.estados:
			self.estados[estado].cenaManager = self
		self.setJogo(ESTADOS.JOGO)
		self.rodando = 1
		event.set_blocked(None)
		event.set_allowed([QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION])

	def setBotoes(self):
		botoes = self.botoes
		botoes["cima"] = Botao(16+4, DISPLAY_TAMANHO_REAL[1]-56+4)
		botoes["cima"].imgNormal = (4, 0, 2, 2)
		botoes["cima"].imgPressionando = (4, 2, 2, 2)
		
		botoes["baixo"] = Botao(16+4, DISPLAY_TAMANHO_REAL[1]-24+4)
		botoes["baixo"].imgNormal = (6, 0, 2, 2)
		botoes["baixo"].imgPressionando = (6, 2, 2, 2)
		
		botoes["esquerda"] = Botao(4, DISPLAY_TAMANHO_REAL[1]-40+4)
		botoes["esquerda"].imgNormal = (0, 0, 2, 2)
		botoes["esquerda"].imgPressionando = (0, 2, 2, 2)
		
		botoes["direita"] = Botao(32+4, DISPLAY_TAMANHO_REAL[1]-40+4)
		botoes["direita"].imgNormal = (2, 0, 2, 2)
		botoes["direita"].imgPressionando = (2, 2, 2, 2)
		
		botoes["b"] = Botao(DISPLAY_TAMANHO[0]-32-14, DISPLAY_TAMANHO_REAL[1]-24+4)
		botoes["b"].imgNormal = (8, 0, 2, 2)
		botoes["b"].imgPressionando = (8, 2, 2, 2)
		
		botoes["a"] = Botao(DISPLAY_TAMANHO[0]-16-4, DISPLAY_TAMANHO_REAL[1]-24+4)
		botoes["a"].imgNormal = (10, 0, 2, 2)
		botoes["a"].imgPressionando = (10, 2, 2, 2)
		
	def fade(self, funcao=None):
		for botao in self.botoes:
			self.botoes[botao].pressionado = False
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
		for botao in self.botoes:
			self.botoes[botao].pressionado = False
	
	def lidarEventos(self):
		for evento in event.get():
			if evento.type==QUIT:
				self.rodando = False
			elif evento.type in [MOUSEBUTTONDOWN, MOUSEMOTION] and not self.transicao.fading:
				pos = telaParaDisplay(*evento.pos)
				for botao in self.botoes:
					self.botoes[botao].pressionandoMouse(pos)
				
			elif evento.type==MOUSEBUTTONUP and not self.transicao.fading:
				pos = telaParaDisplay(*evento.pos)
				for botao in self.botoes:
					self.botoes[botao].tirandoMouse(pos)
					
	"""updatea o jogo atual"""
	def update(self):
		if not self.rodando: return
		self.lidarEventos()
		self.estados[self.estado].update(self)
		if self.transicao.fading:
			if self.transicao.fadeout:
				self.transicao.update()
				if self.transicao.fadein:
					self.estados[self.estado].show()					
				return
			else:
				self.transicao.update()
		else:
			for botao in self.botoes:
				self.botoes[botao].update()

	
	"""desenha na tela o display do jogo atual"""
	def show(self, tela):
		if not self.rodando: return
		self.estados[self.estado].show()
		self.showUi()
		if self.transicao.fading:			
			if self.transicao.fadeout:
				displayCopia = self.estados[self.estado].display.copy()
			else:
				self.estados[self.estado].show()
				self.showUi()
				displayCopia = self.estados[self.estado].display.copy()

			self.transicao.show(displayCopia)
			scale(displayCopia, TELA_TAMANHO, tela)
			return
#		if self.aaa:
#			tela.fill((0, 0, 0))
#			tela.blit(scale(self.estados[self.estado].display, (int(256*self.scale), int(144*self.scale))), (int(1920-256*self.scale)/2, int(1080-144*self.scale)/2))
		#else:
		scale(self.estados[self.estado].display, TELA_TAMANHO, tela)
	
	def showUi(self):
		for botao in self.botoes:
			self.botoes[botao].show(self.estados[self.estado].display, self.spriteManager)

		
class ESTADOS(Enum):
	JOGO = 0
	estados = [JOGO]#, LUTA, MENUPRINCIPAL
	estadosClasses = [Jogo]#MenuPrincipal, MenuConfiguracoes]
	
def telaParaDisplay(x, y):
	return [int(x/TELA_TAMANHO[0]*DISPLAY_TAMANHO_REAL[0]),
				int(y/TELA_TAMANHO[1]*DISPLAY_TAMANHO_REAL[1])]		