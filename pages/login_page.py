from selenium import webdriver as driver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import webdriverWait
from selenium.webdriver.support import expected_condition as EC

class LoginPage :
    def __init__(self):
        self.driver = driver
        self.wait = webdriverWait(driver,10)
    
    def login(self,username, password) :
        self.wait.until(EC.presence_of_element(By.XPATH,))