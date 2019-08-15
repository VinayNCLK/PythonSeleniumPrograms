
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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
        self.driver.get("https://demo.actitime.com/login.do")
        self.driver.maximize_window()

        parentwindowid = self.driver.current_window_handle
        print(parentwindowid)

        self.driver.find_element(By.XPATH,"//a[text()='actiTIME Inc.']").click()

        listofwindowids = self.driver.window_handles
        for i in listofwindowids:
            if i is not parentwindowid:
                self.driver.switch_to.window(i)

        print(self.driver.current_url)
        time.sleep(10)
        self.driver.switch_to.window(parentwindowid)
        print(self.driver.current_url)
        time.sleep(10)
        self.driver.quit()

def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
