from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#title 1 position: X: 727 Y: 700 RGB: (77, 80, 115)
#title 2 position: X: 907 Y: 700 RGB: (163, 169, 232)
#title 3 position: X: 1095 Y: 700 RGB: (253,  18,   1)
#title 4 position: X: 1160 Y: 700 RGB: (169, 173, 232)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed ('q') == False:

    if pyautogui.pixel (727, 700)[0] == 0:
        click(727, 700)
    if pyautogui.pixel (907, 700)[0] == 0:
        click(907, 700)
    if pyautogui.pixel (1095, 700)[0] == 0:
        click(1095, 700)
    if pyautogui.pixel (1160, 700)[0] == 0:
        click(1160, 700)
