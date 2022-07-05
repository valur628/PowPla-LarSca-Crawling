import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pandas.io.html import read_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import sys
import time
import random
import pandas as pd
import numpy as np
import base64
import csv
import math

from chromewebdriver import generate_chrome
from userdata import siteID, sitePW

import datetime
from datetime import timedelta
from dateutil import relativedelta


def getMonthRange(year, month):
    this_month = datetime.datetime(year=year, month=month, day=1).date()
    next_month = this_month + relativedelta.relativedelta(months=1)
    last_day = next_month - timedelta(days=1)
    return (last_day.day)


def splitTimes():
    elm = browser.find_element(
        "xpath", '//*[@id="SELECT_DT"]')  # 현재 년도와 월 그리고 일 함께 가져오기
    now_year_month = elm.get_attribute('value')  # elm에서 value만 빼내기
    # value를 - 기준으로 나누고 정수로 변환
    split_year_month = list(map(int, now_year_month.split('-')))
    return (split_year_month)


RANGEMONTH = 12  # 크롤링할 개월 수(끝나는 기간 아님)

PROJECT_DIR = str(os.path.dirname(os.path.abspath(__file__)))
DOWNLOAD_DIR = f'{PROJECT_DIR}/download'
DATABASE_DIR = f'{PROJECT_DIR}/database'
driver_path = f'{PROJECT_DIR}/lib/webDriver/'

electricity_time_columns_15 = [0]
current_time = datetime.datetime(2020, 1, 1)
for i in range(15, 24*60, 15):
    current_time = current_time + datetime.timedelta(minutes=15)
    electricity_time_columns_15.append(current_time.strftime('%H:%M'))
electricity_time_columns_15.append('24:00')
print(electricity_time_columns_15)

electricity_time_columns_60 = [0]
current_time = datetime.datetime(2020, 1, 1)
for i in range(0, 24*60-60, 60):
    current_time = current_time + datetime.timedelta(minutes=60)
    electricity_time_columns_60.append(current_time.strftime('%H'))
electricity_time_columns_60.append('24')
print(electricity_time_columns_60)

#electricity_df = pd.DataFrame(electricity_list, columns=electricity_time_columns_15)

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
browser.get(url)  # url 주소로 접속
time.sleep(5)

elm = browser.find_element("xpath", '//*[@id="RSA_USER_ID"]')  # 아이디 입력
elm.send_keys(siteID)
elm = browser.find_element("xpath", '//*[@id="RSA_USER_PWD"]')  # 비밀번호 입력
elm.send_keys(sitePW)
elm = browser.find_element(
    "xpath", '//*[@id="intro_form"]/form/fieldset/input[1]').click()  # 로그인 버튼 클릭
time.sleep(5)

elm = browser.find_element(
    "xpath", '//*[@id="smart2"]/a').click()  # 실시간사용량-시간대별 상단 버튼 누르기
time.sleep(7)

elm = browser.find_element(
    "xpath", '//*[@id="txt"]/div[2]/div/p[1]/img').click()  # 날짜 선택 펼치기

# elm = browser.find_element(
#     "xpath", '//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()  # 년도 찾아 누르기
elm = browser.find_element(
    "xpath", '//*[@id="ui-datepicker-div"]/div/div/select[2]/option[4]').click()  # 월 찾아 누르기
elm = browser.find_element(
    "xpath", '//a[@class="ui-state-default" and text()="16"]').click()  # 날짜 찾아 누르기
time.sleep(1)

split_year_month = splitTimes()
elm = browser.find_element(
    "xpath", '//*[@id="txt"]/div[2]/div/p[1]/img').click()  # 날짜 선택 펼치기

break_check = False

for i in range(1, RANGEMONTH):  # 탐색이 이루어지는 개월 범위
    number_day = getMonthRange(split_year_month[0], split_year_month[1])
    for j in range(1, number_day+1):  # 탐색이 이루어지는 요일 범위
        time.sleep(1)

        # pass_text = browser.find_element("xpath", '//td[@id="F_AP_QT"]').text
        # if pass_text == "0.00 kWh":
        #     break_check = True
        #     break

        elm = browser.find_element(
            "xpath", '//a[@class="ui-state-default" and text()="{0}"]'.format(str(j)))
        ActionChains(browser).move_to_element(elm).perform()
        elm = browser.find_element(
            "xpath", '//a[@class="ui-state-default ui-state-hover" and text()="{0}"]'.format(str(j))).click()  # 날짜 찾아서 집어넣기
        elm = browser.find_element(
            "xpath", '//*[@id="txt"]/div[2]/div/p[2]/span[1]/a').click()  # 조회 버튼 누르기
        time.sleep(4)
        # 표 제작 시작

        table_15 = browser.find_element(By.ID, 'tableListChart')  # 15분짜리 테이블 경로
        tbody_15 = table_15.find_element(By.TAG_NAME, "tbody")
        rows_15 = tbody_15.find_elements(By.TAG_NAME, "tr")
        print(splitTimes())
        for index, value in enumerate(rows_15):
            body = value.find_elements(By.TAG_NAME, "td")[0]
            print(body.text)
        for index, value in enumerate(rows_15):
            body = value.find_elements(By.TAG_NAME, "td")[7]
            print(body.text)
        # electricity_data = browser.find_element(
        #     "xpath", '//*[@id="txt"]/div[2]/div/p[2]/span[1]/a')
        # 표 제작 종료
        elm = browser.find_element(
            "xpath", '//*[@id="txt"]/div[2]/div/p[1]/img').click()  # 날짜 선택 펼치기
    elm = browser.find_element(
        "xpath", '//*[@id="ui-datepicker-div"]/div/a[2]/span').click()  # 다음 달 버튼 누르기
    elm = browser.find_element(
        "xpath", '//a[@class="ui-state-default" and text()="16"]').click()  # 날짜 찾아 누르기

    # if break_check == True:
    #     elm = browser.find_element(
    #         "xpath", '//*[@id="txt"]/div[2]/div/p[2]/span[1]/a').click()  # 조회 버튼 누르기
    #     time.sleep(4)
    #     break_check = False

    split_year_month = splitTimes()
    elm = browser.find_element(
        "xpath", '//*[@id="txt"]/div[2]/div/p[1]/img').click()  # 날짜 선택 펼치기
    time.sleep(1)

time.sleep(10)
# time.sleep(7 + random.randrange(1, 8))
