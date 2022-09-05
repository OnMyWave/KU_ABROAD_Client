## Import Librarys 
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os


## Chrome Settings
chrome_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'chromedriver')
options = webdriver.ChromeOptions() 
# Download path 설정
prefs = {"download.default_directory" : "/Users/onmywave/Desktop/download"}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=options, executable_path=chrome_path)

# 고려대학교 국제처 사이트
driver.get('https://studyabroad.korea.ac.kr/studyabroad/report02.do?mode=list&&articleLimit=10&article.offset=0')

# 로그인 대기
if input() == 'a':
    while True:
        # articleLimit i 설정 및 반복
        for i in range(10):
            # article Click
            WebDriverWait(driver,10).until(element_to_be_clickable((By.XPATH,'//*[@id="jwxe_main_content"]/div/div/div/div[2]/ul/li['+str(2+i)+']/a'))).click()
            # except : no download file 
            try: 
                WebDriverWait(driver,10).until(element_to_be_clickable((By.XPATH,'//*[@id="jwxe_main_content"]/div/div/div/table/tbody/tr[3]/td/a'))).click()
            except:
                pass
            # 뒤로 가기
            driver.back()
        # 다음 페이지 
        WebDriverWait(driver,10).until(element_to_be_clickable((By.XPATH,"//img[@alt='다음']"))).click()