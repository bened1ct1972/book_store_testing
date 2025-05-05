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
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wpmenucart-contents"))).click() # go to cart
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout a"))).click() # proceed-to-checkout
data = {'billing_first_name':'Alex',
        'billing_last_name': 'Ivanov',
        #'billing_email': 'htjr@hfjd.com',
        'billing_phone': '9876543210',
        'billing_address_1': 'street 1 home 2',
        'billing_city': 'City-13',
        'billing_state': 'State-13',
        'billing_postcode': '123456',
}
for (key,value) in data.items():
    inp_element = wait.until(EC.element_to_be_clickable((By.ID, key)))
    inp_element.clear()
    inp_element.send_keys(value)

country_sel1 = wait.until(EC.element_to_be_clickable((By.ID, 's2id_billing_country'))).click()
country_inp1 = wait.until(EC.element_to_be_clickable((By.ID, 's2id_autogen1_search')))
country_inp1.send_keys('Rus')
wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='select2-results']/li[1]/div"))).click()  # select 1st element
driver.execute_script("window.scrollBy(0, 300)")
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#payment_method_cheque"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "place_order"))).click() # go to pay
time.sleep(3)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), 'Thank you. Your order has been received.'))
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//tr[th[contains(.,'Payment Method:')]]/td"), 'Check Payments'))

