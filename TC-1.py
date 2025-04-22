from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import select
driver = Chrome()
#act = ActionChains(driver)

driver.get("http://www.facebook.com")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@name="email"]').send_keys("brajendra")
time.sleep(3)
# driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys("Brajendra")
# time.sleep(5)
# driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys("Singh")
# driver.find_element(By.XPATH,'//select[@id="day"]').send_keys("19")
# driver.find_element(By.XPATH,'//select[@name="birthday_month"]').send_keys("Oct")
# time.sleep(3)
# driver.find_element(By.XPATH,'//select[@id="year"]').send_keys("2020")
time.sleep(5)

driver.close()

