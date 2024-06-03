# cria um programa que pede usuario e senha
# copiar e colar num bloco de notas

import pyautogui

email = pyautogui.prompt(text='Digite seu email', title='informações obrigatórias')
senha = pyautogui.password(text='Digite sua senha',title='informações obrigatórias',  mask='*')

pyautogui.click(x=1398, y=142)
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)
