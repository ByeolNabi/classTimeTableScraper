
# 사용법
Config.py파일을 만들어주세요.   
그 안에 ID와 PW를 기록해주세요.
```python
# 아래 형식을 이용해주세요.
ID = "20240000"
PW = "password"
```
## 교양 카테고리 정리
```
각 과목유형은 'O'에 해당하는 하위 카테고리를 선택해야함
```
|과목유형|개설학과|이수구분|학년|
|---|---|---|---|
|**교양**|-|O|-|
|**전공**|O|-|-|
|**교양부전공**|-|-|-|
|**교직**|-|-|-|
|**자유선택**|O|-|-|
|**공유대학**|-|-|-|


## 개선점<br>
- 파일을 중간에 저장하려고 했어서 파일을 닫았더니 datetime이 달라저서 다른 파일을 생성한다.
   - 그냥 파일 이름을 대충 짓자

- 몇 페이지를 저장하고 있는지 말해주자
   - print를 이용해서 구현

- csv파일에 기록하는 것은 모듈화하자
   - ClassInfoWriter.py로 분리

- csv파일에 자율교양인지 전공인지 말이 없는데...? 수강신청 시스템에서 스크래핑을 해야겠는걸...?




