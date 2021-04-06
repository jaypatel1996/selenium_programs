from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("D:\\selenium\\Python\\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
driver.maximize_window()

click = Select(driver.find_element_by_id('select-demo'))
click.select_by_value('Sunday')

click1 = Select(driver.find_element_by_id('multi-select'))

click1.select_by_value('California')
click1.select_by_value('Florida')
click1.select_by_value('New Jersey')
click1.select_by_value('New York')
click1.select_by_value('Ohio')
click1.select_by_value('Texas')
click1.select_by_value('Pennsylvania')
click1.select_by_value('Washington')
click1.deselect_all()
# driver.find_element_by_id("printMe").click()
# driver.find_element_by_id("printAll").click()
