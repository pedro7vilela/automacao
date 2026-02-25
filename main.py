import pyautogui
from dotenv import load_dotenv
import os
from funcao_imagem import clicar_imagem
from time import sleep

pyautogui.FailSafeException()
load_dotenv()
SENHA_AVA = os.getenv('SENHA_AVA')

pyautogui.PAUSE = 1
clicar_imagem('brave')
# ABA ANONIMA
pyautogui.hotkey('ctrl', 'shift', 'n')
sleep(1)
# GOOGLE
pyautogui.hotkey('ctrl', 'l')
pyautogui.typewrite('google.com', interval=0.1)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
sleep(1)
#UNICARIOCA
pyautogui.hotkey('ctrl', 'l')
pyautogui.typewrite('ava.unicarioca.edu.br', interval=0.1)
pyautogui.press('enter')
sleep(2)
clicar_imagem('ava_usuario')
pyautogui.typewrite('2023200145', interval=0.1)
pyautogui.press('tab')
pyautogui.typewrite(SENHA_AVA, interval=0.1)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
sleep(1)
#GE
pyautogui.hotkey('ctrl', 'l')
pyautogui.typewrite('ge.globo.com/flamengo', interval=0.1)
pyautogui.press('enter')
#SPOTIFY
clicar_imagem('spotify')
sleep(5)
clicar_imagem('buscador')
pyautogui.typewrite('runaway', interval=0.2)
pyautogui.press('enter')
sleep(1)
clicar_imagem('runaway')