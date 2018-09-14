#-*- coding: euc-kr -*-
import os
import time

os.system('mode con:cols=121 lines=53')
os.system('cls')


class ScreenCon:
	screen = []

	def __init__(self, s):
		for num in range(0, 50):
			self.screen.append('%2d'%num + s*118)

	def printscreen(self):
		os.system('cls')
		for num in range(0, len(self.screen)):
			print(self.screen[num])

	def setxy(self, x, y, s):
		self.screen[y] = self.screen[y][0:x] + s + self.screen[y][x+len(s):]
		#printscreen(screen)

	def move(self, x, y, tox, toy, s):
		backs = self.screen[y][x]
		self.setxy(x, y, s)
		self.printscreen()
		time.sleep(0.5)
		for num in range(1, tox-x):
			self.setxy(x+num, y, s)
			self.setxy(x+num-1, y, backs)
			self.printscreen()
			time.sleep(0.5)

screencon = ScreenCon('-')

#screencon.printscreen()

screencon.setxy(38, 20, 'abcd')
screencon.printscreen()

screencon.move(10, 1, 15, 1, 'AAAA')
