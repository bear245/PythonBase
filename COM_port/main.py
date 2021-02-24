import serial
import time


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


# Initialize Serial port with parameters
ser = serial.Serial(
    port='COM3', \
    baudrate=115200, \
    parity=serial.PARITY_NONE, \
    stopbits=serial.STOPBITS_ONE, \
    bytesize=serial.EIGHTBITS, \
    timeout=None)

Calys_Init()

while True:
    User_Input = input('\nType your Command and press Enter: ')
    if User_Input.upper() == 'EXIT' or User_Input.upper() == 'QUIT':
        break
    if User_Input[-1] == '?':
        Calys_Send_Request(User_Input)
    else:
        Calys_Send_Command(User_Input)

Calys_Stop()

# TODO: Create main menu on dispaly:
#  1) Start Voltage calibration: 1.1 Range 0..1VDC e.t.c.
#  2) Start current calibration: 2.1 Range 0..5mA
#  3) Manual enter CMD
#  4) Exit

# time.sleep(5.5) # Pause 5.5 seconds
# wait = input('Press any key to continue...')
