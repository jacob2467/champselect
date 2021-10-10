import pyautogui
import time
from PIL import Image, ImageGrab
import cv2
import numpy as nm
import pytesseract

pyautogui.FAILSAFE = True
time.sleep(2)


def imToString():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
    image1 = ImageGrab.grab(bbox=(160, 200, 2724, 1600))
    string = pytesseract.image_to_string(cv2.cvtColor(nm.array(image1), cv2.COLOR_BGR2GRAY), lang='eng')
    return string


# Choose pick/ban
playing = str(input("Who would you like to play?\n"))
banning = str(input("Who would you like to ban?\n"))
time.sleep(2)

# Will differ depending on resolution. This works for my Mac that has a 2880x1800 Display.
# Also, you obviously have to keep the window in the same place every time
searchx = 900
searchy = 200
characterx = 475
charactery = 250
lockinx = 720
lockiny = 700


def lockin():
    pyautogui.moveTo(lockinx, lockiny, duration=0)
    pyautogui.click()


def character():
    pyautogui.moveTo(characterx, charactery, duration=0)
    pyautogui.click()
    lockin()


def searchplay():
    pyautogui.moveTo(searchx, searchy, duration=0)
    time.sleep(.5)
    pyautogui.click()
    pyautogui.hotkey('command' 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(playing)
    pyautogui.press('enter')
    character()


def searchban():
    pyautogui.moveTo(searchx, searchy, duration=0)
    time.sleep(.5)
    pyautogui.click()
    pyautogui.hotkey('command' 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(banning)
    pyautogui.press('enter')
    character()


declare = "declare"
ban = "ban"
choose = "choose"
loadout = "loadout"

hasdeclared = False
while hasdeclared == False:
    imToString()
    string = imToString()
    time.sleep(1)
    if declare in string.lower():
        searchplay()
        hasdeclared = True
    elif choose in string.lower():
        searchplay()
        exit()
    else:
        imToString()
while hasdeclared == True:
    imToString()
    string = imToString()
    if ban in string.lower():
        searchban()
    elif choose in string.lower():
        searchplay()
    elif loadout in string.lower():
        print("Done!")
        exit()
