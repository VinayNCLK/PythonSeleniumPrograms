
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
        self.driver.get("file:///C:/Users/shekar/PycharmProjects/Selenium_July/htmlpages/page6.html")
        self.driver.maximize_window()
        #Single select drop down
        ele1 = self.driver.find_element(By.XPATH,
                                        "(//select[@name='Countries'])[1]")
        sel = Select(ele1)
        sel.select_by_index(1)
        time.sleep(2)
        sel.select_by_visible_text("China")
        time.sleep(2)
        sel.select_by_value("NZ")

        #Multi select drop down

        ele1 = self.driver.find_element(By.XPATH,
                                         "(//select[@name='Countries'])[2]")
        sel = Select(ele1)
        sel.select_by_index(1)
        time.sleep(2)
        sel.select_by_visible_text("China")
        time.sleep(2)
        sel.select_by_value("NZ")

        #deselcting the options in multi select drp dwn

        time.sleep(2)
        sel.deselect_by_index(1)
        time.sleep(2)
        sel.deselect_by_visible_text("China")
        time.sleep(2)
        sel.deselect_by_value("NZ")

        #Deselecting all options selected in multi select drp dwn
        sel.deselect_all()

        time.sleep(10)
        self.driver.close()

def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
