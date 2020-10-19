from selenium import webdriver

from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://poong.today")
assert "" in driver.title
elem = driver.find_element_by_class_name("chart-filter-searchbox-text")
print(elem)
elem.clear()
elem.send_keys("apple")
