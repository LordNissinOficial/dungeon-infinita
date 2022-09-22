import pygame as pg
import random
from scripts.spritesheet import SpriteSheet
from scripts.config import *

class MapaManager:
	def __init__(self):
		self.mapa = []
		spriteSheet = SpriteSheet("tilesets/tileset")		
		self.tiles = [spriteSheet.load(0, 0, 24, 24), spriteSheet.load(24, 0, 24, 24),
		spriteSheet.load(48, 0, 24, 24),
		spriteSheet.load(48+24, 0, 24, 24),
		spriteSheet.load(24, 24, 24, 24),
		spriteSheet.load(24*3, 48, 24, 24),
		spriteSheet.load(24, 48, 24, 24)]
	
	def gerarLevel(self):
		mapaLargura = 100
		mapaAltura = 100
		self.mapa = [[-1 for i in range(mapaLargura)] for j in range(mapaAltura)]
		subDungeons = [[0, 0, len(self.mapa[0]), len(self.mapa)]]
		subDungeonsAtuais = [*self.cortarDungeon(subDungeons[0])]
		acabarGeracao = False
		while not acabarGeracao:
			subDungeonsAtuaisCopia = list(subDungeonsAtuais)
			subDungeonsAtuais = []
			for subDungeon in subDungeonsAtuaisCopia:
				novasDungeons = self.cortarDungeon(subDungeon)
				for d in novasDungeons:
					if d[2]<=10 or d[3]<=10:
						acabarGeracao = True
				subDungeonsAtuais.append(novasDungeons[0])
				subDungeonsAtuais.append(novasDungeons[1])
		
		for subDungeon in list(subDungeonsAtuais):
			index = subDungeonsAtuais.index(subDungeon)
			naoAdicionar = random.randint(1, 100)<20 if len(subDungeonsAtuais)>10 else False
			if len(subDungeonsAtuais)>15:
				naoAdicionar=random.randint(1, 100)<40
				
			novaLargura = random.randint(max(4, subDungeon[2]//2), subDungeon[2])
			novaAltura = random.randint(max(4, subDungeon[3]//2), subDungeon[3])
			subDungeon = [subDungeon[0]+(subDungeon[2]-novaLargura), subDungeon[1]+(subDungeon[3]-novaAltura), novaLargura, novaAltura]
			subDungeonsAtuais[index] = subDungeon
			if naoAdicionar:
				del subDungeonsAtuais[subDungeonsAtuais.index(subDungeon)]		
			self.adicionarMapa(subDungeon, naoAdicionar)
			
		self.show1()
		d = random.choice(subDungeonsAtuais)
		return (random.randint(d[0]+1, (d[0]+d[2]-2))*24, random.randint(d[1]+1, d[1]+d[3]-2)*24)
	
	def adicionarMapa(self, subDungeon, naoAdicionar):		
		cor  = (random.randint(30, 240), 100, random.randint(30, 240))
		if subDungeon[3]==0 or subDungeon[2]==0: print("ss", subDungeon)
		for y in range(subDungeon[3]):
			for x in range(subDungeon[2]):
				if y==0 or x==0 or x==subDungeon[2]-1 or y==subDungeon[3]-1:
					parede = True
				else:
					parede = False
				if not naoAdicionar:
					if parede:
						self.mapa[subDungeon[1]+y][subDungeon[0]+x] = parede
					else:
						self.mapa[subDungeon[1]+y][subDungeon[0]+x] = parede

	def cortarDungeon(self, dungeon):
		if random.randint(0, 1)==0:
			offset = random.randint(int(dungeon[2]*0.45), int(dungeon[2]*0.55))
			return [[dungeon[0], dungeon[1], offset, dungeon[3]], [dungeon[0]+offset, dungeon[1], dungeon[2]-offset, dungeon[3]]]
		else:
			offset = random.randint(int(dungeon[3]*0.45), int(dungeon[3]*0.55))
			return [[dungeon[0], dungeon[1], dungeon[2], offset], [dungeon[0], dungeon[1]+offset, dungeon[2], dungeon[3]-offset]]
	
	def show1(self):
		tiles = self.tiles
		mapa = self.mapa
		self.display = pg.Surface((len(mapa[0])*24, len(mapa)*24)).convert()
		for y in range(len(mapa)):
			for x in range(len(mapa[0])):
				if mapa[y][x]==-1:
					pg.draw.rect(self.display, (52, 49, 29), (x*24, y*24, 24, 24))
					continue
				walls = {(0, 1): False, (0, -1): False, (1, 0): False, (-1, 0): False}
				eParede = mapa[y][x]
				for pos in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
					try:
						walls[pos] = mapa[y+pos[1]][x+pos[0]]==1
					except:
						walls[pos] = False
				tile = 0
				if eParede:
					if (walls[(0, -1)] and walls[(0, 1)]) and not (walls[(1, 0)] or walls[(-1, 0)]): tile=4
					elif (walls[(-1, 0)] and walls[(1, 0)]) and not (walls[(0, 1)] or walls[(0, -1)]): tile=2
					elif (walls[(1, 0)] and walls[(0, -1)]) and not (walls[(-1, 0) or walls[(0, -1)]]): tile=6
					elif (walls[(-1, 0)] and walls[(0, -1)]) and not (walls[(1, 0) or walls[(0, -1)]]): tile=5
					elif (walls[(1, 0)] and walls[(0, 1)]) and not (walls[(-1, 0) or walls[(0, 1)]]): tile=1
					elif (walls[(-1, 0)] and walls[(0, 1)]) and not (walls[(1, 0) or walls[(0, 1)]]): tile=3
				self.display.blit(tiles[tile], (x*24, y*24))
				
	def show(self, display, camera):
		display.blit(self.display, (-camera.x, -camera.y))	