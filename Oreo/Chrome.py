import time
import pyautogui

width, height = pyautogui.size()    # returns a screen resolution
print(str(width) + ' ' + str(height))

codesFile = open('C:\\Users\\Oleksandr Siora\\PycharmProjects\\PythonBase\\Oreo\\codes.txt') #Open file in ReadMode
listCodes = codesFile.readlines()
print(listCodes)
codesFile.close()

for i in listCodes:
    print(i)
    CODE = i
    EMAIL = CODE.lower() + '@gmail.com'

    # Enter the CODE
    print('1.Enter CODE...' + CODE)
    time.sleep(5)  # Pause 5 seconds
    pyautogui.moveTo(2655, 500)
    pyautogui.click()
    pyautogui.typewrite(CODE, interval=0.1)

    #Enter the EMAIL
    print('2.Enter EMAIL...')
    time.sleep(5)  # Pause 5 seconds
    #pyautogui.press('tab')
    pyautogui.moveTo(2655, 585)
    pyautogui.click()
    pyautogui.typewrite(EMAIL, interval=0.1)

    # Set CheckBox
    print('3.Set Checkbox...')
    time.sleep(5)  # Pause 5 seconds
    pyautogui.moveTo(2645, 665)
    pyautogui.click()

    # Close Advertisement
    time.sleep(5) # Pause 2 seconds
    pyautogui.moveTo(2100, 245)
    pyautogui.click()

    # Check Result
    print('4.Close Advertisement...')
    time.sleep(5) # Pause 2 seconds
    pyautogui.moveTo(2810, 945) # Need to check and correct coordinates
    pyautogui.click()

    # Locate result button on the screen
    print('5.Try to find TryAgain button...')
    time.sleep(30)
    Result = pyautogui.locateOnScreen('tryagain.png', confidence=0.8)
    print(Result)
    if Result != None:
        break;

    # Backward to previous page and refresh
    print('6.Chrome back & refresh page...')
    pyautogui.hotkey('alt', 'left')
    time.sleep(10)
    pyautogui.press('f5')
    time.sleep(20)