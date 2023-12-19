""" SystemTest is Used to Test System Info Will Change!!!!!"""
import Shadow
import time
import uos as os




class FileTest():
        
        
    def __init__(self, folder,fileName,fileExtension,fileType ):
        self.testFile = Shadow.FileHandler(folder,fileName,fileExtension,fileType,)
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
        #self.testFile = Shadow.FileHandler(folder,fileName,fileExtension,fileType)
        self.testJson = Shadow.JsonHandler(folder,fileName,fileExtension,fileType,self.myDic)
        self.testData = None
        self.randdic = {
        "adventure": "Quest for the Golden Keyboard"
    }

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
    
    
    def testCloneMem(self):
        folder = "/t/System/Test/TestLocation_Clones"
        fileName = "myClone"
        dic = self.randdic
        self.testJson.writeDict(dic,"w")
        print(self.testJson.getDict())
        self.testJson.appendDict()
        print("myDic: {0}, \n\n\n MyAppendedDict:".format(self.testJson.getDict()))
        self.testJson.writeDict()
        self.testJson.cloneTo(folder, "newzeLand" ,mode = "w" )
        print(self.testJson.exists())
        self.testJson.remove()
        print(self.testJson.exists())
    
    
    def reNameTest3(self):
        dic = self.randdic
        json = self.testJson
        LOOP = 2
        json.writeDict(dic,"w")
        folders = ["/t/System/Test/TestLocation1","/t/System/Test/TestLocation2","/t/System/Test/TestLocation3","/t/System/Test/TestLocation4"]
        differentList = ["OceanWaves", "MountainPeak", "DesertMirage", "ForestTrail", "RiverBend", "StarrySky", "SunnyMeadow", "RainyCity", "SnowyVillage"]
        fileNames = ["LargeBallons", "GiantCats", "MySystemStoarge", "BigStuffTimmy", "LongJohnJhonson", "MyepicLavaPit", "1987Wor_end", "THEWORLD", "POSEPOSE"]
        for i in range(LOOP):
            innerFolder = folders[i]
            for j in range(len(fileNames)):
                json.setFile(
                        folder = innerFolder,
                        fileName = fileNames[j]
                        )
                json.reName(differentList[j])
                print("MyFile: {0}, \n\n\n MyAppendedDict:".format(json.getFile()))
                
        
        
    
    def test3(self):
        folders = ["/t/System/Test/TestLocation1","/t/System/Test/TestLocation2","/t/System/Test/TestLocation3","/t/System/Test/TestLocation4"]
        differentList = ["OceanWaves", "MountainPeak", "DesertMirage", "ForestTrail", "RiverBend", "StarrySky", "SunnyMeadow", "RainyCity", "SnowyVillage"]
        fileNames = ["LargeBallons", "GiantCats", "MySystemStoarge", "BigStuffTimmy", "LongJohnJhonson", "MyepicLavaPit", "1987Wor_end", "THEWORLD", "POSEPOSE"]

        
        dic = self.randdic
        json = self.testJson
        LOOP = 2
        json.writeDict(dic,"w")
        json.reName("BigStuffT")
        json.writeDict(dic,"w")        
        
        for i in range(LOOP):
            innerFolder = folders[i]
            for j in fileNames:
                json.setFile(
                    folder = innerFolder,
                    fileName = j
                    )
                json.writeDict(dic,"w")
                json.reName(j)
                if j == "LargeBallons":
                    json.writeDict(dic,"a")
                    json.writeDict(dic,"a")
                    json.writeDict(dic,"a")
                    
                print("MyFile: {0}, \n\n\n MyAppendedDict:".format(json.getFile()))
    
    
    #Noticed When fi;eName is all upper Cased, it will force the extension to be as well maybe becuase of how file system works
    def testWrite(self, data = None):
        if data == None:
            data = self.testData
        self.testFile.write(data)
        
    def testMove(self, folder, fileName, data, delete = False):
        self.testWrite(data)
       # self.testFile.cloneTo(folder, fileName ,"w" ,delete)

    

