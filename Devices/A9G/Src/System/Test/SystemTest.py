""" SystemTest is Used to Test System Info Will Change!!!!!"""
import Shadow
import time
import uos as os




class FileTest():
        
        
    def __init__(self, folder,fileName,fileExtension,fileType ):
<<<<<<< HEAD
        self.testFile = Shadow.FileHandler(folder,fileName,fileExtension,fileType,)
=======
        self.testFile = Shadow.FileHandler(folder,fileName,fileExtension,fileType)
>>>>>>> 16cbddd627fe4ef9be01d560aa1e5618e0964fc2
        self.testJson = Shadow.JsonHandler(folder,fileName,fileExtension,fileType)
        self.testData = None
        self.randdic = {
    "adventure": "Quest for the Golden Keyboard",
    "participants": ["Alice", "Bob", "Charlie", "Dana"],
    "treasureMap": {
        "island": "CodeIsle",
        "coordinates": "28.135° N, 82.334° W",
        "hiddenTraps": True,
        "clues": ["Follow the looping river", "Beware of the Bug Swamp", "Seek the Valley of Variables"]
    },
    "equipment": {
        "items": ["Laptop of Lore", "Sword of Syntax", "Shield of Servers"],
        "spells": ["Firewall Frenzy", "Curse of the Compiler", "Loop of Levitation"]
    },
    "currentLocation": "Function Forest",
    "distanceToTreasure": "500 lines of code",
    "completedChallenges": 3,
    "funFact": "The whispering trees of Function Forest communicate via Wi-Fi signals.",
    "sideQuests": {
        "Find the Lost USB of Ancient Archives": {
            "reward": "100 XP",
            "status": "Incomplete"
        },
        "Decode the Cryptic Comments": {
            "reward": "Mystery Function",
            "status": "Incomplete"
        }
<<<<<<< HEAD
    }
}

# 
    def selfTest(self):
        file = open("testmydogg.txt", "w+")
        file.write("test")
        file.close()
        os.listdir()
        os.listdir()
    
    
    
    
    
    
class TestJsonHandler():
    def __init__(self, folder,fileName,fileExtension,fileType ):
        self.myDic = {
            "ZAAWorld": True
            
            }
        self.testFile = Shadow.FileHandler(folder,fileName,fileExtension,fileType)
        self.testJson = Shadow.JsonHandler(folder,fileName,fileExtension,fileType,self.myDic)
        self.testData = None
        self.randdic = {
        "adventure": "Quest for the Golden Keyboard"
=======
>>>>>>> 16cbddd627fe4ef9be01d560aa1e5618e0964fc2
    }
}

<<<<<<< HEAD
    def testCloneAndMove(self):
        folder = "/t/System/Test/TestLocation2"
        fileName = "BigBalls"
        dic = self.randdic
        self.testJson.writeDict(dic,"w")
        self.testJson.cloneTo(folder, fileName ,mode = "w" )
        #print("Dict: {0} \n\n FormatedDict: {1}, \n\n Obj: {2}".format(self.testJson.getDict(),self.testJson.formatDict(dic), self.testJson))
    
    def test2(self):
        folder = "/t/System/Test/TestLocation2"
        fileName = "BigBalls"
        dic = self.randdic
        self.testJson.writeDict(dic,"w")
        print(self.testJson.getDict())
        self.testJson.appendDict()
        print("myDic: {0}, \n\n\n MyAppendedDict:".format(self.testJson.getDict()))
        self.testJson.writeDict()
        self.testJson.cloneTo(folder, "newzeLand" ,mode = "w" )
        
        for i in range(45):
            self.testJson.writeDict(dic,"a")
            self.testJson.cloneTo(folder,mode = "w" )
    
    
    
    
    
    
    
    
    #Noticed When fi;eName is all upper Cased, it will force the extension to be as well maybe becuase of how file system works
    def testWrite(self, data = None):
        if data == None:
            data = self.testData
        self.testFile.write(data)
        
    def testMove(self, folder, fileName, data, delete = False):
        self.testWrite(data)
       # self.testFile.cloneTo(folder, fileName ,"w" ,delete)
=======
# 
    def selfTest(self):
        file = open("testmydogg.txt", "w+")
        file.write("test")
        file.close()
        os.listdir()
        os.listdir()
    
    
    
    
    
    def testJsonHandler(self):
        folder = "/t/System/Test/TestLocation2"
        fileName = "Json"
        dic = self.randdic
        print("Dict: {0} \n\n FormatedDict: {1}, \n\n Obj: {2}".format(self.testJson.getDict(),self.testJson.formatDict(dic), self.testJson))
        self.testJson.write(dic,"w")
        self.testJson.cloneTo(folder, fileName ,"w" ,False)
        
        
    
    
    #Noticed When fi;eName is all upper Cased, it will force the extension to be as well maybe becuase of how file system works
    def testWrite(self, data = None):
        if data == None:
            data = self.testData
        self.testFile.write(data)
        
    def testMove(self, folder, fileName, data, delete = False):
        self.testWrite(data)
        self.testFile.cloneTo(folder, fileName ,"w" ,delete)
>>>>>>> 16cbddd627fe4ef9be01d560aa1e5618e0964fc2

    

