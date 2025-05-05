import time
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
bottom_element = EC.presence_of_element_located((By.ID,"mc4wp-form-1"))
wait = WebDriverWait(driver, 10)
wait.until(bottom_element)
# login
driver.find_element_by_css_selector("#menu-item-50 a").click()
username = driver.find_element_by_id("username")
username.send_keys("bened1ct@yandex.ru")
passw = driver.find_element_by_id("password")
passw.send_keys("3o2i3j4Ss")
reg_btn = driver.find_element_by_xpath("//input[@type='submit' and @name='login']")
reg_btn.click()
# entering in Shop
wait.until(bottom_element)   # wait bottom of page
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-item-40 a"))).click()
# entering andriod book
wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@title='Android Quick Start Guide']"))).click()
# check prices
del_price = driver.find_element_by_xpath("//del/span[@class='woocommerce-Price-amount amount']")
assert del_price.text == "₹600.00"
ins_price = driver.find_element_by_css_selector('.price > ins > span')
assert ins_price.text == "₹450.00"
wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@title='Android Quick Start Guide']"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#fullResImage")))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))).click()

