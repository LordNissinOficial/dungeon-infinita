import pygame as pg
import math

class Botao():
	def __init__(self, x, y, funcao=None, funcionarPressionando=False):
		self.funcionarPressionando = funcionarPressionando
		self.funcao = funcao
		self.funcaoSolto = None
		self.imgNormal = None
		self.imgPressionando = None
		if self.imgNormal:
			self.Rect = pg.Rect((x, y), self.img.get_size())
		else:
			self.Rect = pg.Rect((x, y), (16, 16))
		self.pressionado = False
	
	def setFuncao(self, funcao, funcionarPressionando):
		self.funcao = funcao
		self.funcionarPressionando = funcionarPressionando
	def setFuncaoSolto(self, funcao):
		self.funcaoSolto = funcao
		
	def pressionandoMouse(self, mousePos):
		if self.Rect.collidepoint(mousePos):
			if not self.pressionado:
				if self.funcao:
					self.funcao()
			self.pressionado = True
		else:
			self.pressionado = False
	
	def tirandoMouse(self, mousePos):
		if self.Rect.collidepoint(mousePos):
			self.pressionado = False
			if self.funcaoSolto:
				self.funcaoSolto()
	
	def update(self):
		if not self.pressionado or not self.funcionarPressionando:	return
		self.funcao()
		
	def show(self, display, spriteManager):
		if not self.pressionado and self.imgNormal:
			img = spriteManager.load("spritesheets/ui", self.imgNormal)
			img.set_alpha(80)
			display.blit(img, self.Rect)
		elif self.pressionado and self.imgPressionando:
			img = spriteManager.load("spritesheets/ui", self.imgPressionando)
			img.set_alpha(128)
			display.blit(img, self.Rect)
		else:
			pg.draw.rect(display, (120, 140, 120), self.Rect)

class Joystick:
	def __init__(self, x, y, area):
		self.area = area
		self.x = x
		self.y = y
		self.a = 0
		self.handlerX = x
		self.handlerY = y
		self.dedoPressionando = None
		self.poder = 0
		self.poderVerdadeiro = 0
		self.poderMaximo = self.area*0.6
	
	def anguloPara(self):
		deltaX = self.handlerX-self.x
		deltaY = self.handlerY-self.y
		rads = math.atan2(-deltaY, deltaX)
		rads %= 2*math.pi
		return -rads
	
	def dentro(self, dedo):
		return (dedo["x"]-self.x)**2 + (dedo["y"]-self.y)**2 < self.area**2
	
	def calcularDistancia(self):
		return math.sqrt((self.handlerX-self.x)**2 + (self.handlerY-self.y)**2)
		
	def pressionandoDedo(self, dedo):
		if self.dedoPressionando!=None and self.dedoPressionando!=dedo["id"]: return
		if not self.dedoPressionando!=None and not self.dentro(dedo): return

		self.dedoPressionando = dedo["id"]
		self.handlerX = dedo["x"]
		self.handlerY = dedo["y"]

		self.poderVerdadeiro = self.calcularDistancia()
		if self.poderVerdadeiro>self.poderMaximo:
			diff = self.poderMaximo-self.poderVerdadeiro
			angulo = self.anguloPara()
			self.handlerX += math.cos(angulo)*diff
			self.handlerY += math.sin(angulo)*diff
			self.poderVerdadeiro = self.poderMaximo
		self.poder = self.poderVerdadeiro/self.poderMaximo
		
	def tirandoDedo(self, dedo):
		if dedo["id"]!=self.dedoPressionando: return
		self.handlerX = self.x
		self.handlerY = self.y
		self.poder = 0
		self.poderVerdadeiro = 0
		self.dedoPressionando = None
		
	def show(self, display):
		pg.draw.circle(display, (237, 230, 200), (self.x, self.y), self.area+1, 7)
		pg.draw.circle(display, (128, 128, 120), (self.x, self.y), self.area, 5)
		
		pg.draw.circle(display, (237, 230, 200), (self.handlerX, self.handlerY), 8, 7)
		pg.draw.circle(display, (128, 128, 120), (self.handlerX, self.handlerY), 7)