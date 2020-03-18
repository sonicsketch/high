#-*- coding: utf-8 -*-
import os, sys
import time
import highclass
import pyautogui as m

os.system('mode con:cols=163 lines=53')
os.system('cls')

screencon = highclass.ScreenCon()
screencon.loadmap('total_map_path.txt')
screencon.printmap()

#screencon.move(90, 40, 120, 40, '■')

try:
	while True:
		x, y = m.position()
		sys.stdout.write('\r%d : %d  ' % (x, y))
except:
	print('test')

s = input()
print(s)