# 크롤링, 파싱
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import *  # BeautifulSoup

# 가독성을 위한 프린트
from selenium.webdriver.support.wait import WebDriverWait

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
    # term_all_button = driver.find_elements_by_xpath("//span[@class='radio-btn date-radio-btn']/input[@id='date1-1']")[0]
    # driver.execute_script("arguments[0].click();", term_all_button)
    input_box.send_keys("삼성전자")
    input_box.send_keys(Keys.RETURN)

    driver.implicitly_wait(time_to_wait=1)
    driver.find_elements_by_xpath("//span[@class='title-elipsis']")[0].click()
    # driver.find_elements_by_xpath("//a[@class='page-next page-link']")[0].click()

    # time.sleep(0.1)
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="news-detail-modal"]/div/div/div[1]')))

    html = driver.page_source  # 페이지 긁어오기

    soup = BeautifulSoup(html, 'html.parser')
    temp_text_head = soup.select('.news-view-head')[0].get_text()
    temp_text_body = soup.select('.news-view-body')[0].get_text()

    print(temp_text_body)

    close_button = driver.find_elements_by_xpath('//*[@id="news-detail-modal"]/div/div/button')[0]
    close_button.click()

    time.sleep(1000)
