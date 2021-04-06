from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\selenium\\Python\\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.tutorialspoint.com/index.htm")

driver.refresh()

driver.close()