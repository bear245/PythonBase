import serial
#import io

# Initialize Serial port with parameters
ser = serial.Serial(
    port='COM3',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=None)

# Display a message about successful connection
print("connected to: " + ser.portstr)

# Write BIN array to SERIAL
ser.write(b'*IDN?\r\n')

# Clear output buffer
ser.flush()

# Read all present data from SERIAL
raw_bytes = ser.readline()

# Display received data as UNICODE decoded from BIN Array
print (raw_bytes.decode())

# Close SERIAL port
ser.close()