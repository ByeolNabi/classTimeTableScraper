from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ClassInfoWriter import ClassInfoWriter

URL = "http://sugang.deu.ac.kr:8080/DEUSugang_Login.aspx"
ID_BOX = "txtID"
PW_BOX = "txtPW"
LOGIN_BUTTON = "ibtnLogin"

class SugangScraper():
    def __init__(self):
        self.URL = "http://sugang.deu.ac.kr:8080/DEUSugang_Login.aspx"
        self.ID_BOX = "txtID"
        self.PW_BOX = "txtPW"
        self.LOGIN_BUTTON = "ibtnLogin"

        self.driver = webdriver.Chrome()
        self.f = None
        self.csvCtrl = ClassInfoWriter()
        
    def Login(self, dict):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

        title = self.driver.title
        print("\""+title+"\"에 접속했습니다.")

        text_box = self.driver.find_element(by=By.ID, value=self.ID_BOX)
        pw_box = self.driver.find_element(by=By.ID, value=self.PW_BOX)
        login_button = self.driver.find_element(by=By.ID, value=self.LOGIN_BUTTON)

        print(dict)
        text_box.send_keys(dict.get("username"))
        pw_box.send_keys(dict.get("password"))
        login_button.click()

        pass

    def GotoClassInfoPage(self):
        self.driver.get("http://sugang.deu.ac.kr:8080/DEUsiganpyo.aspx")
        # menu_list = self.driver.find_element(by=By.CLASS_NAME, value="menulist")
        # look_up_info = menu_list.find_elements(by=By.TAG_NAME, value="li")[1]
        # look_up_info.click()

        pass

    def ScrapClassInfo(self):
        # tbody안에 tr(한 행) 안에 td(행 열)이 존재, 필요한 정보는 앞 5열
        
        # 강의 정보 테이블 잡아내기
        classInfoFrame = self.driver.find_element(by=By.ID, value="CP1_dt_result")
        classInfoTbody = classInfoFrame.find_element(by=By.TAG_NAME, value="tbody")
        # 강의 한 개의 태그(한 행)을 담은 리스트
        trTags = classInfoTbody.find_elements(by=By.TAG_NAME, value="tr")

        # csv파일을 여는 부분
        self.csvCtrl.OpenFile("./csv/test.csv","a")

        # tr을 한 줄씩 가져오고 write하기
        for trTag in trTags:
            # 강의 정보 앞에서 5개 가져오기 (교과목 번호, 분반, 교과목명, 담당교수, 강의실/교실)
            tdTags = trTag.find_elements(by=By.TAG_NAME, value='td')
            classInfoLine = [tdTags[0].text, tdTags[1].text, tdTags[2].text, tdTags[3].text, tdTags[4].text]
            self.csvCtrl.Write(classInfoLine)
        
        self.csvCtrl.CloseFile()

        pass

    def ScrapClassInfoAll(self):
        """
        (과목유형:공유대학) 을 선택하고 검색을 누른 후 다시 (과목유형:전체) 를 선택하자
        """
        # {과목유형 : 공유대학}으로 카테고리 바꾸기
        select_element = self.driver.find_element(By.ID, 'CP1_ddlSubjType')
        select = Select(select_element)
        select.select_by_visible_text('공유대학')
        
        # 검색 클릭
        searchBtn = self.driver.find_element(By.ID,"CP1_BtnSearch")
        searchBtn.click()

        # {과목유형 : 공유대학}으로 카테고리 바꾸기
        select_element = self.driver.find_element(By.ID, 'CP1_ddlSubjType')
        select = Select(select_element)
        select.select_by_visible_text('전체')

        print("stopPoint")

        # 일단 현재페이지의 정보 저장
        # lastPage = False
        # count = 1
        # while not lastPage:
        #     # 그 페이지에서 강의 정보 가져오기
        #     self.ScrapClassInfo()

        #     # 다음 페이지로 넘어가기  
        #     nextPage = self.driver.find_element(by=By.ID, value = "CP1_COM_Paging_Deu_lBtn_next")
        #     colorOfNextPage = nextPage.get_attribute("style")

        #     # 마지막이 아니면
        #     if colorOfNextPage != 'color: rgb(217, 217, 217);':
        #         print(f"{str(count).zfill(3)}페이지 : 저장 완료")
        #         count += 1
        #         nextPage.click()
        #     else:
        #         # 끝까지 잘 했다.
        #         lastPage = True
        #         print("========================\n모든 강의 정보를 저장했습니다.\n========================")

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