from time import sleep
import pyautogui

def clicar_imagem(img):
    imagem = 'imagem/'+ img +'.png'
    local = pyautogui.locateOnScreen(imagem, confidence=0.9)
    pyautogui.moveTo(local, duration=0.2)
    sleep(1)
    return  pyautogui.click(local)
