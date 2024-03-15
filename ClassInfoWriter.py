import csv
from datetime import datetime

class ClassInfoWriter():
    def __init__(self):
        self.f = None   # f를 이용해 csv파일을 열어주세요
        pass

    def OpenFile(self, filePath, mode):
        self.f = open(filePath,mode, newline='')
        self.writer = csv.writer(self.f)
        
        pass

    def trWrite(self, tdTags, quantity):
        classInfoData = []
        for idx in range(quantity):
            classInfoData.append(tdTags[idx].text)
        
        self.writer.writerow(classInfoData)

        pass
    
    def Write(self, tags):
        self.writer.writerow(tags)
        pass

    def CloseFile(self):
        self.f.close()
        pass