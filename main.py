import pyautogui

x, y = pyautogui.position()

import pyautogui
import time

color_x = 2623
color_y = 198

def color_coord(x,y):
	return color_x + 60 * x, color_y + 60*y

def change_color(x,y):
	click_x, click_y = color_coord(x,y)
	pyautogui.click(click_x, click_y)

tries = 0
while tries < 1:
	change_color(1,1)
	for i in range(40):
		pyautogui.click(x + (i) * 10,y)
		time.sleep(0.05)
	#change_color(1,17)
	#for i in range(20):
	#	pyautogui.click(x + (i) * 10,y)
	#change_color(1,19)
	for i in range(40):
		pyautogui.click(x + (i) * 10,y-15)
		time.sleep(0.05)
	#change_color(1,6)
	for i in range(40):
		pyautogui.click(x + (i) * 10,y-30)
		time.sleep(0.05)
	change_color(0,1)
	for i in range(40):
		pyautogui.click(x + (i) * 10,y-45)
		time.sleep(0.05)
	#change_color(1,10)
	for i in range(40):
		pyautogui.click(x + (i) * 10,y-60)
		time.sleep(0.05)
	for i in range(40):
		pyautogui.click(x + (i) * 10,y-75)
		time.sleep(0.05)
	tries += 1

