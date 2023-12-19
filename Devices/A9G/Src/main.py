#1 main.py

import sys
import time
import machine
import ujson as json
import uos as os
sys.path.append('/t/System')
sys.path.append('/t/System/Test')
import Boot as device
import SystemTest as fileTest



randdic = {
    "name": "Example",
    "type": "Test Data",
    "items": [1, 2, 3, 4, 5]
}

data = json.dumps(randdic)


def runTest():
    writeWater = fileTest.TestJsonHandler("/t/System/Test/TestLocation1","SystemData",".json","text")
#     writeWater.testCloneAndMove()
    #writeWater.test3()
    writeWater.reNameTest3()
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


