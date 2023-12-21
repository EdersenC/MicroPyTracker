##boot
import Device
import Shadow
import gps


file = Shadow.JsonHandler("/t/System/Secrete","secret",".json","text")
file.appendDict()
secrets = file.getDict()
myserver = secrets["server"]
apn = secrets["apn"]
token = secrets["token"]
headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}    
def secureBoot2():
    jsosn = Shadow.JsonHandler("/t/System/","LocationData",".json","text")
    jsosn.clearDict()
    net = Device.Network(apn = apn,user="",password="", timeout = 0)
    net.setServer(myserver)
    net.setHeader(headers)
    print(net.status)
    A9G = Device.A9G(net=net,locationData = jsosn)
    A9G.enableGps()
    #net.printStatus()
    A9G.pingLocation(100)
    #print(A9G.getCurrentLocation())
