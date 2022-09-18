from pygame import Surface
from scripts.config import *
from scripts.camera import Camera
from scripts.jogador import Jogador

class Jogo():
	def __init__(self, cenaManager):
		self.spriteManager = cenaManager.spriteManager
		self.spriteManager.load("spritesheets/ui")
		self.camera = Camera()	
		self.jogador = Jogador(192-16, 108-16, self)
		self.display = Surface(DISPLAY_TAMANHO).convert()
		self.mapaDisplay = Surface((DISPLAY_TAMANHO)).convert()
		#self.mapaManager = MapaManager(self.camera,  self)
		self.botoes = {}
	
	def setUp(self, cenaManager):
		self.setUpBotoes(cenaManager)
		
	def setUpBotoes(self, cenaManager):
		cenaManager.botoes["cima"].setFuncao(lambda: self.moverJogador(0, -1), True)
		cenaManager.botoes["baixo"].setFuncao(lambda: self.moverJogador(0, 1), True)
		cenaManager.botoes["esquerda"].setFuncao(lambda: self.moverJogador(-1, 0), True)
		cenaManager.botoes["direita"].setFuncao(lambda: self.moverJogador(1, 0), True)
		
		cenaManager.botoes["b"].setFuncao(None, False)
		cenaManager.botoes["a"].setFuncao(self.a, False)
		cenaManager.botoes["a"].setFuncaoSolto(self.aSolto)
	
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
		
	def update(self, cenaManager):

		if not cenaManager.transicao.fading:
			self.jogador.update(self)
			#self.mapaManager.update(self)

		else:
			pass
			#self.jogador.movendo[0] = False
#			self.jogador.x = self.jogador.xMovendo
#			self.jogador.y = self.jogador.yMovendo
		self.camera.moverPara(self.jogador.x, self.jogador.y)
		
		#self.mapaManager.updateAnimacoes(self.camera)
	
	def checarGrama(self, x, y):
		if self.mapaManager.mapas["centro"].grid[0][y//16][x//16]==25:
			if random.randint(1, 100)<=15:
				self.fadeBatalha()

	def show(self):
		self.display.fill((55, 58, 62))		
#		if self.camera.mudouPosicao() or True:
#			self.mapaManager.updateDisplay(self.camera)

		#self.mapaManager.show(self.display)
		#self.jogador.show(self.display, self.camera, self.mapaManager.mapas["centro"].offsetX, self.mapaManager.mapas["centro"].offsetY)
		self.jogador.show(self.display, self.camera)
#		if self.dialogoManager.emDialogo:
#			self.dialogoManager.show(self.display)