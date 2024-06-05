#mensagensWhatsapp.py

import webbrowser
import pyautogui
from time import sleep

telefones = 

sleep(1)

for telefone in telefones:
      webbrowser.open_new_tab(f'https://wa.me/{telefone}')
      sleep(2)
      pyautogui.press('tab')
      sleep(0.5)
      pyautogui.press('tab')
      sleep(0.5)
      pyautogui.press('space')
      sleep(1.5)
      pyautogui.typewrite('Oi amigo, estou testando um novo sistema de mensagens automáticas, fica bravo nao S2', interval=0.1)
      sleep(1)
      pyautogui.press('tab')
      sleep(0.5)
      pyautogui.press('space') #enviou mensagem
      sleep(1)
      pyautogui.hotkey('alt', 'tab')
      sleep(1)
      pyautogui.hotkey('ctrl', 'w')


