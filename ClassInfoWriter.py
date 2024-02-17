import csv
from datetime import datetime

def ClassInfoWriter():
    def __init__(self):
        self.f = open("./csv/"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.csv','w', newline='')
        pass

    def OpenFile(self, filePath, mode):
        self.f = open("./csv/"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.csv',mode, newline='')
        
        pass

    def closeFile(self):
        self.f.close()
        pass

    def Append(self):
        self.OpenFile()



        pass