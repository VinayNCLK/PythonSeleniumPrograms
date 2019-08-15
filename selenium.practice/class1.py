
from selenium import webdriver
import os
import time
#Launching the browser

class browserName:
    def __init__(self):
        print("Init method called")

    def chrome_launch(self):
        chrome_api_location = "C:\\Users\\shekar\\PycharmProjects" \
                              "\\Selenium_July\\browserapis\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chrome_api_location
        driver = webdriver.Chrome(executable_path=chrome_api_location)
        driver.get("https://www.seleniumhq.org/download/")
        time.sleep(15)
        driver.close()

    def ff_launch(self):
        ff_api_location = "C:\\Users\\shekar\\PycharmProjects" \
                          "\\Selenium_July\\browserapis\\geckodriver.exe"
        os.environ["webdriver.gecko.driver"] = ff_api_location
        driver = webdriver.Firefox(executable_path=ff_api_location)
        driver.get("https://www.seleniumhq.org/download/")
        time.sleep(15)
        driver.close()

    def ie_launch(self):
        ie_api_location = "C:\\Users\\shekar\\PycharmProjects" \
                          "\\Selenium_July\\browserapis\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = ie_api_location
        driver = webdriver.Ie(executable_path=ie_api_location)
        driver.get("https://www.seleniumhq.org/download/")
        time.sleep(15)
        driver.close()

def main():
    obj1 = browserName()
    obj1.ie_launch()

if __name__ == '__main__':
    main()
