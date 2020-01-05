# Packages
import time

import selenium
from selenium import webdriver

import NameExtractor

app_names = []
element_web = []
k = 0
count = 1

def decompiler(path, file_path):
    global app_names, driver
    driver = webdriver.Chrome(path)
    driver.maximize_window()

    app_names = NameExtractor.name_extractor(file_path)
    for i in app_names:
        try:
            driver.refresh()
            driver.get("https://www.apkdecompilers.com/")
            time.sleep(5)

            # find element
            # extra code
            print(app_names)
            driver.get("https://www.apkdecompilers.com/")
            driver.find_element_by_id('apk')
            time.sleep(10)
            # send element
            element_send = driver.find_element_by_id("apk")
            element_send.send_keys(i)
            print(i)
            driver.find_element_by_id("submit-btn").click()
            time.sleep(270)
            # download element
            driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/a/b/u/h3").click()
            time.sleep(50)
        except:
            # find element
            # extra code
            driver.refresh()
            driver.get("http://www.javadecompilers.com/apk")
            # send element
            element_send = driver.find_element_by_id("upload_datafile")
            element_send.send_keys(i)
            print(i)
            send_element = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/button")
            webdriver.ActionChains(driver).move_to_element(send_element).click(send_element).perform()
            time.sleep(270)
            # download element
            down_element = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[1]/div[2]/a")
            webdriver.ActionChains(driver).move_to_element(down_element).click(down_element).perform()
            time.sleep(50)

    driver.close()

driver_path = "C:\Program Files (x86)\Python38-32\Chrome Driver\chromedriver.exe"
file_path = "D:\Project\Privacy Detection\Apps\App Data.xlsx"

decompiler(driver_path,file_path)