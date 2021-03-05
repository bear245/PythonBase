import os
import pyautogui
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# pyautogui.screenshot('screen2.png')

# print(os.path.abspath('TryAgain.png'))
# Check = os.path.isfile('TryAgain.png')
# print(Check)
# Result = pyautogui.locateCenterOnScreen('C:\\Users\\Oleksandr Siora\\PycharmProjects\\PythonBase\\Oreo\\TryAgain.png')
Result = pyautogui.locateOnScreen('tryagain.png')
print(Result)