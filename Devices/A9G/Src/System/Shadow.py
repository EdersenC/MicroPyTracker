
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
  
    def getFileType(self):
        return self.fileType
    def getExtension(self):
        return self.extension
    def getFile(self):
        #print("File: {0} in Get file".format(self.file))
        return self.file
    def getFileName(self):
        return self.fileName
    def getFolder(self):
        return self.folder
    def setFolder(self,folder):
        self.folder = folder
    def setFileName(self,fileName):
        self.fileName = fileName
        
    def setFile(self, folder = None, fileName= None, extension= None):
        print("\nObjects:\nfolder:{0} \nFile:{1} \nextension:{2}".format(self.getFolder(),self.getFileName(),self.getExtension()))
        print("\nObjects:\nfolder:{0} \nFile:{1} \nextension:{2}".format(folder,fileName,extension))    
        if extension is None:
            extension = self.getExtension()
        if folder is None or fileName is None:
            self.setFile(self.getFolder(), self.getFileName(), self.getExtension())
        else:
            self.file = folder+fileName+extension
            if not folder.endswith('/'):
                self.setFolder(folder+"/")
                self.setFileName(fileName)
                self.file = self.getFolder()+self.getFileName()+self.getExtension()
               # print("File: {0} After ".format(self.file))
        
    
    # TODO: Implement Mode Error handling "w+" errors
    def write(self, data, mode="w"):
        print("Yooooooo in here")
        try:
            with open(self.file, mode) as file:
                #print("File: {0}, Data: {1}, Obj: {2}".format(self.file, data, file))
                file.write(data)
            return True
        except Exception as e:
            #Sprint("Error writing to file: {0}".format(e))
            return False
    
    def exists(self, file= None):
        if file is None:
            file = self.file
        try:
            os.stat(file)
            return True
        except Exception as e:
            return False
        
         #Could implement folder Renaming!!!
    def reName(self,fileName = None):
        newFile = str(self.getFolder()+fileName+self.getExtension())
        if self.exists(newFile):
            return "File With same Name already exist's"
        if self.exists():
            os.rename(self.getFile(),newFile)
            self.setFile(self.getFolder(), fileName, self.getExtension())
            return True
        return "Cant Do That you Fool What File!!!!"
        
    def read(self,mode = 'r+'):
        with open(self.file, mode) as f:
            contents = f.read()
            f.close()
            return contents
            return " "
    def remove(self):
            os.remove(self.file)
            
    def cloneTo(self, folder ="",fileName = None, mode = "w", delete = False,):
        newFile = fileName
        if fileName == None:
            newFile = self.fileName+ str(random.randrange(10))
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
        self.folder = folder
        self.fileName = fileName
        self.extension = extension
        self.setFile(folder, fileName, extension)
        self.file = self.getFile()
        self.fileType = fileType
        self.dic = dic
        self.cloneDict = {"first":self.file}
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
        



    
    
    
    
    
    
    
    
    
    
    
    


