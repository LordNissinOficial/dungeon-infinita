from pygame import (Surface, event)
from scripts.config import *
from scripts.camera import Camera
from scripts.jogador import Jogador
from scripts.mapaManager import MapaManager
from scripts.uiComponentes import Joystick
from pygame import (QUIT, FINGERDOWN, FINGERUP, FINGERMOTION)
import math

class Jogo():
	def __init__(self, cenaManager):
		self.spriteManager = cenaManager.spriteManager
		self.spriteManager.load("spritesheets/ui")
		self.mapaManager = MapaManager()
		self.dedos = {}
		self.botoes = {}
		self.camera = Camera()	
		self.jogador = Jogador(48, 48, self)
		self.display = Surface(DISPLAY_TAMANHO).convert()
		self.mapaDisplay = Surface((DISPLAY_TAMANHO)).convert()
		#self.mapaManager = MapaManager(self.camera,  self)
		self.botoes = {}
		self.mapaManager.gerarLevel()
	
	def setUp(self, cenaManager):
		event.set_blocked(None)
		event.set_allowed([QUIT, FINGERDOWN, FINGERUP, FINGERMOTION])
		self.setUpBotoes(cenaManager)
		
	def setUpBotoes(self, cenaManager):
		self.botoes["joystick"] = Joystick(40, DISPLAY_TAMANHO[1]-40, 30)
	
	def moverJogador(self, x, y):
		self.jogador.mover(x, y, self)
		
	def a(self):
		pass
		
	def aSolto(self):
		pass
		
	def fade(self, funcao, warp):
		pass
		#self.cenaManager.fade(lambda: self.jogadorWarp(funcao, warp))
	
	def fadein(self):
		pass
		#self.cenaManager.fadein(self.jogadorWarp)

	def fadeBatalha(self):
		self.cenaManager.fadeBatalha()
		
	def jogadorWarp(self, funcao, warpId):
		funcao()
		for funcao in self.mapaManager.mapas["centro"].funcoes:
			if funcao.type=="warp":
				for propriedade in funcao.properties:
					if propriedade.name=="id" and propriedade.value==warpId:
						warp = funcao
						break
		for propriedade in warp.properties:
			if propriedade.name=="direcao":
				direcao = list(map(int, propriedade.value.split(",")))

		novoX, novoY = (warp.x, warp.y)
		self.jogador.x = novoX
		self.jogador.xMovendo = novoX
		self.jogador.y = novoY
		self.jogador.yMovendo = novoY
		self.jogador.movendo[1] = direcao
		self.jogador.updateAnimacao()
		self.jogador.andarAutomatico = 1
	
	def lidarEventos(self, eventos):
		for evento in eventos:
			#print(23)
			if evento.type==QUIT:
				self.rodando = False
			elif evento.type in [FINGERDOWN, FINGERMOTION]:
				dedo = {"id": evento.finger_id, "x": int(evento.x*DISPLAY_TAMANHO[0]), "y": int(evento.y*DISPLAY_TAMANHO[1])}
				self.dedos[dedo["id"]] = dedo
				for botao in self.botoes:
					self.botoes[botao].pressionandoDedo(dedo)
				
			elif evento.type==FINGERUP:
				dedo = {"id": evento.finger_id, "x": int(evento.x*DISPLAY_TAMANHO[0]), "y": int(evento.y*DISPLAY_TAMANHO[1])}
				if dedo["id"] in self.dedos.keys():
					del self.dedos[dedo["id"]]
				for botao in self.botoes:
					self.botoes[botao].tirandoDedo(dedo)
					
	def update(self, cenaManager):

		if not cenaManager.transicao.fading:
			self.jogador.update(self)
			#self.mapaManager.update(self)

		else:
			pass
			#self.jogador.movendo[0] = False
#			self.jogador.x = self.jogador.xMovendo
#			self.jogador.y = self.jogador.yMovendo
		angulo = self.botoes["joystick"].anguloPara()
		self.moverJogador(math.cos(angulo)*self.botoes["joystick"].poder, math.sin(angulo)*self.botoes["joystick"].poder)
		self.camera.moverPara(self.jogador.x, self.jogador.y)
		
		#self.mapaManager.updateAnimacoes(self.camera)
	
	def checarGrama(self, x, y):
		if self.mapaManager.mapas["centro"].grid[0][y//16][x//16]==25:
			if random.randint(1, 100)<=15:
				self.fadeBatalha()

	def show(self):
		self.display.fill((52, 49, 29))		
#		if self.camera.mudouPosicao() or True:
#			self.mapaManager.updateDisplay(self.camera)

		#self.mapaManager.show(self.display)
		#self.jogador.show(self.display, self.camera, self.mapaManager.mapas["centro"].offsetX, self.mapaManager.mapas["centro"].offsetY)
		self.mapaManager.show(self.display, self.camera)
		self.jogador.show(self.display, self.camera)
		for botao in self.botoes.values():
			botao.show(self.display)
#		if self.dialogoManager.emDialogo:
#			self.dialogoManager.show(self.display)
