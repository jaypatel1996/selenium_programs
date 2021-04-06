import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

expected_from_date_str = '01/20/2020'
expected_to_date_str = '02/26/2020'

expected_fr_date = '20'
expected_to_date = '26'

test_url = 'https://jqueryui.com/datepicker/#date-range'


def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()


def test_calendar_control_range_(self):
    driver = self.driver
    driver.get(test_url)
    time.sleep(5)

    frame = driver.find_element_by_xpath("//*[@id='content']/iframe")
    driver.switch_to.frame(frame)

    # Steps for the From Date
    from_dp = driver.find_element_by_xpath("//input[@id='from']")
    from_dp.click()
    time.sleep(5)

    from_month = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
    selected_from_month = Select(from_month)
    selected_from_month.select_by_visible_text("Jan")
    time.sleep(5)

    driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='20']")
    from_day = driver.find_element_by_xpath(
        "//td[not(contains(@class,'ui-datepicker-month'))]/a[text()='" + expected_fr_date + "']")
    from_day.click()
    time.sleep(10)

    to_dp = driver.find_element_by_xpath("//input[@id='to']")
    to_dp.click()
    time.sleep(5)

    to_month = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
    selected_to_month = Select(to_month)
    selected_to_month.select_by_visible_text("Feb")
    time.sleep(5)

    driver.find_element_by_xpath("//table/body/tr/td/a[text()='26']")
    to_day = driver.find_element_by_xpath(
        "//td[not(contains(@class,'ui-datepicker-month'))]/a[text()='" + expected_to_date + "']")
    to_day.click()
    time.sleep(10)

    selected_from_date_str = from_dp.get_attribute('value')
    self.assertEqual(selected_from_date_str, expected_from_date_str)

    selected_to_date_str = to_dp.get_attribute('value')
    self.assertEqual(selected_to_date_str, expected_to_date_str)
    print("Unit Test of jQuery Calendar passed")


def tearDown(self):
    self.driver.close()
    self.driver.quit()
