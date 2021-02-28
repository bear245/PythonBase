import serial
import time

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

# def cls():
#    os.system('cls' if os.name=='nt' else 'clear')

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

def Calys_Init():
    """This function realize Initialization of Hardware (Calys75)
    check it identification (*IDN?) as evidence of successful connection
    and change device's state to Remote work (REM)
    :return: None
    """
    print("Connected to: " + ser.portstr)  # Display a message about successful connection
    ser.write(b'*IDN?\r\n')  # Write BIN array to SERIAL
    ser.flush()  # Clear output buffer
    raw_bytes = ser.readline()  # Read all present data from SERIAL
    print(raw_bytes.decode())  # Display received data as UNICODE decoded from BIN Array
    ser.write(b'REM\r\n')


def Calys_Stop():
    """This function realize stop of Hardware (Calys75)
    change device's state to Local work (LOC) and close SERIAL
    :return: None
    """
    ser.write(b'LOC\r\n')
    ser.close()  # Close SERIAL port
    print('Disconnected')


def Calys_Send_Command(Command):
    """This function transform user input(string) into HW command(bytes),
    display it and write to SERIAL
    :param Command: User input from keyboard
    :return: None
    """
    Command = Command + '\r\n'
    print('Send Command: ' + str(Command.encode()))
    ser.write(Command.encode())


def Calys_Send_Request(Command):
    """This function transform user input(string) into HW command(bytes),
    display it, write to SERIAL and wait for answer from SERIAL
    :param Command: User input from keyboard
    :return: None
    """
    Command = Command + '\r\n'
    print('Send Request: ' + str(Command.encode()))
    ser.write(Command.encode())
    raw_bytes = ser.readline()  # Read all present data from SERIAL
    print('Received: ' + str(raw_bytes.decode()))  # Display received data as UNICODE decoded from BIN Array

def Calys_Menu():
    """This function realiizes processing
    of all levels of app menu
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
                User_Input = input('\x1b[5;30;42m' + 'Type your Command (or quit) and press Enter: ' + '\x1b[0m')
                if User_Input.upper() == 'EXIT' or User_Input.upper() == 'QUIT':
                    break
                if User_Input[-1] == '?':
                    Calys_Send_Request(User_Input)
                else:
                    Calys_Send_Command(User_Input)
        else:
            print('\x1b[2;30;41m' + 'Please select correct options...' + '\x1b[0m')

# Initialize Serial port with parameters
ser = serial.Serial(
    port='COM3', \
    baudrate=115200, \
    parity=serial.PARITY_NONE, \
    stopbits=serial.STOPBITS_ONE, \
    bytesize=serial.EIGHTBITS, \
    timeout=None)

Calys_Init()

Calys_Menu()

Calys_Stop()

# time.sleep(5.5) # Pause 5.5 seconds
# wait = input('Press any key to continue...')
