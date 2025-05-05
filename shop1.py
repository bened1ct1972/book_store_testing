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
# login
driver.find_element_by_css_selector("#menu-item-50 a").click()
username = driver.find_element_by_id("username")
username.send_keys("bened1ct@yandex.ru")
passw = driver.find_element_by_id("password")
passw.send_keys("3o2i3j4Ss")
reg_btn = driver.find_element_by_xpath("//input[@type='submit' and @name='login']")
reg_btn.click()
# entering in Shop
WebDriverWait(driver,10).until(bottom_element)
shop_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-item-40 a")))
shop_link.click()
# entering in HTML5 book
html5_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@title='Mastering HTML5 Forms']")))
html5_link.click()
# check book title
html5_header = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".product_title.entry-title")))
assert html5_header.text == "HTML5 Forms"

driver.close()