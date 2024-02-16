from selenium import webdriver
from selenium.webdriver.common.by import By
import CONST

class DAPscraper():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
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
        classInfoFrame = self.driver.find_element(by=By.ID, value="CP1_dt_result")
        classInfoTbody = classInfoFrame.find_element(by=By.TAG_NAME, value="tbody")
        # 강의 한 개의 태그(한 행)
        trTags = classInfoTbody.find_elements(by=By.TAG_NAME, value="tr")
        # 강의 정보 앞에서 5개 가져오기 (교과목 번호, 분반, 교과목명, 담당교수, 강의실/교실)
        for trTag in trTags:
            tdTags = trTag.find_elements(by=By.TAG_NAME, value='td')
            classInfoLine = [tdTags[0].text, tdTags[1].text, tdTags[2].text, tdTags[3].text, tdTags[4].text]
            

        print("dfk")
        
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
        self.ScrapClassInfo()
        # driver.quit()
        pass