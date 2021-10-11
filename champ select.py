import pyautogui
import time
from PIL import Image, ImageGrab
import cv2
import numpy as nm
import pytesseract

pyautogui.FAILSAFE = True


def imToString():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    image1 = ImageGrab.grab(bbox=(320,180,1600,825))
    string = pytesseract.image_to_string(cv2.cvtColor(nm.array(image1), cv2.COLOR_BGR2GRAY), lang='eng')
    print(string)
    return string


# Choose pick/ban
playing = str(input("Who would you like to play?\n"))
banning = str(input("Who would you like to ban?\n"))

# Will differ depending on resolution. Also, you obviously have to keep the window in the same place every time
searchx = 1150
searchy = 265
characterx = 700
charactery = 325
lockinx = 950
lockiny = 775


def lockin():
    pyautogui.moveTo(lockinx, lockiny, duration=0.1)
    pyautogui.click()
    pyautogui.click()


def character():
    pyautogui.moveTo(characterx, charactery, duration=0.1)
    pyautogui.click()
    pyautogui.click()
    time.sleep(0.1)
    lockin()


def searchplay():
    pyautogui.moveTo(searchx, searchy, duration=0.1)
    time.sleep(.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl' 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(playing)
    pyautogui.press('enter')
    character()


def searchban():
    pyautogui.moveTo(searchx, searchy, duration=0.1)
    time.sleep(.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl' 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(banning)
    pyautogui.press('enter')
    character()


declare = "declare"
ban = "ban"
choose = "choose"
loadout = "loadout"

hasdeclared = False
hasbanned = False
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
    while hasbanned == False:
        imToString()
        string = imToString()
        if ban in string.lower():
            searchban()
            hasbanned = True
        elif choose in string.lower():
            searchplay()
            exit()
        elif loadout in string.lower():
            print("Done!")
            exit()
