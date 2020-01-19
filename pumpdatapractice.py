from datetime import datetime

def offerChoices(pumpState):
    if pumpState == "Y":
        print("Pump is on")
        startTime = datetime.now()
        print("current time is", startTime)
         

    elif pumpState == "N":
        print("Pump is not on")
    else:
        print("Invalid Response")

    if pumpState == "Y":
        isPumpStillOn = input("Is pump still on? Y/N: ")
        if isPumpStillOn == "Y":
            print("Pump is still on")
        elif isPumpStillOn == "N":
            print("Pump is off")
            endTime = datetime.now()
            print("current time is", endTime)
            runtime = endTime-startTime
            print("Total time pump was on:", runtime, runtime.seconds)
            writetofile(str(startTime) + "," + str(runtime.seconds))
            readfile()
        else:
            print("Invalid Response")

def writetofile(stringtowrite):
    f = open("pumpcontent.txt", "a")
    f.write(" %s\n" % stringtowrite)
    f.close()

def readfile():
    f = open("pumpcontent.txt", "r")
    print(f.read())
    f.close()

while True:

    isPumpOn = input("Is pump on? Y/N: ")

    offerChoices(isPumpOn)



