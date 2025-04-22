from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

fbb=Chrome()
fbb.get("https://www.facebook.com/")
fbb.maximize_window()

#fb.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
fbb.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
fbb.find_element(By.XPATH,"//input[@name='firstname']").send_keys("braj")
fbb.find_element(By.XPATH,"//input[@name='lastname']").send_keys("singh")
fbb.find_element(By.XPATH,'//select[@name="birthday_day"]').send_keys("19")
time.sleep(5)
fbb.find_element(By.XPATH,'//input[@value="1"]').click()
fbb.get_screenshot_as_file("e:\\1200.png")
fbb.find_element(By.NAME,'//select[@title="Month"]').
fbb.find_element(By.XPATH,'//select[@title="Month"]').se
fbb.close()
