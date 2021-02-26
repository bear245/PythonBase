import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    CGREEN = '\33[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Show_Main_Menu():
    TopLevel_Menu = ("Main menu for Calys75 operations.\n\n"
                     "1. Start Voltage Calibration\n"
                     "2. Start Voltage Measurement\n"
                     "3. Manual Input a Command/Request\n"
                     "0. Quit\n\n")
    print(bcolors.WARNING + TopLevel_Menu + bcolors.ENDC)
    TopLevel_Selector = input('\x1b[5;30;42m' + 'Select your option and press Enter to continue: ' + '\x1b[0m')
    return int(TopLevel_Selector)
# ('\x1b[5;30;42m' + 'Success!' + '\x1b[0m')
def Show_Calibration_Menu():
    Calibration_Menu = ("Calibration menu for Calys75 operations. \n\n"
                        "1. Start Calibration in range 100mV \n"
                        "2. Start Calibration in range 2V \n"
                        "3. Start Calibration in range 20V \n"
                        "0. Quit to Main Menu \n")
    print(bcolors.OKCYAN + Calibration_Menu + bcolors.ENDC)
    Calibration_Selector = input('\x1b[5;30;42m' + 'Select your option and press Enter to continue: ' + '\x1b[0m')
    return int(Calibration_Selector)

def Show_Measurement_Menu():
    Measurement_Menu = ("Measurement menu for Calys75 operations. \n\n"
                        "1. Start Measurement in range 100mV \n"
                        "2. Start Measurement in range 1V \n"
                        "3. Start Measurement in range 10V \n"
                        "4. Start Measurement in range 50V \n"
                        "0. Quit to Main Menu \n")
    print(bcolors.CGREEN + Measurement_Menu + bcolors.ENDC)
    Measurement_Selector = input('\x1b[5;30;42m' + 'Select your option and press Enter to continue: ' + '\x1b[0m')
    return int(Measurement_Selector)


while True:
    TopSelector = Show_Main_Menu()
    if TopSelector == 0:
        break
    elif TopSelector == 1:
        while True:
            CalSelector = Show_Calibration_Menu()
            if CalSelector == 0:
                break
            elif CalSelector == 1:
                print("\n1. Start Calibration in range 100mV \n")
            elif CalSelector == 2:
                print("\n2. Start Calibration in range 2V \n")
            elif CalSelector == 3:
                print("\n3. Start Calibration in range 20V \n")
            else:
                print('\x1b[2;30;41m' + 'Please select correct options...' + '\x1b[0m')
    elif TopSelector == 2:
        while True:
            MeasSelector = Show_Measurement_Menu()
            if MeasSelector == 0:
                break
            elif MeasSelector == 1:
                print("\n1. Start Measurement in range 100mV \n")
            elif MeasSelector == 2:
                print("\n2. Start Measurement in range 1V \n")
            elif MeasSelector == 3:
                print("\n3. Start Measurement in range 10V \n")
            elif MeasSelector == 4:
                print("\n4. Start Measurement in range 50V \n")
            else:
                print('\x1b[2;30;41m' + 'Please select correct options...' + '\x1b[0m')
    elif TopSelector == 3:
        while True:
            User_Input = input('\nType your Command and press Enter: ')
            if User_Input.upper() == 'EXIT' or User_Input.upper() == 'QUIT':
                break
            if User_Input[-1] == '?':
                Calys_Send_Request(User_Input)
            else:
                Calys_Send_Command(User_Input)
    else:
        print('\x1b[2;30;41m' + 'Please select correct options...' + '\x1b[0m')