#-*- coding: euc-kr -*-
import os, sys
import time

class ScreenCon:
	mapscreen = []
	curscreen = []

	def __init__(self):
		self.tmap = []
		self.WIDTH = 0
		self.HEIGHT = 0

	def setxy(self, x, y, s):
		#self.curscreen[y] = self.curscreen[y][0:x] + s + self.curscreen[y][x+len(s):]
		self.tmap[y][x] = s
		#printscreen(screen)

	def move(self, x, y, tox, toy, s):
		temps = self.tmap[y][x]
		self.setxy(x, y, s)
		self.printmap()
		time.sleep(0.5)
		for num in range(1, tox-x, 1):
			self.setxy(x+num-1, y, temps)
			temps = self.tmap[y][x+num]
			self.setxy(x+num, y, s)
			self.printmap()
			time.sleep(0.5)
	
	def printmap(self):
		os.system('cls')
		for y in range(self.HEIGHT):
			for x in range(self.WIDTH):
				sys.stdout.write(self.tmap[y][x])
			sys.stdout.write('\n')
	
	def loadmap(self, fname):
		f = open(fname, 'r')
		mapline = f.read().split('\n')
		f.close()
		self.WIDTH = len(mapline[0])
		self.HEIGHT = len(mapline)
		self.tmap = [['o']*self.WIDTH for _ in range(self.HEIGHT)]
		for y in range(0, self.HEIGHT, 1):
			for x in range(0, self.WIDTH, 1):
				self.tmap[y][x] = mapline[y][x:x+1]
