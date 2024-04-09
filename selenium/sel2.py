#pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.service import Service
options = Options()
options.add_argument('--incognito')
options.add_argument('--start-maximized')
driver =webdriver.Chrome(options=options,executable_path=r'C:\Python37\Scripts\chromedriver.exe')
url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'

#Launch URL
driver.get(url)

#Retrieve Browser Details:
driver.get(url)
handles = driver.window_handles
print(handles)
current_handle = driver.current_window_handle
print(current_handle)
cur_url = driver.current_url
print(cur_url)
pageSource = driver.page_source
print(pageSource)
#Navigation
title = driver.title
driver.back()
driver.forward()
driver.refresh()


#Locating Elements

'''
By CLASS
<input class=”gLFyf” type=”text” />
'''
class_element = driver.find_element(By.CLASS_NAME, 'gLFyf')

'''
By Name
<input name=”z” type=”text” />
'''
name_element = driver.find_element(By.NAME, 'z')

'''
By Tag Name
<div id=”login” >…</div>
'''
tag_element= driver.find_element(By.TAG_NAME, 'div')

'''
By Link Text
<a href=”#”>News</a>
'''
linkText_element = driver.find_element(By.LINK_TEXT, 'News')

'''
By XPath
<form id=”login” action=”submit” method=”get”>
Username: <input type=”text” />
Password: <input type=”password” />
</form>
'''
xpath = "//form[@id='login']//input[@type='text']"
xpath_element = driver.find_element(By.XPATH , xpath)



'''
By CSS Selector
<form id=”login” action=”submit” method=”get”>
Username: <input type=”text” />
Password: <input type=”password” />
</form>
'''
css_element = driver.find_element(By.CSS_SELECTOR, '')
# # driver.maximize_window()
# driver.implicitly_wait(5)
# try:
#     element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,))

driver.quit()