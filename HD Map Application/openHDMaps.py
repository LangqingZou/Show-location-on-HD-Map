import getLocation
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def showLocation():

    '''
    Get the location
    '''
    location = getLocation.extractLatLon(getLocation.getLocation())


    '''
    Login page
    '''
    # openHDMaps credentials
    username = "zoulangqingskye@gmail.com"
    password = "TWhtmmpBChcn6UP"

    # initialize the Chrome driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # head to login page
    driver.get("https://platform.ecopiatech.com")
    # find username/email field and send the username itself to the input field
    driver.find_element(By.ID, "email").send_keys(username)
    # find password input field and insert password as well
    driver.find_element(By.ID, "password").send_keys(password)
    # click login button
    driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div/div/div[2]/div[2]/button[1]/span").click()


    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=20).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Incorrect username or password."
    # get the errors (if there are)
    errors = driver.find_elements(By.CLASS_NAME, "flash-error")
    # print the errors optionally
    # for e in errors:
    #     print(e.text)
    # if we find that error message within errors, then login is failed
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
    else:
        print("[+] Login successful")



    '''
    Map browser
    '''
    driver.get("https://platform.ecopiatech.com/map_browser/index")
    driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div[1]/ul/li[2]/span[2]").click()


    '''
    Show search box and input the location
    '''
    driver.find_element(By.XPATH, "//*[@id='lm-container']/div[2]/div/div/div[2]/span[1]/button").click()
    driver.find_element(By.XPATH, "//*[@id='lm-container']/div[2]/div/div/div[4]/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/input").send_keys(location)
    driver.find_element(By.XPATH, "//*[@id='lm-container']/div[2]/div/div/div[4]/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/button[2]").click()

    input()

    # close the driver
    # driver.close()

if __name__ == "__main__":
    showLocation()