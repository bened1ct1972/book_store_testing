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

driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_partial_link_text('Selenium Ruby').click()
WebDriverWait(driver,10).until(bottom_element)
driver.find_element_by_css_selector(".reviews_tab > a").click()
driver.find_element_by_css_selector(".star-5").click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
author_name = driver.find_element_by_id("author")
author_name.send_keys("Bened1ct")
author_email = driver.find_element_by_id("email")
author_email.send_keys("bened1ct@domain.com")
driver.find_element_by_id("submit").click()
# time.sleep(3)
driver.close()