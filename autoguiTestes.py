import pyautogui 

# clica e cria pasta x vezes
def mover():
      for i in range(3):
            pyautogui.click(x=1572, y=401, duration= 0.5)

            pyautogui.rightClick()

            pyautogui.click(x=1589, y=698, duration= 0.5)

            pyautogui.click(x=1542, y=700, duration= 0.5)

#mover()