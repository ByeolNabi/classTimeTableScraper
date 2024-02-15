from selenium import webdriver
from selenium.webdriver.common.by import By
import CONST

class DAPscrapper():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def Login(self, dict):
        self.driver.get(CONST.URL)
        self.driver.implicitly_wait(0.5)

        title = self.driver.title
        print("\""+title+"\"에 접속했습니다.")

        self.driver.implicitly_wait(0.5)

        text_box = self.driver.find_element(by=By.ID, value=CONST.ID_BOX)
        pw_box = self.driver.find_element(by=By.ID, value=CONST.PW_BOX)
        login_button = self.driver.find_element(by=By.ID, value=CONST.LOGIN_BUTTON)

        print(dict)
        text_box.send_keys(dict.get("username"))
        pw_box.send_keys(dict.get("password"))
        login_button.click()

        pass

    def GotoTarget(self):
        class_info_menu = self.driver.find_element(by=By.ID, value=CONST.CLASS_INFO_MENU)

        class_info_menu.click()

        pass

    def ScrapClassInfo(self):
        

        pass

    def ScrapClassInfoAll(self):
        # for


        pass
    
    def Connect(self, dict):
        print("=== 로그인 시작 ===")
        self.Login(dict)
        print("--- 로그인 완료 ---")
        print("=== 수업계획서조회 메뉴로 이동 ===")
        self.GotoTarget()
        print("--- 수업계획서조회 메뉴로 이동 완료 ---")
        # ScrapInfo()
        # driver.quit()
        pass