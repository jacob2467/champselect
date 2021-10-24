import pyautogui
import time
from PIL import ImageGrab
import cv2
import numpy as nm
import pytesseract
import configparser

config = configparser.ConfigParser()
config
config.read("config.ini")


def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


searchx = int(ConfigSectionMap("SearchBar")['searchx'])
searchy = int(ConfigSectionMap("SearchBar")['searchy'])
characterx = int(ConfigSectionMap("ChooseCharacter")['characterx'])
charactery = int(ConfigSectionMap("ChooseCharacter")['charactery'])
lockinx = int(ConfigSectionMap("LockInCharacter")['lockinx'])
lockiny = int(ConfigSectionMap("LockInCharacter")['lockiny'])
acceptx = int(ConfigSectionMap("AcceptMatch")['acceptx'])
accepty = int(ConfigSectionMap("AcceptMatch")['accepty'])
windowSize1 = int(ConfigSectionMap("WindowSize")['windowsize1'])
windowSize2 = int(ConfigSectionMap("WindowSize")['windowsize2'])
windowSize3 = int(ConfigSectionMap("WindowSize")['windowsize3'])
windowSize4 = int(ConfigSectionMap("WindowSize")['windowsize4'])
ocr = (ConfigSectionMap("PyTesseract")['ocr'])

pyautogui.FAILSAFE = True


def imgToString():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = str(ocr)
    image1 = ImageGrab.grab(bbox=(windowSize1, windowSize2, windowSize3, windowSize4))
    global string
    string = pytesseract.image_to_string(cv2.cvtColor(nm.array(image1), cv2.COLOR_BGR2GRAY), lang='eng')


# Choose pick/ban
playing = str(input("Who would you like to play?\n"))
banning = str(input("Who would you like to ban?\n"))


def acceptMatch():
    pyautogui.moveTo(acceptx, accepty, duration=0.5)
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
    pyautogui.click()


hasDeclared = False
hasBanned = False
hasAccepted = False
inGame = False

while hasAccepted == False:
    imgToString()
    print(string)
    time.sleep(1)
    if "decline" in string.lower():
        acceptMatch()
        while inGame == False:
            if "declare" in string.lower():
                hasAccepted = True
                inGame = True
            else:
                inGame = True


while hasDeclared == False:
    imgToString()
    print(string)
    time.sleep(1)
    if "declare" in string.lower():
        searchPlay()
        pyautogui.click()
        hasDeclared = True
    elif "character" in string.lower():
        searchPlay()
        pyautogui.click()
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
            lockin()
            print("Done!")
            exit()
