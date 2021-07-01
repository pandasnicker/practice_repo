from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Python38\Lib\site-packages\selenium\driver\chromedriver_83.exe")
driver.get("http://www.google.com")

assert "Google" in driver.title, "Oops"

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Selenium Tutorial")
elem.send_keys(Keys.RETURN)
assert "No result found" not in driver.page_source

time.sleep(3)

driver.close()
