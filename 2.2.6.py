from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    a = browser.find_element_by_xpath('//*[@id="input_value"]')
    a = a.text
    a = int(a)
    r = calc(a)
    browser.execute_script("window.scrollBy(0, 100);")
    a2 = browser.find_element_by_xpath('//*[@id="answer"]')
    a2.send_keys(r)
    a3 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
    a4 = browser.find_element_by_xpath('//*[@id="robotsRule"]').click()
    a5 = browser.find_element_by_xpath('/html/body/div/form/button').click()
finally:
    time.sleep(5)
    browser.quit()
