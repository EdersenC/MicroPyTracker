
import ujson as json
import gps
import Shadow



 
class Device():
    def __init__(self, name, id, type, value):
        self.name = name
        self.id = id
        self.type = type
        self.value = value
    


class A9G(Device):
    def __init__(self):
        self.states = Shadow.State()
        pass

    def enableGps(self, enabled = True):
        if enabled and self.states.getValue('gps')==False:
            print(self.states.getDict())
            gps.on()
            print(self.states.get('gps'))
            self.states.update('gps', True)
            print(self.states.getDict())
            return True
        gps.off()
        
            
