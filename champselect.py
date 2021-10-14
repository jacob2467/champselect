import pyautogui
import time
from PIL import ImageGrab
import cv2
import numpy as nm
import pytesseract

pyautogui.FAILSAFE = True


def imgToString():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    image1 = ImageGrab.grab(bbox=(320, 180, 1600, 825))
    global string
    string = pytesseract.image_to_string(cv2.cvtColor(nm.array(image1), cv2.COLOR_BGR2GRAY), lang='eng')


# Choose pick/ban
playing = str(input("Who would you like to play?\n"))
banning = str(input("Who would you like to ban?\n"))

# Will differ depending on resolution. Also, you obviously have to keep the window in the same place every time
searchx = 1150
searchy = 265
characterx = 700
charactery = 325
lockinx = 950
lockiny = 770
acceptx = 925
accepty = 700


def acceptMatch():
    pyautogui.moveTo(925, 700, duration=0.5)
    pyautogui.click()
    pyautogui.click()


def lockin():
    pyautogui.moveTo(lockinx, lockiny, duration=0.5)
    pyautogui.click()
    pyautogui.click()


def character():
    pyautogui.moveTo(characterx, charactery, duration=0.5)
    pyautogui.click()
    pyautogui.click()
    time.sleep(0.1)
    lockin()


def searchPlay():
    pyautogui.moveTo(searchx, searchy, duration=0.5)
    time.sleep(.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl' 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(playing)
    pyautogui.press('enter')
    character()


def searchBan():
    pyautogui.moveTo(searchx, searchy, duration=0.5)
    time.sleep(.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl' 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(banning)
    pyautogui.press('enter')
    character()


hasDeclared = False
hasBanned = False
hasAccepted = False

while hasAccepted == False:
    imgToString()
    print(string)
    time.sleep(1)
    if "decline" in string.lower():
        acceptMatch()
        hasAccepted = True
    elif "declare" in string.lower():
        searchPlay()
        hasAccepted = True
        hasDeclared = True
    elif "choose" in string.lower():
        searchPlay()
        exit()

while hasDeclared == False:
    imgToString()
    print(string)
    time.sleep(1)
    if "declare" in string.lower():
        searchPlay()
        hasDeclared = True
    elif "choose" in string.lower():
        searchPlay()
        exit()
    else:
        imgToString()

while hasDeclared == True:
    while hasBanned == False:
        time.sleep(1)
        imgToString()
        print(string)
        if "ban" in string.lower():
            searchBan()
            hasBanned = True
    while hasBanned == True:
        time.sleep(1)
        imgToString()
        print(string)
        if "choose" in string.lower():
            searchPlay()
            print("Done!")
            exit()
