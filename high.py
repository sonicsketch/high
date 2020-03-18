#-*- coding: utf-8 -*-
import os, sys
import time
import highclass
import pyautogui as m

os.system('mode con:cols=163 lines=53')
os.system('cls')

'''
f = open('total_map_path.txt', 'r')
totalmap = f.read().split('\n')
f.close()

screencon = highclass.ScreenCon(totalmap)
screencon.printscreen()

s = input()

print(s)


WIDTH = 162
HEIGHT = 51

tmap = [['o']*WIDTH for _ in range(HEIGHT)]

for y in range(0, HEIGHT, 1):
	for x in range(0, WIDTH, 1):
		tmap[y][x] = totalmap[y][x:x+1]
'''

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