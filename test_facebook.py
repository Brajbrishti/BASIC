import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
### code starts from here ###
driver.get("http://www.facebook.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,'//input[@name="email"]').send_keys("brajendra")
time.sleep(3)
driver.close()


