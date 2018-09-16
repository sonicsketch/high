#-*- coding: euc-kr -*-
import os
import time

class ScreenCon:
	mapscreen = []
	curscreen = []

	def __init__(self, maptext):
		for num in range(0, len(maptext)):
			self.mapscreen.append(maptext[num])
			self.curscreen.append(maptext[num])

	def printscreen(self):
		os.system('cls')
		for num in range(0, len(self.curscreen)):
			print(self.curscreen[num])

	def setxy(self, x, y, s):
		self.curscreen[y] = self.curscreen[y][0:x] + s + self.curscreen[y][x+len(s):]
		#printscreen(screen)

	def move(self, x, y, tox, toy, s):
		self.setxy(x, y, s)
		self.printscreen()
		time.sleep(0.5)
		for num in range(1, tox-x):
			self.setxy(x+num, y, s)
			self.setxy(x+num-1, y, self.mapscreen[y][x+num-1])
			self.printscreen()
			time.sleep(0.5)
