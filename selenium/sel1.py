from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

url = "https://www.google.co.in"

driver.get(url)
driver.maximize_window()

driver.save_screenshot('ss.png')
element = driver.find_element(By.NAME,'q')

element.send_keys("Arrays")
time.sleep(3)
element.clear()
# element2 = driver.find_element(By.XPATH,"//body").click()
time.sleep(3)

driver.quit()