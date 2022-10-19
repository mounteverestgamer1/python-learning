command = ""
started = False
stop = False
while True:
    command = input(">").lower()
    if command == 'start':
        if started:
            print("the car is already started")
            
        else:
            started = True
            print('the car is started')
    elif command == 'stop' :
        if stop:
            print("the car is already stoppped")
        else:
            stop = True
            print('the car is stopped')
    elif command == 'help':
        print("""
              start - to start the car
              stop - to stop the car
              quit - to quit
              """)
    elif command == 'quit':
        break
    else:
        print("i don't understand that")
        break
        

