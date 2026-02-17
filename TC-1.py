from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import select
driver = googlechrome()
### code starts from here ###
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@name="email"]').send_keys("brajendra")
time.sleep(3)
driver.close()


