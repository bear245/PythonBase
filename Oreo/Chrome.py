import time
import pyautogui

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

width, height = pyautogui.size()  # returns a screen resolution
print(str(width) + ' ' + str(height))

codesFile = open('C:\\Users\\Oleksandr Siora\\PycharmProjects\\PythonBase\\Oreo\\codes.txt')  # Open file in ReadMode
listCodes = codesFile.readlines()
print(listCodes)
codesFile.close()

for i in listCodes:
    print(i)
    CODE = i
    EMAIL = CODE.lower() + '@ukr.net'

    # Set CheckBox
    print('1.Set Checkbox...')
    time.sleep(1)  # Pause 5 seconds
    pyautogui.moveTo(2645, 665)
    pyautogui.click()

    # Enter the CODE
    print('2.Enter CODE...' + CODE)
    time.sleep(1)  # Pause 5 seconds
    pyautogui.moveTo(2655, 500)
    pyautogui.click()
    pyautogui.typewrite(CODE, interval=0.1)

    # Enter the EMAIL
    print('3.Enter EMAIL...' + EMAIL)
    time.sleep(1)  # Pause 5 seconds
    # pyautogui.press('tab')
    pyautogui.moveTo(2655, 585)
    pyautogui.click()
    pyautogui.typewrite(EMAIL, interval=0.1)

    # Check Result
    print('4.Go Forward...')
    # Click to empty field
    time.sleep(1)  # Pause 2 seconds
    pyautogui.moveTo(2000, 585)
    pyautogui.click()

    Forward = pyautogui.locateCenterOnScreen('forward.png', confidence=0.9)
    print(Forward)
    if Forward:
        pyautogui.moveTo(Forward[0], Forward[1])
        pyautogui.click()
    else:
        pyautogui.moveTo(2810, 945)  # Need to check and correct coordinates
        pyautogui.click()

    # # TODO insert check for CAPTCHA apeears and "Wait for user input..." and resolve CAPCHA
    # print('5.Try to find CAPTCHA...')
    # time.sleep(5)
    # CapchaFound = pyautogui.locateOnScreen('capcha.png', confidence=0.5)
    # print(CapchaFound)
    # if CapchaFound != None:
    #     wait = input('Press any key to continue...')

    time.sleep(20)
    print('6.Check DailyLimit')
    DailyLimitFound = pyautogui.locateCenterOnScreen('dailylimit.png', confidence=0.9)
    print(DailyLimitFound)
    if DailyLimitFound:
        continue

    # Locate result button on the screen
    print('7.Try to find TryAgain button...')
    time.sleep(20)
    TryAgainFound = pyautogui.locateCenterOnScreen('tryagain.png', confidence=0.9)
    print(TryAgainFound)
    if TryAgainFound:
        # Backward to previous page and refresh
        pyautogui.moveTo(TryAgainFound[0], TryAgainFound[1])
        pyautogui.click()

        # print('7.Chrome back & refresh page...')
        # pyautogui.hotkey('alt', 'left')
        # time.sleep(30)
        # pyautogui.press('f5')
        # time.sleep(20)
    else:
        break;


# TODO store to external file successfull CODE/EMAIL