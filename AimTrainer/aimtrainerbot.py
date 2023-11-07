from pyautogui import *
import pyautogui
import keyboard
import random
import time
import win32api, win32con

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Cor do centro: (255, 87, 34)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(550,300,800,500))
    width, height = pic.size
    
    for x in range(0,width,15):
        for y in range(0,height,15):

            r,g,b = pic.getpixel((x,y))

            if r == 255:
                click(x+550,y+300)
                time.sleep(0.02)
                break
