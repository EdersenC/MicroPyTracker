
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









class FileHandler(): 
    def __init__(self, folder,fileName, extension, fileType,config = None):
        self.config = config
        self.folder = folder
        self.fileName = fileName
        self.extension = extension 
        self.setFile(self.folder, self.fileName, self.extension)
        self.fileType = fileType
        
    def setFile(self, folder, file, extension):
        self.file = folder+file+extension
        #print("File: {0} Before".format(self.file))
        #print(folder.endswith('/'))
        if not folder.endswith('/'):
            self.file = folder+"/"+file+extension
           # print("File: {0} After ".format(self.file))
            
    def getFileType(self):
        return self.fileType
    def getFile(self):
        #print("File: {0} in Get file".format(self.file))
        return self.file
    def getFileName(self):
        return self.fileName
    def getFolder(self):
        return self.folder
    
    
    # TODO: Implement Mode Error handling "w+" errors
    def write(self, data, mode="w"):
        try:
            with open(self.file, mode) as file:
                #print("File: {0}, Data: {1}, Obj: {2}".format(self.file, data, file))
                file.write(data)
            return True
        except Exception as e:
            #Sprint("Error writing to file: {0}".format(e))
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
            newFile = "TestMove"+ str(random.randrange(10))
        clone = FileHandler(folder, newFile, self.extension, self.fileType)
        clone.write(self.read(),mode)
        if delete:
            self.remove()
            self.setFile(self.folder, self.fileName,self.extension)
        del clone
        return True 




class JsonHandler(FileHandler):
    import ujson as json
    def __init__(self, folder, fileName, extension, fileType, dic = {} ):
       # self.fileHandler = FileHandler(folder,fileName, extension, fileType)
        self.setFile(folder, fileName, extension)
        self.file = self.getFile()
        self.folder = folder
        self.fileName = fileName
        self.extension = extension
        self.fileType = fileType
        self.dic = dic
        pass
    
    
    # could implment formtJson
    def formatDict(self, dic):
        return json.dumps(dic)
    
    def getDict(self):
        return self.dic
    
    
    def appendDict(self):
        self.dic.update(json.loads(self.read()))      
    
    
    def writeDict(self, dic = None, mode = "w"):
        if dic is None:
            dic = self.getDict()
        self.write(self.formatDict(dic), mode)
        



    
    
    
    
    
    
    
    
    
    
    
    


