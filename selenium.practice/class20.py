
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

#Launching the browser

class browserName:
    def __init__(self):
        print("Init method called")
        chrome_api_location = "C:\\Users\\shekar\\PycharmProjects" \
                              "\\Selenium_July\\browserapis\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chrome_api_location
        ff_api_location = "C:\\Users\\shekar\\PycharmProjects" \
                          "\\Selenium_July\\browserapis\\geckodriver.exe"
        os.environ["webdriver.gecko.driver"] = ff_api_location
        ie_api_location = "C:\\Users\\shekar\\PycharmProjects" \
                          "\\Selenium_July\\browserapis\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = ie_api_location
        self.driver = webdriver.Chrome(executable_path=chrome_api_location)
        #self.driver = webdriver.Firefox(executable_path=ff_api_location)
        #self.driver = webdriver.Ie(executable_path=ie_api_location)

    def browser_launch(self):
        self.driver.get("file:///C:/Users/shekar/PycharmProjects/Selenium_July/htmlpages/page8.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.driver.find_element(By.XPATH,"//button[text()='Click here']").click()
        time.sleep(5)
        alertcontent = self.driver.switch_to.alert.text
        print(alertcontent)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Click here']").click()
        time.sleep(5)
        self.driver.switch_to.alert.dismiss()
        time.sleep(5)
        self.driver.close()



def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
