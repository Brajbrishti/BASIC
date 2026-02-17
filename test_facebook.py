# import os
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# import time

# driver = Chrome()
# ### code starts from here ###
# driver.get("http://www.facebook.com")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element(By.XPATH,'//input[@name="email"]').send_keys("brajendra")
# time.sleep(3)
# driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

print("Starting Selenium Test...")

options = Options()
options.add_argument("--headless")  # REQUIRED for Jenkins
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# If chromedriver is in PATH, this is enough:
driver = Chrome(options=options)

driver.get("https://www.facebook.com")
# print("Page Title:", driver.title)

driver.find_element(By.NAME, "email").send_keys("brajendra")
print("Email entered successfully")

driver.quit()
print("Test Completed")


