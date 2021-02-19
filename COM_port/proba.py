Command = ''
while True:
    Command = input('Type your Command and press Enter: ')
    if Command.upper() == 'EXIT':
        break
    Command = Command + '\r\n'
    print(Command)
    print(Command.encode())