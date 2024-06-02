#arrastar arquivos

import pyautogui

def arrastar():
      for i in range(2):
            pyautogui.moveTo(x=1296, y=133, duration=1)

            pyautogui.dragTo(x=1481,y=962, duration=1)

arrastar()