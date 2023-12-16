#1 main.py

import sys
import time
import machine
import uos as os
sys.path.append('/t/System')
sys.path.append('/t/System/Test')
import Boot as device
import SystemTest as fileTest




def runTest():
    writeWater = fileTest.FileTest("/t/System/Test/TestLocation1","Eddy.txt","txt","w")
    writeWater.testMove(folder = "/t/System/Test/TestLocation2",fileName ="TheApple.json",data="I Love Soda", delete = True)
    #writeWater.selfTest()
    return True



def runDevice():
    print("watchdog armed")
    machine.watchdog_on(30)
    while True:
        try:
            time.sleep(1)
            #device.secureBoot()
            machine.watchdog_reset()
        except Exception as e:
            print("at Main",e)





runTest()


