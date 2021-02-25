import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Show_Main_Menu():
    TopLevel_Menu = ("Main menu for Calys75 operations.\n\n"
                     "1. Start Voltage Calibration\n"
                     "2. Start Voltage Measurement\n"
                     "3. Manual Input a Command/Request\n"
                     "0. Quit\n\n")
    print(TopLevel_Menu)
    TopLevel_Selector = input('Select your option and press Enter to continue...')
    return int(TopLevel_Selector)

def Show_Calibration_Menu():
    Calibration_Menu = ("Calibration menu for Calys75 operations. \n\n"
                        "1. Start Calibration in range 100mV \n"
                        "2. Start Calibration in range 2V \n"
                        "3. Start Calibration in range 20V \n"
                        "0. Start Calibration in range 20V \n")
    print(Calibration_Menu)
    Calibration_Selector = input('Select your option and press Enter to continue...')
    return int(Calibration_Selector)

Selector = Show_Main_Menu()
while True:
    if Selector > 3:
        print("\nIncorrect option")
        time.sleep(2.5)  # Pause 2.5 seconds
        cls()
        Selector = Show_Main_Menu()
    elif Selector == 0:
        print("\nYou selected 0")
    elif Selector == 1:
        print("\nYou selected 1")
    elif Selector == 2:
        print("\nYou selected 2")
    elif TopLevel_Selector == 3:
        print("\nYou selected 3")
