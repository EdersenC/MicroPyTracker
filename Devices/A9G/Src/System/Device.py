import urequests as url
import ujson as json
import gps
import cellular as cell
import machine as MC


class Device():
    def __init__(self, name, id, type, value):
        self.name = name
        self.id = id
        self.type = type
        self.value = value



class A9G(Device):
    def __init__(self, SystemStats = None, net= None, locationData = None):
        self.cordnates = ["latitude","longitude"]
        self.SystemStats = SystemStats
        self.net = net
        self.locationData = locationData
        locationData.appendDict()
        self.locationDict = locationData.getDict()
        self.latitude  = self.getLatitude()
        self.longitude = self.getLongitude()
        
                

    def enableGps(self, enabled = True):
        if enabled is False:
            gps.on()
        else:
            gps.off
            
            
    def getLatitude(self):
        return self.locationDict["location"][self.cordnates[0]]
    
    def getLongitude(self):
         return self.locationDict["location"][self.cordnates[1]]
    
    def updateLocation(self,location):
        for i in range(len(self.cordnates)):
            self.locationData.updateDict(key= self.cordnates[i], value = location[i])
            
            
            
    def printStatus(self):
        print("Satellites: {0}".format(gps.get_satellites()))
            
    def getCurrentLocation(self):
        return [self.getLatitude(),self.getLongitude()]
            
            
    def getLocation(self,currentLocaion = True):
        lastlocation = self.getCurrentLocation()
        try:
            if currentLocaion is True:
                location = gps.get_location()
                self.updateLocation(location)
                self.locationData.writeDict()
                return self.getCurrentLocation()
        except Exception as e:
            return lastlocation
        return gps.getLastLocation()


    def pingLocation(self,radius):
        self.net.pingServer(self.locationDict)
        
        
        
    
    






    
class Network():
    def __init__(self,apn = None,user="",password="", timeout = 0):
#         self.states = Shadow.State()
#         self.SystemStats = SystemStats
        self.apn = apn
        self.user = user
        self.headers = {}
        self.server = None
        self.password = password
        self.timeout = timeout
        self.start(self.apn,self.user,self.password,self.timeout)
        
    def status(self):
        try:
            return cell.gprs()
        except Exception as e:
            return False
    def printStatus(self):
        print("\nDevice: \nImei:{0}, \n Sim Present:{1}, \n Imei:{2}, \n netRegistered:{3}, \n Cellular Stations:{4}".format(
            cell.get_imei(),
            cell.is_sim_present(),
            cell.get_signal_quality(),
            cell.is_network_registered(),
            cell.stations()))
    
    
    def isActive(self):
        return cell.is_network_registered()
        
    
    def reset(self):
        cell.reset()

    def start(self,apn = None,user="",password="", timeout = 0):
        if self.status() is False:
            if apn is None:
                return "U Cant Do ThaT LOL"
            try:
                cell.gprs(apn, user, password)
                return True
            except Exception as e:
                return False
        return "NetWork Already Connected"
    
    
    def setServer(self, server):
        self.server = server
        
    
    def setHeader(self, headers):
        self.headers = headers
        
    
    def endNet(self):
        cell.gprs(False)
        
    def pingServer(self, dic={}, retries=3):
        jsondump = json.dumps(dic)
        for attempt in range(retries):
            try:
                r = url.post(self.server, headers=self.headers, data=jsondump)
                print("{}, {}".format(r.status_code, r.text))
                return True
            except Exception as e:
                print("An error occurred on attempt {} at pingServer: {}".format(attempt + 1, e))
                if attempt < retries - 1:
                    print("Retrying...")
                    continue
                else:
                    print("Max retries reached.")
                    self.endNet()
                    self.reset()# Assuming MC is defined and accessible
                    return False
        
    
    
#     def enableGps(self, enabled = True):
#         if enabled and self.states.getValue('gps')==False:
#             print(self.states.getDict())
#             gps.on()
#             print(self.states.get('gps'))
#             self.states.update('gps', True)
#             print(self.states.getDict())
#             return True
#         gps.off()
        

