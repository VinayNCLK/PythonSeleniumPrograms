
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
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
        self.driver.get("file:///C:/Users/shekar/PycharmProjects/Selenium_July/htmlpages/page5.html")
        self.driver.maximize_window()
        #Xpath by group index

        self.driver.find_element(By.
                XPATH,"(//input[@type='checkbox'])[last() - 1]").click()

        time.sleep(10)
        self.driver.close()

def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
