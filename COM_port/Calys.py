import serial
# Initialize Serial port with parameters
ser = serial.Serial(
    port='COM3', \
    baudrate=115200, \
    parity=serial.PARITY_NONE, \
    stopbits=serial.STOPBITS_ONE, \
    bytesize=serial.EIGHTBITS, \
    timeout=None)

def Init():
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


def Stop():
    """This function realize stop of Hardware (Calys75)
    change device's state to Local work (LOC) and close SERIAL
    :return: None
    """
    ser.write(b'LOC\r\n')
    ser.close()  # Close SERIAL port
    print('Disconnected')


def Send_Command(Command):
    """This function transform user input(string) into HW command(bytes),
    display it and write to SERIAL
    :param Command: User input from keyboard
    :return: None
    """
    Command = Command + '\r\n'
    print('Send Command: ' + str(Command.encode()))
    ser.write(Command.encode())


def Send_Request(Command):
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


def Set_Range(*, Function=('VOLT', 'CURR'), **kwargs):
    """This function sets Source output function of HW
    and sets it to correct or maximum Range
    :param Function: 'VOLT' - for Voltage, 'CURR' - for current
    :param kwargs: VRange: int=(100, 2, 20, 50) - set range for Voltage, 100mV, others in V
                   CRange: int=(0, 4, 24) - set range for Current, mA
    :return: Units - string, depends from range
    call examples: Calys.Set_Range(Function='VOLT', VRange=50) - Set Source to Voltage output in Range 50V
                   Calys.Set_Range(Function='CURR', CRange=4) - Set Source to Current output in Range 4-20mA
    """
    if Function == 'CURR':
        Send_Command('SOUR:FUNC CURR')
        Units = 'mA'
        CRange = kwargs.get('CRange', 24)
        if CRange == 0:
            Send_Command('SOUR:CURR:RANG 0mA')
        elif CRange == 4:
            Send_Command('SOUR:CURR:RANG 4mA')
        elif CRange == 24:
            Send_Command('SOUR:CURR:RANG 24mA')
        else:
            print('\x1b[2;30;41m' + 'Incorrect Range of Function (Setup MAX range)...' + '\x1b[0m')
            Send_Command('SOUR:CURR:RANG 24mA')
    else:
        Send_Command('SOUR:FUNC VOLT')
        Units = 'V'
        VRange = kwargs.get('VRange', 50)
        if VRange == 100:
            Send_Command('SOUR:VOLT:RANG 100mV')
            Units = 'mV'
        elif VRange == 2:
            Send_Command('SOUR:VOLT:RANG 2V')
        elif VRange == 20:
            Send_Command('SOUR:VOLT:RANG 20V')
        elif VRange == 50:
            Send_Command('SOUR:VOLT:RANG 50V')
        else:
            print('\x1b[2;30;41m' + 'Incorrect Range of Function (Setup MAX range)...' + '\x1b[0m')
            Send_Command('SOUR:VOLT:RANG 50V')
    return Units

def Measurement(Unit, Average):
    pass
    Value = 0
    return Value

# def Calys_Calibration(*, Start_Cal, Stop_Cal, Step_Cal, End_of_String='V'):
def Calibration(**kwargs):
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
            Send_Command('SOUR:CURR ' + str(Value) + End_of_Command)
        elif End_of_Command == 'V' or End_of_Command == 'mV':
            Send_Command('SOUR:VOLT ' + str(Value) + End_of_Command)
        else:
            print('\x1b[2;30;41m' + 'Incorrect Units...Quit' + '\x1b[0m')
            break
        User_Input = input('\x1b[5;30;42m' + 'Press any key to continue Next Step...' + '\x1b[0m')
        if User_Input.upper() == 'EXIT' or User_Input.upper() == 'QUIT':
            break

    Send_Command('SOUR:FUNC VOLT')
    Send_Command('SOUR:VOLT:RANG 2V')
    Send_Command('SOUR:VOLT 0V')
