#botGuitarflash.py

import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(x=450,y=492, duration=1)

def click(x,y):
      win32api.SetCursorPos((x,y))
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
      sleep(0.05)
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('1') == False:
      if pyautogui.pixelMatchesColor(556,542, (0,0,0)): #verde
            click(556,542)
            
      if pyautogui.pixelMatchesColor(468,542, (0,0,0)): #vermelho
            click(468,542)
            
      if pyautogui.pixelMatchesColor(371,542, (0,0,0)): #amarelo
            click(371,542)
            
      if pyautogui.pixelMatchesColor(280,542, (0,0,0)): #azul
            click(280,542)
      
            