import argparse
from SugangScraper import *
import Config


def Parser():
    # 입력된 id, pw를 파싱하고 값을 리턴합니다.
    parser = argparse.ArgumentParser(description = "수강신청사이트 > 강의시간표 에 있는 수업계획서를 csv형태로 저장합니다.")
    parser.add_argument('-u', '--username', type=str,required=True, help="DAP 아이디를 입력해주세요")
    parser.add_argument('-p', '--password', type=str,required=True, help="DAP 비밀번호를 입력해주세요")
    args = parser.parse_args()

    return args

def main():
    # dict = Parser()
    dict = {"username":Config.ID,"password":Config.PW}  # 디버깅을 위한 코드
    print(dict)
    scraper = SugangScraper()
    scraper.Connect(dict)

    pass

if __name__ == "__main__":
    main()
    pass