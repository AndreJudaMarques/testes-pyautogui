import pyautogui
import webbrowser
from time import sleep

'''Este programa acessa a rede social, pesquisa a #personalizada
visita as 3 ultimas publicacoes, deixa o like em cada uma e 
fecha a aba'''

webbrowser.open_new_tab('https://www.instagram.com/')
sleep(3)
pyautogui.click(x=49,y=314, duration=1)
sleep(1)
pyautogui.typewrite('#calisthenics')
sleep(2)
pyautogui.press('tab')
sleep(0.5)
pyautogui.press('tab')
sleep(0.5)
pyautogui.press('enter')
sleep(6)

for i in range(3):
      pyautogui.press('tab')
      sleep(1)
      pyautogui.press('enter')
      sleep(1)
      pyautogui.moveTo(x=541,y=738, duration=1)
      sleep(1)
      pyautogui.click()
      sleep(0.5)
      pyautogui.press('esc')
      sleep(1)
print('chegou aqui')
sleep(1)
pyautogui.hotkey('ctrl', 'w')
print('finalizou')