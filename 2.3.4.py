from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


lin = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(lin)
    a1 = browser.find_element_by_xpath('/html/body/form/div/div/button').click()
    al = browser.switch_to.alert
    al.accept()
    a2 = browser.find_element_by_xpath('//*[@id="input_value"]')
    a2 = a2.text

    r = calc(a2)
    a3 = browser.find_element_by_xpath('//*[@id="answer"]')
    a3.send_keys(r)
    a4 = browser.find_element_by_xpath('/html/body/form/div/div/button').click()


finally:
    time.sleep(3)
    browser.quit()
