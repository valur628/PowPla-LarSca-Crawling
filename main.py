import os
from selenium import webdriver
from pandas.io.html import read_html
from selenium.webdriver.common.keys import Keys

import sys
import time
import random
import pandas as pd
import numpy as np

from chromewebdriver import generate_chrome
from userdata import siteID, sitePW

PROJECT_DIR = str(os.path.dirname(os.path.abspath(__file__)))
DOWNLOAD_DIR = f'{PROJECT_DIR}/download'
DATABASE_DIR = f'{PROJECT_DIR}/database'
driver_path = f'{PROJECT_DIR}/lib/webDriver/'

platform = sys.platform
if platform == 'linux':
    print('시스템 플랫폼: 리눅스')
    driver_path += 'chromedriver_Lin64'
elif platform == 'darwin':
    print('시스템 플랫폼: 맥')
    driver_path += 'chromedriver_Mac64'
elif platform == 'win32':
    print('시스템 플랫폼: 윈도우')
    driver_path += 'chromedriver_Win32'
else:
    print(f'[{sys.platform}] 시스템 플랫폼 확인 바람. 지원되지 않음.')
    raise Exception()
 
browser = generate_chrome(
    driver_path=driver_path,
    headless=False,
    download_path=DOWNLOAD_DIR)

url = 'https://pp.kepco.co.kr/intro.do'
browser.get(url) #url 주소로 접속
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="RSA_USER_ID"]') #아이디 입력
elm.send_keys(siteID) 
elm = browser.find_element("xpath", '//*[@id="RSA_USER_PWD"]') #비밀번호 입력
elm.send_keys(sitePW)
elm = browser.find_element("xpath", '//*[@id="intro_form"]/form/fieldset/input[1]').click() #로그인 버튼 클릭
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="smart2"]/a').click() #실시간사용량-시간대별 상단 버튼 누르기
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="txt"]/div[2]/div/p[1]/img').click() #날짜 선택 펼치기
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click() #년도 찾아 누르기
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="ui-datepicker-div"]/div/div/select[2]/option[6]').click() #월 찾아 누르기
time.sleep(5)

elm = browser.find_element("xpath", '//a[@class="ui-state-default" and text()="11"]').click() #날짜 찾아 누르기
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="txt"]/div[2]/div/p[2]/span[1]/a').click() #조회 버튼 누르기
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="txt"]/div[2]/div/p[1]/img').click() #날짜 선택 펼치기
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="ui-datepicker-div"]/div/a[2]/span').click() #다음 달 버튼 누르기
time.sleep(5)

elm = browser.find_element("xpath", '//a[@class="ui-state-default" and text()="5"]').click() #날짜 찾아 누르기
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="txt"]/div[2]/div/p[2]/span[1]/a').click() #조회 버튼 누르기
time.sleep(5)


time.sleep(10)
# time.sleep(7 + random.randrange(1, 8))