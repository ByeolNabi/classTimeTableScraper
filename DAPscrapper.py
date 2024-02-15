from selenium import webdriver
from selenium.webdriver.common.by import By
import CONST
import csv
from datetime import datetime

class DAPscrapper():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.f = open(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.csv','w', newline='')
        
    def Login(self, dict):
        self.driver.get(CONST.URL)
        self.driver.implicitly_wait(5)

        title = self.driver.title
        print("\""+title+"\"에 접속했습니다.")

        text_box = self.driver.find_element(by=By.ID, value=CONST.ID_BOX)
        pw_box = self.driver.find_element(by=By.ID, value=CONST.PW_BOX)
        login_button = self.driver.find_element(by=By.ID, value=CONST.LOGIN_BUTTON)

        print(dict)
        text_box.send_keys(dict.get("username"))
        pw_box.send_keys(dict.get("password"))
        login_button.click()

        pass

    def GotoClassInfoPage(self):
        self.driver.get("https://dap.deu.ac.kr/Student/UCB/UCB0510Q.aspx?mcd=111968&pid=Ucb0510q")

        look_up_info = self.driver.find_element(by=By.ID, value="CP1_BtnOk")
        look_up_info.click()

        pass

    def ScrapClassInfo(self):
        # tbody안에 tr(한 행) 안에 td(행 열)이 존재, 필요한 정보는 앞 5열

        # 강의 정보 테이블 잡아내기
        class_frame = self.driver.find_element(by=By.ID, value="CP1_dt_result")
        class_tbody = class_frame.find_element(by=By.TAG_NAME, value="tbody")
        
        # tr을 한 줄씩 가져오기
        
        pass

    def ScrapClassInfoAll(self):
        # for


        pass
    
    def Connect(self, dict):
        print("=== 로그인 시작 ===")
        self.Login(dict)
        print("--- 로그인 완료 ---")
        print("=== 수업계획서조회 메뉴로 이동 ===")
        self.GotoClassInfoPage()
        print("--- 수업계획서조회 메뉴로 이동 완료 ---")
        # ScrapInfo()
        # driver.quit()
        pass