#-*- coding: euc-kr -*-
import os
import time
import highclass

os.system('mode con:cols=163 lines=53')
os.system('cls')


f = open('total_map_path.txt', 'r')
totalmap = f.read().split('\n')
f.close()

screencon = highclass.ScreenCon(totalmap)
screencon.printscreen()

#screencon.setxy(75, 40, 'ABCD')
#time.sleep(1)
#screencon.printscreen()

#screencon.move(75, 40, 120, 40, 'ABCD')

s = input()

print(s)