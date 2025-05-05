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
username = driver.find_element_by_id("username")
username.send_keys("bened1ct@yandex.ru")
passw = driver.find_element_by_id("password")
passw.send_keys("3o2i3j4Ss")
reg_btn = driver.find_element_by_xpath("//input[@type='submit' and @name='login']")
reg_btn.click()
logout_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout a")))

#time.sleep(5)
#driver.close()