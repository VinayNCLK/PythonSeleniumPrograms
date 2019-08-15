
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
        #find elements

        noOfTables = self.driver.find_elements(By.XPATH,"//table")
        print("NUmber of tables present in the web page is = "+str(len(noOfTables)))

        noOfColumnsInTables = self.driver.find_elements(By.XPATH,
                                                        "(//table)[1]//th")
        print("NUmber of Columns in table present in the web page is = "
              + str(len(noOfColumnsInTables)))

        noOfRowsInTables = self.driver.find_elements(By.XPATH,
                                                     "(//table)[1]//tr")
        print("NUmber of rows in table present in the web page is = "
              + str(len(noOfRowsInTables)))

        noOfCellsInTables = self.driver.find_elements(By.XPATH,
                                            "(//table)[1]//td|(//table)[1]//th")
        print("NUmber of cells in table present in the web page is = "
              + str(len(noOfCellsInTables)))
        #Below loop is to print content in the table
        for x in noOfCellsInTables:
            print(x.text)

        noOflinks = self.driver.find_elements(By.XPATH, "//a")
        print("NUmber of links present in the web page is = " + str(len(noOflinks)))
        #print(noOflinks[1].text)
        for x in noOflinks:
            print(x.text)

        time.sleep(10)
        self.driver.close()

def main():
    obj1 = browserName()
    obj1.browser_launch()

if __name__ == '__main__':
    main()
