
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
        self.driver.get("file:///C:/Users/shekar/PycharmProjects/Selenium_July/htmlpages/page4.html")
        self.driver.maximize_window()
        #Xpath by Dependent and independent element
        '''
        maths = self.driver.find_element(By.
                XPATH,"//td[contains(text(),'Maths')]/../td[3]").text

        print("Marks scored in maths "+maths)

        physics = self.driver.find_element(By.
                XPATH, "//td[contains(text(),'Pysics')]/../td[3]").text

        print("Marks scored in physics " + physics)
        '''
        '''
        maths = self.driver.find_element(By.
                XPATH, "//tr[//td[text()='Maths']]/td[3]").text

        print("Marks scored in maths " + maths)

        physics = self.driver.find_element(By.
               XPATH, "//tr[//td[text()='Pysics']]/td[3]").text

        print("Marks scored in physics " + physics)
        '''

        maths = self.driver.find_element(By.
                 XPATH, "//td[text()='Maths']/following-sibling::td").text

        print("Marks scored in maths " + maths)

        physics = self.driver.find_element(By.
                XPATH, "//td[text()='Pysics']/following-sibling::td").text

        print("Marks scored in physics " + physics)

        time.sleep(10)
        self.driver.close()

def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
