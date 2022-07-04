import os
from selenium import webdriver
from pandas.io.html import read_html

import sys
import time
import random
import pandas as pd
import numpy as np

from chromewebdriver import generate_chrome

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

url = 'https://github.com/'
browser.get(url)
time.sleep(4)
# time.sleep(7 + random.randrange(1, 8))