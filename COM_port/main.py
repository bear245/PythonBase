import serial
import time


def Calys_Init():
    print("Connected to: " + ser.portstr)   # Display a message about successful connection
    ser.write(b'*IDN?\r\n')                 # Write BIN array to SERIAL
    ser.flush()                             # Clear output buffer
    raw_bytes = ser.readline()              # Read all present data from SERIAL
    print(raw_bytes.decode())               # Display received data as UNICODE decoded from BIN Array
    ser.write(b'REM\r\n')

def Calys_Stop():
    print('Disconnected')
    ser.write(b'LOC\r\n')
    # Close SERIAL port
    ser.close()

# Initialize Serial port with parameters
ser = serial.Serial(
        port='COM3', \
        baudrate=115200, \
        parity=serial.PARITY_NONE, \
        stopbits=serial.STOPBITS_ONE, \
        bytesize=serial.EIGHTBITS, \
        timeout=None)

Calys_Init()

# time.sleep(5.5) # Pause 5.5 seconds
#wait = input('Press any key to continue...')
Command = ''
while True:
    Command = input('Type your Command and press Enter: ')
    if Command.upper() == 'EXIT':
        break
    Command = Command + '\r\n'
    print(Command)
    print(Command.encode())
    ser.write(Command.encode())

Calys_Stop()