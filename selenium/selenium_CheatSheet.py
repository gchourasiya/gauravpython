from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#FIND ELEMENT
element = driver.find_element(By.ID,'ID')
element = driver.find_element(By.NAME,'NAME')
element = driver.find_element(By.TAG_NAME,'TAG')
element = driver.find_element(By.LINK_TEXT,'TEXT')
element = driver.find_element(By.PARTIAL_LINK_TEXT,'TEXT')
element = driver.find_element(By.CSS_SELECTOR,'CSS')


#SELECT DROP DOWN LIST
select = Select(driver.find_element(By.ID,'ID'))
select.select_by_visible_text('text')
select.select_by_index('index')
select.select_by_value('value')

