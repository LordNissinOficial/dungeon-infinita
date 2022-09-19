import pygame as pg
from scripts.spritesheet import SpriteSheet

class MapaManager:
	def __init__(self):
		self.mapa = [
			[1, 2, 2, 2, 2, 2, 2, 3],
			[4, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 4],
			[6, 2, 2, 2, 2, 2, 2, 5]
		]
		spriteSheet = SpriteSheet("tilesets/tileset")		
		self.tiles = [spriteSheet.load(0, 0, 24, 24), spriteSheet.load(24, 0, 24, 24),
		spriteSheet.load(48, 0, 24, 24),
		spriteSheet.load(48+24, 0, 24, 24),
		spriteSheet.load(24, 24, 24, 24),
		spriteSheet.load(24*3, 48, 24, 24),
		spriteSheet.load(24, 48, 24, 24)]
		
	def show(self, display, camera):
		tiles = self.tiles
		mapa = self.mapa
		for y in range(len(self.mapa)):
			for x in range(len(self.mapa[0])):
				display.blit(tiles[mapa[y][x]], (x*24-camera.x, y*24-camera.y))