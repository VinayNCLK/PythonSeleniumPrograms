
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
        self.driver = webdriver.Chrome(executable_path=chrome_api_location)
        #self.driver = webdriver.Firefox(executable_path=ff_api_location)
        #self.driver = webdriver.Ie(executable_path=ie_api_location)

    def browser_launch(self):
        self.driver.get("https://www.seleniumhq.org/download/")
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        time.sleep(5)
        self.driver.back()
        time.sleep(5)
        self.driver.forward()
        time.sleep(5)
        self.driver.refresh()
        #self.driver.minimize_window()
        #self.driver.set_window_size(300,300)
        #self.driver.set_window_position(500, 500)
        #currenturl = self.driver.current_url
        #print(currenturl)
        #currenttitle = self.driver.title
        #print(currenttitle)
       # pagesource = self.driver.page_source
        #print(pagesource)



        time.sleep(10)
        self.driver.close()

def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
