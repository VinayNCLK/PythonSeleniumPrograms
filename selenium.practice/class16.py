
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
        self.driver.get("https://www.myntra.com/?gclid=EAIaIQobChMI3cjr4-Tl4wIV2YBwCh1WrwtcEAAYASAAEgLHmPD_BwE&utm_source=google&utm_medium=cpc&utm_campaign=&utm_term=myntra&utm_content=&matchtype=e")
        self.driver.maximize_window()
        action = ActionChains(self.driver)
        ele1 = self.driver.find_element(By.XPATH,"//a[text()='Men']")
        action.move_to_element(ele1).perform()
        time.sleep(5)
        ele2 = self.driver.find_element(By.XPATH,"//a[text()='Formal Shirts']")
        action.move_to_element(ele2).click().perform()
        self.driver.execute_script("window.scrollBy(0,10000);")
        time.sleep(10)
        self.driver.close()

def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
