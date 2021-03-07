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


def Calys_Set_Range(*, Function=('VOLT', 'CURR'), **kwargs):
    """This function sets Source output function of HW
    and sets it to correct or maximum Range
    :param Function: 'VOLT' - for Voltage, 'CURR' - for current
    :param kwargs: VRange: int=(100, 2, 20, 50) - set range for Voltage, 100mV, others in V
                   CRange: int=(0, 4, 24) - set range for Current, mA
    :return: Units - string, depends from range
    call examples: Calys_Set_Range(Function='VOLT', VRange=50) - Set Source to Voltage output in Range 50V
                   Calys_Set_Range(Function='CURR', CRange=4) - Set Source to Current output in Range 4-20mA
    """
    if Function == 'CURR':
        Calys_Send_Command('SOUR:FUNC CURR')
        Units = 'mA'
        CRange = kwargs.get('CRange', 24)
        if CRange == 0:
            Calys_Send_Command('SOUR:CURR:RANG 0mA')
        elif CRange == 4:
            Calys_Send_Command('SOUR:CURR:RANG 4mA')
        elif CRange == 24:
            Calys_Send_Command('SOUR:CURR:RANG 24mA')
        else:
            print('\x1b[2;30;41m' + 'Incorrect Range of Function (Setup MAX range)...' + '\x1b[0m')
            Calys_Send_Command('SOUR:CURR:RANG 24mA')
    else:
        Calys_Send_Command('SOUR:FUNC VOLT')
        Units = 'V'
        VRange = kwargs.get('VRange', 50)
        if VRange == 100:
            Calys_Send_Command('SOUR:VOLT:RANG 100mV')
            Units = 'mV'
        elif VRange == 2:
            Calys_Send_Command('SOUR:VOLT:RANG 2V')
        elif VRange == 20:
            Calys_Send_Command('SOUR:VOLT:RANG 20V')
        elif VRange == 50:
            Calys_Send_Command('SOUR:VOLT:RANG 50V')
        else:
            print('\x1b[2;30;41m' + 'Incorrect Range of Function (Setup MAX range)...' + '\x1b[0m')
            Calys_Send_Command('SOUR:VOLT:RANG 50V')
    return Units

def Calys_Measurement(Unit, Average):
    pass
    Value: = 0
    return Value

# def Calys_Calibration(*, Start_Cal, Stop_Cal, Step_Cal, End_of_String='V'):
def Calys_Calibration(**kwargs):
    """ This function provides a sequence (loop) of source output values, depends from kwargs
    :param kwargs: Start_Cal(int) - start point for calibration process
                   Stop_Cal(int) - final point for calibration process
                   Step_Cal(int) - delta for changing next output value
                   End_of_Command(str) - units for close output command string ('mV', 'V', 'mA')
    :return: None
    call_examples: Calys_Calibration(Start_Cal=0, Stop_Cal=20, Step_Cal=5, End_of_String='mA')
                   Calys_Calibration(Start_Cal=10, Stop_Cal=100, Step_Cal=10, End_of_String='mV')
    """
    Start_Cal = kwargs.get('Start_Cal', 0)
    Stop_Cal = kwargs.get('Stop_Cal', 0)
    Step_Cal = kwargs.get('Step_Cal', 1)
    End_of_Command = kwargs.get('End_of_Command', 'V')

    for Value in range(Start_Cal, Stop_Cal + 1, Step_Cal):
        if End_of_Command == 'mA':
            Calys_Send_Command('SOUR:CURR ' + str(Value) + End_of_Command)
        elif End_of_Command == 'V' or End_of_Command == 'mV':
            Calys_Send_Command('SOUR:VOLT ' + str(Value) + End_of_Command)
        else:
            print('\x1b[2;30;41m' + 'Incorrect Units...Quit' + '\x1b[0m')
            break
        User_Input = input('\x1b[5;30;42m' + 'Press any key to continue Next Step...' + '\x1b[0m')
        if User_Input.upper() == 'EXIT' or User_Input.upper() == 'QUIT':
            break

    Calys_Send_Command('SOUR:FUNC VOLT')
    Calys_Send_Command('SOUR:VOLT:RANG 2V')
    Calys_Send_Command('SOUR:VOLT 0V')


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
                    Unit = (Calys_Set_Range(Function='VOLT', VRange=100))
                    print(str(Unit))
                    Calys_Calibration(Start_Cal=0, Stop_Cal=100, Step_Cal=25, End_of_Command=Unit)
                elif CalSelector == 2:
                    print("\n2. Start Calibration in range 2V \n")
                    Unit = (Calys_Set_Range(Function='VOLT', VRange=2))
                    Calys_Calibration(Start_Cal=0, Stop_Cal=2, Step_Cal=1, End_of_Command=Unit)
                elif CalSelector == 3:
                    print("\n3. Start Calibration in range 20V \n")
                    Unit = (Calys_Set_Range(Function='VOLT', VRange=20))
                    Calys_Calibration(Start_Cal=0, Stop_Cal=20, Step_Cal=5, End_of_Command=Unit)
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

# Units = (Calys_Set_Range(Function='VOLT', VRange=20))
# Calys_Calibration(Start_Cal=0, Stop_Cal=20, Step_Cal=5, End_of_String=Units)

Calys_Stop()

# time.sleep(5.5) # Pause 5.5 seconds
# wait = input('Press any key to continue...')
# TODO 1) Develop a function for Voltage Measurement use Calys_Calibration as example
#      2) Implement Voltage measurement into Main_Menu
