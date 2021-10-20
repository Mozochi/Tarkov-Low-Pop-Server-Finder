from datetime import datetime, timedelta
menu = 0
mainLoop = True

def mainMenu():
    print("1. Show all server times")
    print("2. Only show servers with low pop")
    menuInput = int(input("3. Change daylight saving(CHECK ONLINE)"))

    if menuInput == 1:
        for i in range (len(serverTimezones)):
            serverTime(serverTimezones[i][0], serverTimezones[i][1], "all")
            pass

    elif menuInput == 2:
        for i in range (len(serverTimezones)):
            serverTime(serverTimezones[i][0], serverTimezones[i][1], "selective")

    elif menuInput == 3:
        print("Enter current UTC time...")
        userUTC = input(">")

    else: 
        mainMenu()


def serverTime(serverName, serverTimeDiff, output):
    currentUTC = datetime.utcnow()
    serverTime = currentUTC+(timedelta(hours = int(serverTimeDiff)))
    serverTime = serverTime.strftime("%H:%M")

    if output == "all":
        print(serverName, serverTime)

    if output == "selective":
        print("Selective")



serverTimezones = [["Netherlands","1"], ["London","1"], ["France", "2"], ["Switzerland","2"], ["Germany","2"], ["Poland","2"], ["Czech","2"], ["Austria","2"], ["Italy","2"], ["Spain","2"], ["Slovakia","2"], ["Sweeden","2"], ["Finland","3"], ["SaintPetersburg","3"], ["Bulgaria","3"], ["Ukraine","3"], ["Turkey","3"], ["Romania","3"], ["Israel","3"], ["Moscow","3"], ["Ekaterinburg","5"], ["WashingtonDC","-4"], ["NewYork","-4"], ["Beauharnois","-4"], ["Novosibrisk","7"], ["Montreal","-4"], ["Chicago","-5"], ["Toronto","-4"], ["Atlanta","-4"], ["Krasnoyarsk","7"], ["StLouis","-5"], ["Miami","-4"], ["Orlando","-4"], ["Dallas","-5"], ["Denver","-6"], ["Kazakhstan","6"], ["California","-7"], ["Phoenix","-7"], ["Khabarorvsk","10"], ["Vladivostok","10"], ["Vancouver","-7"], ["Seattle","-7"], ["Singapore","8"], ["Johannesburg","2"], ["SanPaulo","-3"], ["Japan","9"], ["Seoul","9"], ["HongKong","8"], ["Australia","11"]]


#serverTime(serverTimezones[37][0], serverTimezones[37][1])


#while mainLoop == True:
#for i in range (len(serverTimezones)):
#    serverTime(serverTimezones[i][0], serverTimezones[i][1])
    


#for i in serverTimezones
#serverTime(serverTimeZones[i])


mainMenu()