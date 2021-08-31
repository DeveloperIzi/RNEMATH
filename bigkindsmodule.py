# 크롤링, 파싱
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import *  # BeautifulSoup

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

    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')

    information_list = soup.select("#news-results")
    for information in information_list:
        print(information.text)

    '''
    print_big("크롤링을 시작합니다: " + driver.current_url)

    decode_text = driver.find_element_by_xpath('//img[1]')
    img_text = decode_text.get_attribute("alt")
    input_box = driver.find_element_by_name('ans')

    i = 0

    while i < 101:
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


def big_kinds_samsung(mode, page):
    url = 'https://www.bigkinds.or.kr/v2/news/index.do'

    print_big("삼성 전용 뉴스 검색 준비중...")

    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=url)

    input_box = driver.find_element_by_id('total-search-key')

    term_button = driver.find_element_by_link_text('기간').click()

    term_all_button = driver.find_elements_by_xpath("//span[@class='radio-btn date-radio-btn']/input[@id='date1-1']")

    print(term_all_button)

    # term_button = driver.find_elements_by_xpath("//a[text()='기간']")

    time.sleep(5)

    input_box.send_keys("삼성전자")
    # input_box.send_keys(Keys.RETURN)

    time.sleep(1000)