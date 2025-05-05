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
driver.execute_script("window.scrollBy(0, 300)")
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-product_id='182']"))).click()  # add HTML book in stash
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-product_id='180']"))).click()  # add ОЫ book in stash
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wpmenucart-contents"))).click() # go to cart
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart_item:nth-child(1) .remove"))).click() # remove 1st book
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce a"))).click() # undo

js_book_cnt = wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='cart_item' and td[contains(.,'JS Data Structures and Algorithm')]]/td[@class='product-quantity']/div/input")))
js_book_cnt.clear()
js_book_cnt.send_keys(3)
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='update_cart']"))).click() # update basket
js_book_cnt2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='cart_item' and td[contains(.,'JS Data Structures and Algorithm')]]/td[@class='product-quantity']/div/input")))
assert str(js_book_cnt2.get_attribute("value")) == str(3)
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='apply_coupon']"))).click() # update basket
time.sleep(2)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce li"), 'Please enter a coupon code.'))
