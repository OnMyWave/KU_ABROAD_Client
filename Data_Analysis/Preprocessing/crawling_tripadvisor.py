## Import Librarys 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By
import os
import pandas as pd
import time
## Chrome Settings
options = webdriver.ChromeOptions() 
# Download path 설정
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

df = pd.read_excel(os.path.dirname(__file__) +'/univ_data.xlsx')
trip_links = df['Unnamed: 35'][1:]

obj = {}
cnt = 0

def get_attribute(driver,html):
    if 'Tourism' in html : 
        html = html.replace('Tourism', 'Attractions')
    driver.get(html)
    time.sleep(2)
    attr = {}
    for i in range(1,4):
        for j in range(1,9):
            try:
                title = driver.find_element(By.XPATH,'//*[@id="lithium-root"]/main/span/div/div[3]/div/div[2]/div[2]/span/div/div[2]/section['+str(j)+']/div/div/span/div/div[2]/div/span['+str(i)+']/div/article/div[2]/header/div/div/a[1]/h3/div/span/div')
                image = driver.find_element(By.XPATH,'//*[@id="lithium-root"]/main/span/div/div[3]/div/div[2]/div[2]/span/div/div[2]/section['+str(j)+']/div/div/span/div/div[2]/div/span['+str(i)+']/div/article/div[1]/div/div/div/div[1]/a/div/div/div/div[1]/ul/li[1]/picture/img')
                attr['title'+str(i)] = title.text
                attr['image'+str(i)] = image.get_attribute('src')
                break
            except:
                pass
            
    return attr

for row in trip_links:
    obj = get_attribute(driver,row)
    print(obj)
    print()

    if obj != {}:
        df.loc[cnt+2,'여행'] =  obj['title1'] # title1
        df.loc[cnt+2,'Unnamed: 30'] =  obj['image1'] # image1
        df.loc[cnt+2,'Unnamed: 31'] =  obj['title2'] # title2
        df.loc[cnt+2,'Unnamed: 32'] =  obj['image2'] # image2
        df.loc[cnt+2,'Unnamed: 33'] =  obj['title3'] # title3
        df.loc[cnt+2,'Unnamed: 34'] =  obj['image3'] # image3
    cnt += 1


df.to_excel('univ_data3.xlsx')