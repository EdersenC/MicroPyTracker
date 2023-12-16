""" SystemTest is Used to Test System Info Will Change!!!!!"""
import Shadow
import time
import uos as os

class FileTest(): 
    
    def __init__(self, file, extension,fileType, mode ):
        self.file = file
        self.testFile = Shadow.File(file,extension,fileType,mode)
        self.testData = "WaterMellon"

    def selfTest(self):
        file = open("test.txt", "w+")
        file.write("test")
        file.close()
        os.listdir()
        os.listdir()

    
    def create(self, data = None):
        if data == None:
            data = self.testData
        self.testFile.write(data)
    
    def remove(self):
        self.testFile.remove()
        
    
    
    def moveClone(self):
        #self.selfTest()
        #self.create()
        self.remove()
        #self.testFile.moveTo("TestingMyPasta.txt")
        #self.cloneTo("/t/System/Test/TestLocation2")
        return True 
    

