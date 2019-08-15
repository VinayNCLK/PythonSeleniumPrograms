
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
        self.driver.get("file:///C:/Users/shekar/PycharmProjects/Selenium_July/htmlpages/page2.html")
        self.driver.maximize_window()
        self.driver.find_element(By.NAME,"google").click()
        print("Identified element using name locator")
        time.sleep(5)
        self.driver.back()
        time.sleep(5)
        self.driver.find_element(By.ID,"googleid").click()
        print("Identified element using id locator")
        time.sleep(5)
        self.driver.back()
        time.sleep(5)
        self.driver.find_element(By.TAG_NAME, "a").click()
        print("Identified element using tag locator")
        time.sleep(5)
        self.driver.back()
        self.driver.get_screenshot_as_file()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "googlecls").click()
        print("Identified element using class name locator")
        time.sleep(5)
        self.driver.back()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Google").click()
        print("Identified element using Link text locator")
        time.sleep(5)
        self.driver.back()
        time.sleep(5)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Goo").click()
        print("Identified element using Partial Link text locator")
        time.sleep(5)
        self.driver.back()
        time.sleep(5)

        time.sleep(10)
        self.driver.close()

def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
