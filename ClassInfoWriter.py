import csv
from datetime import datetime

def ClassInfoWriter():
    def __init__(self):
        self.f = None   # f를 이용해 csv파일을 열어주세요
        pass

    def OpenFile(self, filePath, mode):
        self.f = open("./csv/"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.csv',mode, newline='')
        
        pass

    def closeFile(self):
        self.f.close()
        pass

    def write(self):
        self.OpenFile()



        pass