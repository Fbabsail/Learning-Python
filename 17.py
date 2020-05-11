
#total faliure


command=input()
while command.upper() != 'QUIT':
    if command.upper() == 'START':
        print('Car started...')
    elif command.upper() == 'STOP':
        print('Car stopped.')
    elif command.upper() == 'EXIT':
        break
    elif command.upper() == 'HELP':
        print('Start - to start the car')
        print('Stop - to stop the car')
        print('Exit - to quit program')
    elif command.upper() != 'HELP'and 'EXIT' and 'STOP'and 'START':
        print("I don't understand that")







     



