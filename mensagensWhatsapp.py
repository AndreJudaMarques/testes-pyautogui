#mensagensWhatsapp.py

import webbrowser
import pyautogui
from time import sleep

telefones = 'xxxxxxx'

#x guilherme
#x wanda
#x priscila

sleep(1)

for telefone in telefones:
      webbrowser.open_new_tab(f'https://wa.me/{telefone}')
      sleep(2)
      pyautogui.press('tab')         
      sleep(0.5)
      pyautogui.press('tab')
      sleep(0.5)
      pyautogui.press('space')
      sleep(2)
      pyautogui.typewrite('Ola, provavelmente eu ja comprei pizza com voces e hoje trabalho com automatizacao de mensagens, gostaria de enviar mensagens automaticas para seus clientes? como catálogos, promoçoes ou entao apenas lembrando a eles que sexta feira é um otimo dia para comprar pizza, se sim entre em contato comigo para eu te passar um programa que faz isso automatico para voce. Até mais. ', interval=0.05)
      sleep(1)
      pyautogui.press('tab')
      sleep(0.5)
      pyautogui.press('space') #enviou mensagem
      sleep(1)
      pyautogui.hotkey('alt', 'tab')
      sleep(1)
      pyautogui.hotkey('ctrl', 'w')


