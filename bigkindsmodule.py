# 크롤링, 파싱
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 가독성을 위한 프린트
from pyrint import print_big

# 시간 조정
import time


# 함수 선언
def big_kinds_crawling(mode, page):
    url = 'https://www.bigkinds.or.kr/v2/news/recentNews.do'

    print_big("준비중...")

    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=url)

    # time.sleep(5)

    i = 1

    while i <= 100:
        time.sleep(0.2)
        print_big(driver.find_elements_by_xpath("//*[contains(text(), '전체')]"))
        i += 1

    '''
    print_big("크롤링을 시작합니다: " + driver.current_url)

    decode_text = driver.find_element_by_xpath('//img[1]')
    img_text = decode_text.get_attribute("alt")
    input_box = driver.find_element_by_name('ans')

    i = 0

    while i < 101:
        #

        decode_text = driver.find_element_by_xpath('//img[1]')
        img_text = decode_text.get_attribute("alt")
        input_box = driver.find_element_by_name('ans')

        input_box.send_keys(text_decoded)
        input_box.send_keys(Keys.RETURN)

        print(text_decoded)

        i += 1

    # 모두 정리
    driver.close()
    '''
