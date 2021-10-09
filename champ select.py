import pyautogui
import time

pyautogui.FAILSAFE = True
time.sleep(5)


playing = str(input("Who would you like to play?\n"))
banning = str(input("Who would you like to ban?\n"))
time.sleep(1)

# Will differ depending on resolution. This works for my Mac that has a 2880x1800 Display.
# Also, you obviously have to keep the window in the same place every time
searchx = 900
searchy = 200
characterx = 475
charactery = 250
lockinx = 720
lockiny = 700


def lockin():
    pyautogui.moveTo(lockinx, lockiny, duration=1)
    pyautogui.click()


def character():
    pyautogui.moveTo(characterx, charactery, duration=1)
    pyautogui.click()
    lockin()


def searchplay():
    pyautogui.moveTo(searchx, searchy, duration=1)
    time.sleep(.5)
    pyautogui.click()
    pyautogui.hotkey('command' 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(playing)
    pyautogui.press('enter')
    character()


def searchban():
    pyautogui.moveTo(searchx, searchy, duration=1)
    time.sleep(.5)
    pyautogui.click()
    pyautogui.hotkey('command' 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(banning)
    pyautogui.press('enter')
    character()


searchplay()
time.sleep(15)
searchban()
time.sleep(30)
for i in range(10):
    searchplay()
    time.sleep(10)
print("Done!")
