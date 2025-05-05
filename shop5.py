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
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".main-nav:nth-child(1) a"))).click()  # Shop
# add book to stash
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-product_id='182']"))).click()  # add book in stash
time.sleep(1)
items_cnt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cartcontents")))
assert items_cnt.text == "1 Item"
items_sum = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#wpmenucartli .amount")))
assert items_sum.text == "₹180.00"
# go to cart
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wpmenucart-contents"))).click()
time.sleep(1)
subtotal = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@data-title='Subtotal']/span[@class='woocommerce-Price-amount amount']")))
assert subtotal != ''
total = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@data-title='Total']/strong/span[@class='woocommerce-Price-amount amount']")))
assert total != ''

