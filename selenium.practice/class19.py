
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
        self.driver.get("https://demo.actitime.com/login.do")
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("admin")
        self.driver.find_element(By.XPATH, "//input[@name='pwd']").send_keys("manager")

        ele1 = self.driver.find_element(By.XPATH, "//div[contains(text(),'Login')]")
        wait = WebDriverWait(self.driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException])
        wait.until(EC.element_to_be_clickable(ele1))
        ele1.click()
        time.sleep(10)

        self.driver.find_element(By.XPATH,"//div[@onclick='openHelpAndSupportMenu(event)']").click()
        parentwindowid = self.driver.current_window_handle
        print(parentwindowid)
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//a[text()='Frequently Asked Questions']").click()
        listofwindowids = self.driver.window_handles
        for i in listofwindowids:
            if i is not parentwindowid:
                self.driver.switch_to.window(i)
        print(self.driver.current_url)
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(parentwindowid)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]")
        self.driver.close()

def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
