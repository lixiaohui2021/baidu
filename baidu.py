from selenium import webdriver
import time
browser=webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("邓论")
browser.find_element_by_id("su").click()
time.sleep(10)
browser.quit()