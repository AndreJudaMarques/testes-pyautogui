import webbrowser
import pyautogui
from time import sleep

''' DESAFIO SITE '''
#navegar ate o site
#encontrar digite seu nome em alertar e digitar
#clicr em alerta
#fechar o alerta
#subir toda pagina
#descer ate a secao de downloads
#realizar download de excel e pdf
#alerta 'Voce TErminou"

webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(1)
pyautogui.click(x=824,y=244, duration=1.5)
sleep(1)
pyautogui.scroll(-500)

blank = pyautogui.locateCenterOnScreen('blank1.png')
pyautogui.click(x=783, y=761, duration=1)

pyautogui.typewrite('Andre Juda da Rosa Marques', interval=0.2)
pyautogui.click(x=783, y=795, duration=1)
sleep(1)
pyautogui.press('space')
sleep(2)
pyautogui.scroll(+1000)
sleep(1)
pyautogui.scroll(-1500)

excelButton = pyautogui.locateCenterOnScreen('excelButton.png')
pyautogui.moveTo(excelButton, duration= 1)
pyautogui.click(x=114, y=935, duration= 0.5)
sleep(0.5)
pyautogui.click(x=312, y=903, duration=1)
sleep(1)
pyautogui.alert('Tarefa Finalizada', title= 'Alerta do programa')


