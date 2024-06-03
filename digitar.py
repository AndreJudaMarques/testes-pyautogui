import pyautogui
from time import sleep
#mover mouse ate o campo de digitar

pyautogui.moveTo(x=1626, y=1015, duration= 0.5)
pyautogui.click()
pyautogui.typewrite('so um teste do bot')
sleep(0.3)
pyautogui.click(x=1889, y=1015)

#clicar no tempo de digitar
#digitar a msg
#clicar botao de enviar

''' para caracteres especiais usar piperclip'''

