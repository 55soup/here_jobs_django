## google로그인하고, 페이지 스크래핑

# 1. 기업명 enterprise
# 2. 사업자등록번호 enterprise_num
# 3. 업종 sector
# 4. 사원수(명) employee
# 매출규모(억) sales
# 주소(도로명 주소) address
# 웨ㅐㅂ사이트 주소 weblink
# 기업소개 및 기업규모 introduce
# 담당업무 work
# 지원요건 req_apply
# 채용인원 recruitment
# 제출서류 submit
# 13. 서류제출 마감일 submit_deadline
# 14. 기타 사항들... etc1
# 15.etc2
# 16.etc3
# selenium을 이용하여 구글자동로그인, 스크래핑
from unittest.mock import sentinel
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from csv_save import save_to_file

def parse_jobs():
    options = webdriver.ChromeOptions()

    # 크롭 웹 드라이버의 경로를 설정
    # driver = webdriver.Chrome("chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(-10000, 0)  # chrome 창 안보이게
    url = "https://classroom.google.com/u/0/c/NDc0MzAyMDQ3MzM0"

    # 구글 로그인에 접속
    driver.get(url)
    # driver.maximize_window()
    # id입력
    driver.find_element(By.ID, "identifierId").send_keys("w2118@e-mirim.hs.kr")
    sleep(3)

    driver.find_element(By.ID, "identifierNext").click()
    driver.find_element(By.ID, "identifierNext").is_displayed
    sleep(5)
    # 비밀번호 입력

    driver.find_element(By.CSS_SELECTOR, ".whsOnd").send_keys("may279**2")
    sleep(2)
    driver.find_element(By.ID, "passwordNext").click()  # 간혹 오류 발생 => 다시실행하면 됨.
    sleep(10)

    # 무한 스크롤
    ############################################

    elem = driver.find_element(By.TAG_NAME, "body")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        scroll_down = 0
        while scroll_down < 10:
            elem.send_keys(Keys.PAGE_DOWN)
            sleep(0.2)
            scroll_down += 1

        new_height = driver.execute_script("return document.body.scrollHeight")  # 화면에 끝까지 내리기
        if new_height == last_height:
            # print("********" + lecture['category'] + ' / ' + lecture['subCategory']  + " break********")
            break

        last_height = new_height

    #############################################
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    # contents = soup.find_all('html-blob')

    # #html태그 다 지우기
    # print(str_content)
    # str_content = str(contents).replace("<br/>", "\n").replace("<html-blob>", "").replace("<span>", "").replace("</html-blob>", "").replace("</span>","")
    # print(len(str_content))
    # # 다른 모든 페이지 스크래핑 하기

    # titles = soup.select('html-blob')
    # titles = soup.find('html-blob').find_all(text=True)
    titles = soup.find_all('html-blob')
    title = ''
    jobs_csv = []
    for i in titles:
        # 정보정제
        title = str(i).replace("<br/>", "\n").replace("<html-blob>", "").replace("<span>", "").replace("</html-blob>",
                                                                                                       "").replace(
            "</span>", "")  # 태그제거
        title2 = title.replace("파일이름: ", "").replace("(주)Nomad 개발분야 지원자 3100김맑음_이력서, 자기소개서", "\n").replace(
            "(주)Nomad 개발분야 지원자 3300김개인_포트폴리오", "").replace("* 파일이름 지켜주세요", "")
        title3 = title2.replace("<b>", "").replace("</b>", "").replace(":", "")  # 태그제거
        title4 = title3.replace("\n", "").replace("기업명(사업자등록증명)", "").replace("사업자등록번호", "").replace("업종", "").replace(
            "사원수(명)", "").replace("매출규모(억)", "").replace("주소(도로명 주소)", "").replace("웹사이트 주소", "").replace("기업소개 및 기업규모",
                                                                                                          "").replace(
            "담당업무", "").replace("지원요건", "").replace("채용인원", "").replace("제출서류", "").replace("제출서류 마감일", "").replace(
            "서류제출 마감일", "")

        # list에 넣기
        # list2 = list(filter(None, re.split(r'\d+.', title4)))
        # print(list2)
        words = '!!!'
        for i in range(1, 17):
            title4 = title4.replace(f'{i}. ', words).replace(u'\xa0', u' ')  # 숫자. 을 기준으로 나누기
        answer = title4.split(words)
        key_list=["enterprise", "enterprise_num", "sector", "employee", "sales", "address", "weblink", "introduce", "work", "req_apply", "recruitment", "submit", "submit_deadline", "etc1", "etc2", "etc3"]
        dictionary = dict(zip(key_list, answer[1:])) # db에 넣기 위해 dict으로 변환
        print(dictionary)
        # return answer[1:]

        # jobs_csv.append(answer[1:17])  # 17열까지로 제한 -> db에 저장하기 좋게
        # # 정보 csv파일에 저장.
        # save_to_file(jobs_csv)

    driver.quit()  # 종료

parse_jobs()