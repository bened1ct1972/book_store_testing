import time
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
bottom_element = EC.presence_of_element_located((By.ID,"mc4wp-form-1"))
WebDriverWait(driver,10).until(bottom_element)

driver.find_element_by_css_selector("#menu-item-50 a").click()
email = driver.find_element_by_id("reg_email")
email.send_keys("bened1ct@yandex.ru")
passw = driver.find_element_by_id("reg_password")
passw.send_keys("3o2i3j4Ss1")
reg_btn = driver.find_element_by_xpath("//input[@type='submit' and @value='Register']")
reg_btn.click()

#time.sleep(5)
#driver.close()