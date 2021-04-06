import time

from selenium import webdriver

driver = webdriver.Chrome("D:\\selenium\\Python\\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
driver.maximize_window()

# driver.find_element_by_xpath("//i[@class='glyphicon glyphicon-th']")
boot = driver.find_element_by_css_selector("div#sandbox-container1>div>span")
boot.click()
time.sleep(2)

month = driver.find_element_by_xpath("//th[@class='datepicker-switch']")
month.click()
time.sleep(2)

year = driver.find_element_by_xpath("(//th[@class='datepicker-switch'])[2]")
year.click()
time.sleep(2)

year1 = driver.find_element_by_xpath("//span[text()='2019']")
year1.click()

month1 = driver.find_element_by_xpath("//span[text()='Feb']")
month1.click()

date = driver.find_element_by_xpath("//td[text()='27']")
date.click()
