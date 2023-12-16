""" SystemTest is Used to Test System Info Will Change!!!!!"""
import Shadow
import time
import uos as os

class FileTest():
    
    def __init__(self, folder,fileName,fileExtension,fileType ):
        self.testFile = Shadow.File(folder,fileName,fileExtension,fileType)
        self.testData = None
# 
    def selfTest(self):
        file = open("testmydogg.txt", "w+")
        file.write("test")
        file.close()
        os.listdir()
        os.listdir()
    
    def testWrite(self, data = None):
        if data == None:
            data = self.testData
        self.testFile.write(data)
        
    def testMove(self, folder, fileName, data, delete = False):
        self.testWrite(data)
        os.listdir("/t/System/")
        self.testFile.cloneTo(folder, fileName ,"w" ,delete)

    

