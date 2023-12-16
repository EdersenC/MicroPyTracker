
import ujson as json
import uos as os
import time

""" Shadow class is used to logg and store Device information"""
class Shadow():
    def __init__(self, file, mode, formating):
        self.file = file
        self.mode = mode
        self.formating = formating
        pass


    def log(self, message, type):
        with open(self.file, self.mode) as f:
            f.write(message.format(self.formating))
        pass

    
def deBugFunction(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("{0} executed in {1:.4f}s".format(func.__name__, elapsed_time))
        return result
    return wrapper


class Flags():
    def __init__(self):
        self.SystemStates = {
        "GPS": False,
        "wifi": False,
        "bluetooth": False,
        "usb": False,
    }

    def getDict(self):
        return self.SystemStates



class State():
    def __init__(self):
        FLAGS = Flags()
        self.stateData = FLAGS.getDict()
        pass

    def getValue(self, key):
        return self.stateData[key]

    def update(self, key, value):
        self.stateData[key] = value
    
    def getDict(self):
        return self.stateData
            
    def saveState(self, func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            pass









class File(): 
    def __init__(self, fileLocation,fileName, extension, fileType,):
        self.folder = folder
        self.fileName = fileName
        self.setFileLocation(self.folder, self.fileName)
        self.fileLocation = self.getFile
        self.extension = extension
        self.fileType = fileType
        
        
        
    def setFile(self, folder, file):
        if not folder.endswith('/'):
            self.fileLocation = folder+"/"+file
        self.fileLocation = folder+file
        
    def getFileType(self):
        return self.fileType

    def getFileLocation(self):
        return self.fileLocation

    def setFileLocation(self, fileLocation):
        self.fileLocation = fileLocation
        
    

    def getFileLocation(self):
        return self.fileLocation
















class File(): 
    def __init__(self, fileLocation, extension, fileType, mode):
        self.fileLocation = fileLocation
        self.extension = extension
        self.mode = mode
        self.file = open(fileLocation,mode)
        self.fileType = fileType
        
            
    def close(func):
        def wrapper(self,*args, **kwargs):
            run = func(self,*args, **kwargs)
            self.file.close()
            return run 
        return wrapper

    def deBugFunction(func):
        def wrapper(self,*args, **kwargs):
            
            start_time = time.time()
            result = func(self,*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            class_name = self.__class__.__name__
            print("The Funciton: {0} From Class: {1} executed in {2:.4f}s".format(func.__name__,class_name, elapsed_time))
            return result
        return wrapper
     
    def getFileType(self):
        return self.fileType

    def getFileLocation(self):
        return self.fileLocation

    def setFileLocation(self, fileLocation):
        self.fileLocation = fileLocation
        
    def setFile(self,fileLocation = None,mode = None):
        if mode is None:
            mode = self.mode
        if fileLocation is None:
            fileLocation = self.fileLocation
        self.file.close()
        self.file = open(fileLocation,mode)
        
    @close        
    def closer(self):
        self.file.close()
        
    @close
    @deBugFunction
    def write(self, data):
        self.file = open(self.fileLocation,'w+')
        self.file.write(data)
        
    @close
    def remove(self):
        print(self.fileLocation)
        os.remove(self.getFileLocation())
        
    def cloneTo(self, fileLocation):
        clone = File(fileLocation,self.extension, self.fileType, "w+")
        self.closer()
        self.setFile(None,"r")
        data = self.file.read()
        self.closer()
        clone.write(data)
        return clone
    
    
    
    @close
    def moveTo(self, fileLocation, mode = None):
        if mode is None:
            mode = self.mode
        clone = self.cloneTo(fileLocation)
        clone.write("RainDrop")
        clone.closer()
        self.remove()
        self.setFileLocation(clone.getFileLocation())
        self.setFile(clone.getFileLocation(), mode)










