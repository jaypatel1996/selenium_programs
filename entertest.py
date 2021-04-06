import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('D:\\selenium\\Python\\chromedriver.exe')
driver.get("https://www.python.org")
driver.maximize_window()
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
Donate = driver.find_element_by_class_name("donate-button")
Donate.click()
print("the test pass at the end!!")
print(driver.current_url)