Command = ''
while True:
    Command = input('Type your Command and press Enter: ')
    if Command.upper() == 'EXIT' or Command.upper() == 'QUIT':
        break
    if Command[-1] == '?':
        print('Request: ' + Command.upper())
        Command = Command + '\r\n'
        print(Command.encode())
    else:
        print('Command: ' + Command.upper())
        Command = Command + '\r\n'
        print(Command.encode())