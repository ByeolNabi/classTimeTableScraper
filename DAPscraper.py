from selenium import webdriver
from selenium.webdriver.common.by import By
import CONST
import csv
from datetime import datetime


class DAPscraper():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.f = None
        
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
        # 강의 한 개의 태그(한 행)을 담은 리스트
        trTags = classInfoTbody.find_elements(by=By.TAG_NAME, value="tr")

        # csv파일을 여는 부분
        # self.f = open("./csv/"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.csv', 'a', newline='')
        self.f = open('./csv/강의정보.csv', 'a', newline='')
        writer = csv.writer(self.f)

        # tr을 한 줄씩 가져오고 write하기
        for trTag in trTags:
            # 강의 정보 앞에서 5개 가져오기 (교과목 번호, 분반, 교과목명, 담당교수, 강의실/교실)
            tdTags = trTag.find_elements(by=By.TAG_NAME, value='td')
            classInfoLine = [tdTags[0].text, tdTags[1].text, tdTags[2].text, tdTags[3].text, tdTags[4].text]
            writer.writerow(classInfoLine)
        
        self.f.close() # 저장하기

        pass

    def ScrapClassInfoAll(self):
        """
        다음쪽 style="color:#D9D9D9;" 일 때까지 다음쪽 클릭
        {이전쪽id:(CP1_COM_Paging_Deu_lBtn_prev),
         다음쪽id:(CP1_COM_Paging_Deu_lBtn_next)}
        """

        # 일단 현재페이지의 정보 저장
        lastPage = False
        while not lastPage:
            # 그 페이지에서 강의 정보 가져오기
            self.ScrapClassInfo()

            # 다음 페이지로 넘어가기  
            nextPage = self.driver.find_element(by=By.ID, value = "CP1_COM_Paging_Deu_lBtn_next")
            colorOfNextPage = nextPage.get_attribute("style")

            # 마지막이 아니면
            if colorOfNextPage != 'color: rgb(217, 217, 217);':
                nextPage.click()
            else:
                # 끝까지 잘 했다.
                lastPage = True

        pass
    
    def Connect(self, dict):
        print("=== 로그인 시작 ===")
        self.Login(dict)
        print("--- 로그인 완료 ---")
        print("=== 수업계획서조회 메뉴로 이동 ===")
        self.GotoClassInfoPage()
        print("--- 수업계획서조회 메뉴로 이동 완료 ---")
        self.ScrapClassInfoAll()
        self.driver.quit()
        pass