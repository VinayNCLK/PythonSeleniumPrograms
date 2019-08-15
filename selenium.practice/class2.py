
from selenium import webdriver
import os
import time
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


    def chrome_launch(self):
        driver = webdriver.Chrome(executable_path=self.chrome_api_location)
        driver.get("https://www.seleniumhq.org/download/")
        time.sleep(15)
        driver.close()

    def ff_launch(self):
        driver = webdriver.Firefox(executable_path=self.ff_api_location)
        driver.get("https://www.seleniumhq.org/download/")
        time.sleep(15)
        driver.close()

    def ie_launch(self):
        driver = webdriver.Ie(executable_path=self.ie_api_location)
        driver.get("https://www.seleniumhq.org/download/")
        time.sleep(15)
        driver.close()

def main():
    obj1 = browserName()
    #obj1.chrome_launch()
    #obj1.ff_launch()
    obj1.ie_launch()

if __name__ == '__main__':
    main()
