# PowPla-LarSca-Crawling
### _Powerplanner large data crawler_
>경상국립대학교 컴퓨터과학과 19학번
>박주철

# 개요
현장실습 업무 보조를 위해 제작한 파이썬 프로그램.
전력 사용량 분석을 위해 파워플래너 사이트 내부에 분산되어 있는 전력 관련 데이터를 모으고, 이 과정을 자동화할 필요가 있었기에 제작되었다.
단순히 데이터를 모을 뿐만 아니라, 모아진 데이터를 기반으로 합계, 평균, 수요전력도 추가로 계산 후 DataFrame에 저장한다.
저장된 데이터는 엑셀 파일(xlsx)의 형태로 만들어진다.
***
# 상세
### 개발 인원
 - 박주철
   - 개발 환경 구축
   - 프로그램 구상
   - 프로그램 제작
### 개발 기술
본 프로젝트 개발에 사용된 라이브러리 및 파이프라인입니다.
- [Python 3.10] - 동적 타이핑 범용 프로그래밍 언어
- [Pandas] - 대규모 데이터 조작 및 분석 라이브러리
- [Selenium] - 웹 애플리케이션 테스트를 위한 포터블 프레임워크
- [Openpyxl] - Office Open XML를 읽고 쓰기 위한 라이브러리

### 개발 환경
| 종류 | 목록 |
| ------ | ------ |
| 사용 언어 | Python(3.10) |
| 개발 도구 | Visual Studio Code(1.68.1), Chromium(103.0.5060.66) |
| 데이터베이스 | Microsoft Excel Open XML Spreadsheet |
| OS 환경 | Windows 10 |

### 사용 방법
본 프로젝트의 결과물을 시연하는 방법입니다.
- 시작 전 python 3.10, pip, pandas, selenium, openpyxl 다운로드 및 업그레이드 필수
- 다운로드한 다음, [userdata.py] 라는 이름으로 main.py와 같은 폴더에 py 파일 생성
- userdata.py 파일 내에 siteURL(사이트 주소), siteID(사이트 ID), sitePW(사이트 비밀번호) 변수를 문자열 형태로 추가
- [database] 라는 이름으로 main.py와 같은 폴더에 폴더 생성
- 명령어를 통해 main.py를 실행시키면 자동화된 전력 관련 데이터 수집을 시작

   [Python 3.10]: <https://www.python.org/downloads/release/python-3100/>
   [Numpy]: <https://github.com/numpy/numpy>
   [Pandas]: <https://github.com/pandas-dev/pandas>
   [Selenium]: <https://github.com/SeleniumHQ/selenium>
   [Openpyxl]: <https://foss.heptapod.net/openpyxl/openpyxl>
