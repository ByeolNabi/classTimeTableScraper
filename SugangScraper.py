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
        print("=== 로그인 시작 ===")
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

        print("--- 로그인 완료 ---")

        pass

    def GotoClassInfoPage(self):
        print("=== 수업계획서조회 메뉴로 이동 ===")

        self.driver.get("http://sugang.deu.ac.kr:8080/DEUsiganpyo.aspx")
        
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

        # 강의 전체조회로 만들기 => 페이지 1클릭
        select.select_by_visible_text('전체')
        pageBtn = self.driver.find_element(By.ID,"CP1_COM_Page_Controllor1_spnPage1")
        pageBtn.click()

        print("--- 수업계획서조회 메뉴로 이동 완료 ---")

        pass

    def ScrapClassInfo(self):
        # thead.tr의 9번째까지가 필요한 속성이름
        # => (개설학과,이수구분,과목번호,분반,교과목명,학점/시간,수강,학년,강의실(시간),담당교수)
        # tbody.tr.td 9개 수집

        # csv파일 접근
        self.csvCtrl.OpenFile("./csv/test.csv","a")

        # 강의 정보 테이블 잡아내기
        classInfoFrame = self.driver.find_element(by=By.ID, value="CP1_grdView")
        # 데이터를 가지고 있는 tbody잡기
        classInfoTbody = classInfoFrame.find_element(by=By.TAG_NAME, value="tbody")
        # 강의 한 개의 태그(한 행)을 담은 리스트
        trTags = classInfoTbody.find_elements(by=By.TAG_NAME, value="tr")
        # tr을 한 줄씩 가져오고 write하기
        for trTag in trTags:
            # 강의 정보 앞에서 9개 가져오기
                # => (개설학과,이수구분,과목번호,분반,교과목명,학점/시간,수강,학년,강의실(시간),담당교수)
            tdTags = trTag.find_elements(by=By.TAG_NAME, value='td')
            self.csvCtrl.trWrite(tdTags, 9)
        
        self.csvCtrl.CloseFile()

        pass

    def ScrapClassInfoAll(self):
        # CP1_COM_Page_Controllor1_lbtnLast이 없어질때까지 다음 페이지 넘어가기
        # id="CP1_COM_Page_Controllor1_spnPage1" ~ "string"10까지 있음
        # 다음 10개 넘기는 버튼이 없어졌을 때, 리스트를 idx[2]부터 클릭하면 될 것 같다.

        # 파일 열기
        self.csvCtrl.OpenFile("./csv/test.csv","a")

        # 헤더 기록하기, 헤더 태그 잡기
        classInfoFrame = self.driver.find_element(by=By.ID, value="CP1_grdView")
        classInfoThead = classInfoFrame.find_element(by=By.TAG_NAME, value="thead")

        ## 헤더 기록하기
        # 헤더 정보를 가진 행에 접근
        trTag = classInfoThead.find_element(by=By.TAG_NAME, value="tr")
        thTags = trTag.find_elements(by=By.TAG_NAME, value='th')
        self.csvCtrl.trWrite(thTags, 9)

        # 다음으로 넘기며 각 페이지를 기록
        btn_id = "CP1_COM_Page_Controllor1_spnPage"
        dst = False
        while dst == False: # 마지막 페이지까지 반복
            for idx in range(1,11): # 1~10페이지 클릭하기
                page_btn = self.driver.find_elements(By.ID, btn_id+str(idx))
                if(len(page_btn) == 0): # idx페이지가 없다면 끝
                    dst = True
                    break
                else: # 있으면 이동 후 옮기기
                    page_btn[0].click();
                    self.ScrapClassInfo();
            
            print("stop point")
            nextpage_btn = self.driver.find_element(By.ID, "CP1_COM_Page_Controllor1_lbtnNext10")
            nextpage_btn.click()

            

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
        self.Login(dict)
        self.GotoClassInfoPage()
        self.ScrapClassInfoAll()
        self.driver.quit()
        pass