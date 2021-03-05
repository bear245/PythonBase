from selenium import webdriver #to import selenium
import time

#pyautogui.readthedocs.org/en/latest/
import pyautogui #third-party module
width, height = pyautogui.size()#returns a screen resolution
print(str(width) + ' ' + str(height))
CODE = 'YNHEMHFE'
EMAIL = CODE.lower() + '@gmail.com'
browser = webdriver.Firefox() #to open the browser
browser.get('https://www.singwithoreo.com/uk-ua/participation') #to send the browser to a URL
# print(pyautogui.position())
wait = input('Press any key to continue...')
# time.sleep(10) # Pause 5.5 seconds
elem = browser.find_element_by_css_selector('div.cookie-banner__content div.cookie-banner__btn button.btn-primary.btn-white.btn-xtra-small')
elem.click()

pyautogui.moveTo(800, 500)
pyautogui.click()
pyautogui.typewrite(CODE, interval=0.5)

pyautogui.press('tab')
pyautogui.typewrite(EMAIL, interval=0.5)

# CheckBox
pyautogui.moveTo(425, 675)
pyautogui.click()
# Close Advertisement
time.sleep(2) # Pause 2 seconds
pyautogui.moveTo(905, 245)
pyautogui.click()

time.sleep(2) # Pause 2 seconds
pyautogui.moveTo(500, 950)
pyautogui.click()

# pyautogui.press('tab')
# CodeLocation = pyautogui.locateCenterOnScreen('Code.png') #will return an (x,y) tuple of where the image is on the screen
# pyautogui.moveTo(CodeLocation)
# pyautogui.click()
# pyautogui.typewrite('Hello CODE', interval=0.5)
#entercode
# elem = browser.find_element_by_css_selector('input#email.form-input.form-control.js-event-type-in.js-event-ab.notvalid')
# elem.click()
# pyautogui.press('tab')
# pyautogui.typewrite('Hello EMAIL', interval=0.5)
#email
# elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a:nth-child(1)') #find element by Uniq CSS selector
# elem.click() #click on found element

# html body.uk-ua.custom-entercode div#root div#js-cooke-banner.cookie-banner.open div.cookie-banner__content div.cookie-banner__btn button.btn-primary.btn-white.btn-xtra-small
# html body.uk-ua.custom-entercode div#root main.body-content.static-content div.content-participation.separator-wave-before div.static-small-content div.static-small-content__wrapper div.content-main form#frm_participation div.form-container div.form-row div#entercode-placeholder.form-field.form-placeholder.notvalid input#entercode.form-input.form-control.form-placeholder.js-event-type-in.js-event-ab.notvalid
# html body.uk-ua.custom-entercode div#root main.body-content.static-content div.content-participation.separator-wave-before div.static-small-content div.static-small-content__wrapper div.content-main form#frm_participation div.form-container div.form-row div.form-field.notvalid input#email.form-input.form-control.js-event-type-in.js-event-ab.notvalid