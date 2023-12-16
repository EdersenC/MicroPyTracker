
import ujson as json
import uos as os
import urandom as random
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
        def wrapper(self,*args, **kwargs):
            start_time = time.time()
            result = func(self,*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            class_name = self.__class__.__name__
            print("The Funciton: {0} From Class: {1} executed in {2:.4f}s".format(func.__name__,class_name, elapsed_time))
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
    def __init__(self, folder,fileName, extension, fileType):
        self.folder = folder
        self.fileName = fileName
        self.file = None
        self.setFile(self.folder, self.fileName)
        self.extension = "."+extension
        self.fileType = fileType
        
    def setFile(self, folder, file):
        self.file = folder+file
        print("File: {0} Before".format(self.file))
        print(folder.endswith('/'))
        if not folder.endswith('/'):
            self.file = folder+"/"+file
            print("File: {0} After ".format(self.file))
            
    def getFileType(self):
        return self.fileType
    def getFile(self):
        print("File: {0} in Get file".format(self.file))
        return self.file
    def getFileName(self):
        return self.fileName
    def getFolder(self):
        return self.folder
    
    
    # TODO: Implement Mode Error handling "w+" errors
    def write(self, data, mode="w"):
        try:
            with open(self.file, mode) as file:
                print("File: {0}, Data: {1}, Obj: {2}".format(self.file, data, file))
                file.write(data)
            return True
        except Exception as e:
            print("Error writing to file: {0}".format(e))
            return False

        
    def read(self,mode = 'r+'):
        with open(self.file, mode) as f:
            contents = f.read()
            f.close()
            return contents
            return " "
    def remove(self):
            os.remove(self.file)
            
    def cloneTo(self, folder ="",fileName = None, mode = "w", delete = False):
        newFile = fileName
        if fileName == None:
            newFile = "TestMove"+ str(random.randrange(10))+self.extension
        clone = File(folder, newFile, self.extension, self.fileType)
        clone.write(self.read())
        if delete:
            self.remove()
            self.setFile(self.folder, self.fileName)
        del clone
        return True 


