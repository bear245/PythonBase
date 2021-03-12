import Calys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    CGREEN = '\33[32m'
    WARNING = '\033[93m'
    CVIOLET = '\33[35m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Show_Main_Menu():
    """This function displays a Main menu
    as multi-strings and a prompt for user's choice
    :return: Selected item of Menu
    """
    TopLevel_Menu = ("Main menu for Calys75 operations.\n\n"
                     "1. Start Voltage Calibration\n"
                     "2. Start Voltage Measurement\n"
                     "3. Manual Input a Command/Request\n"
                     "0. Quit\n\n")
    print(bcolors.WARNING + TopLevel_Menu + bcolors.ENDC)
    TopLevel_Selector = input('\x1b[5;30;42m' + 'Select your option and press Enter to continue: ' + '\x1b[0m')
    return int(TopLevel_Selector)


def Show_Calibration_Menu():
    """This function displays a Calibration menu
    as multi-strings and a prompt for user's choice
    :return: Selected item of Menu
    """
    Calibration_Menu = ("Calibration menu for Calys75 operations. \n\n"
                        "1. Start Calibration in range 100mV \n"
                        "2. Start Calibration in range 2V \n"
                        "3. Start Calibration in range 20V \n"
                        "0. Quit to Main Menu \n")
    print(bcolors.OKCYAN + Calibration_Menu + bcolors.ENDC)
    Calibration_Selector = input('\x1b[5;30;42m' + 'Select your option and press Enter to continue: ' + '\x1b[0m')
    return int(Calibration_Selector)


def Show_Measurement_Menu():
    """This function displays a Measurement menu
    as multi-strings and a prompt for user's choice
    :return: Selected item of Menu
    """
    Measurement_Menu = ("Measurement menu for Calys75 operations. \n\n"
                        "1. Start Measurement in range 100mV \n"
                        "2. Start Measurement in range 1V \n"
                        "3. Start Measurement in range 10V \n"
                        "4. Start Measurement in range 50V \n"
                        "0. Quit to Main Menu \n")
    print(bcolors.CVIOLET + Measurement_Menu + bcolors.ENDC)
    Measurement_Selector = input('\x1b[5;30;42m' + 'Select your option and press Enter to continue: ' + '\x1b[0m')
    return int(Measurement_Selector)


def Calys_Menu():
    """This function realizes processing of all levels of app menu
    :return: None
    """
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
                    Unit = (Calys.Set_Range(Function='VOLT', VRange=100))
                    print(str(Unit))
                    Calys.Calibration(Start_Cal=0, Stop_Cal=100, Step_Cal=25, End_of_Command=Unit)
                elif CalSelector == 2:
                    print("\n2. Start Calibration in range 2V \n")
                    Unit = (Calys.Set_Range(Function='VOLT', VRange=2))
                    Calys.Calibration(Start_Cal=0, Stop_Cal=2, Step_Cal=1, End_of_Command=Unit)
                elif CalSelector == 3:
                    print("\n3. Start Calibration in range 20V \n")
                    Unit = (Calys.Set_Range(Function='VOLT', VRange=20))
                    Calys.Calibration(Start_Cal=0, Stop_Cal=20, Step_Cal=5, End_of_Command=Unit)
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
                User_Input = input('\x1b[5;30;42m' + 'Type your Command (or quit) and press Enter: ' + '\x1b[0m')
                if User_Input.upper() == 'EXIT' or User_Input.upper() == 'QUIT':
                    break
                if User_Input[-1] == '?':
                    Calys.Send_Request(User_Input)
                else:
                    Calys.Send_Command(User_Input)
        else:
            print('\x1b[2;30;41m' + 'Please select correct options...' + '\x1b[0m')
