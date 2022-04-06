from pydoc import describe
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


'''
Returns the information window from "https://www.itilog.com/en/where-am-i" where used to locate the laptop

'''
def getLocation():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--use-fake-ui-for-media-stream")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.itilog.com/en/where-am-i")
    time.sleep(10)

    info = driver.find_element(By.ID, 'info_window').get_attribute('innerHTML')
    print(type(info))
    driver.quit()
    return info


'''
Returns the index of the nth occurrences of symbol in string
@parm: myString 
@parm: symbol
@parm: n the time of occurrences
'''
def find_nth(myString, symbol, n):
    start = myString.find(symbol)
    while start >= 0 and n > 1:
        start = myString.find(symbol, start+len(symbol))
        n -= 1
    return start



'''
Extract the latitude and longitude from the string
@parm: myString 
@return: The latitude and longitude
'''
def extractLatLon(myString):
    # Latitude:
    start1 = find_nth(myString, "</strong>", 1)
    end1 = find_nth(myString, "|", 1)
    lat = myString[start1+9:end1]
    lat = lat.strip()

    # Longitude:
    start2 = find_nth(myString, "</strong>", 2)
    end2 = find_nth(myString, "<br>", 2)
    lon = myString[start2+9:end2]
    lon = lon.strip()
    return lat+","+lon


# if __name__ == "__main__":
#     info = getLocation()
    
#     print(getLocation())



