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

    def Write(self, line):
        self.writer.writerow(line)
        pass

    def CloseFile(self):
        self.f.close()
        pass