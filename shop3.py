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
#check Default sorting
sort_selected_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@name='orderby']/option[@selected='selected']")))
assert sort_selected_option.text == 'Default sorting'
# set new sort order
sort_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@name='orderby']")))
sort_selector = Select(sort_element)
sort_selector.select_by_value('price-desc')
WebDriverWait(driver,10).until(bottom_element)
# check new sort order
sort_selected_option2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@name='orderby']/option[@selected='selected']")))
assert sort_selected_option2.text == 'Sort by price: high to low'
