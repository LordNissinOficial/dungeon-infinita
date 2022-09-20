import pygame as pg
import random
from scripts.spritesheet import SpriteSheet

class MapaManager:
	def __init__(self):
		self.mapa = []
		#	[1, 2, 2, 2, 2, 2, 2, 3],
#			[4, 0, 0, 0, 0, 0, 0, 4],
#			[4, 0, 0, 0, 0, 0, 0, 4],
#			[4, 0, 0, 0, 0, 0, 0, 4],
#			[4, 0, 0, 0, 0, 0, 0, 4],
#			[4, 0, 0, 0, 0, 0, 0, 4],
#			[4, 0, 0, 0, 0, 0, 0, 4],
#			[6, 2, 2, 2, 2, 2, 2, 5]
#		]
		spriteSheet = SpriteSheet("tilesets/tileset")		
		self.tiles = [spriteSheet.load(0, 0, 24, 24), spriteSheet.load(24, 0, 24, 24),
		spriteSheet.load(48, 0, 24, 24),
		spriteSheet.load(48+24, 0, 24, 24),
		spriteSheet.load(24, 24, 24, 24),
		spriteSheet.load(24*3, 48, 24, 24),
		spriteSheet.load(24, 48, 24, 24)]
	
	def gerarLevel(self):
		mapaLargura = random.choice([30, 40, 60])
		mapaAltura = random.choice([30, 40, 60])
		self.mapa = [[0 for i in range(mapaLargura)] for j in range(mapaAltura)]
		subDungeons = [[0, 0, len(self.mapa[0]), len(self.mapa)]]
		subDungeonsAtuais = [*self.cortarDungeon(subDungeons[0])]
		#subDungeon
		for i in range(4):
			subDungeonsAtuaisCopia = list(subDungeonsAtuais)
			subDungeonsAtuais = []
			for subDungeon in subDungeonsAtuaisCopia:
				novasDungeons = self.cortarDungeon(subDungeon)
				
				subDungeonsAtuais.append(novasDungeons[0])
				subDungeonsAtuais.append(novasDungeons[1])
			#print('nvs', subDungeonsAtuais)
		#print(subDungeonsAtuais)
		
	def cortarDungeon(self, dungeon):
		if random.randint(0, 1)==0:
			#print("d1", dungeon)
			offset = random.randint(int(dungeon[2]*0.2), int(dungeon[2]*0.8))
			return [[dungeon[0], dungeon[1], offset, dungeon[3]], [dungeon[0]+offset, dungeon[1], dungeon[2]-offset, dungeon[3]]]
			
			#[[dungeon[0], dungeon[1], offset, dungeon[3]], [dungeon[0]+offset, dungeon[1], dungeon[0]-offset, dungeon[3]]
		else:
			#print("d2", dungeon)
			offset = random.randint(int(dungeon[3]*0.2), int(dungeon[3]*0.8))
			return [[dungeon[0], dungeon[1], dungeon[2], offset], [dungeon[0], dungeon[1]+offset, dungeon[2], dungeon[3]-offset]]

	def show(self, display, camera):
		tiles = self.tiles
		mapa = self.mapa
		for y in range(len(mapa)):
			for x in range(len(mapa[0])):
				display.blit(tiles[mapa[y][x]], (x*24-camera.x, y*24-camera.y))
		