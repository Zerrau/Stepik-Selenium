from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


lin = "http://suninjuly.github.io/redirect_accept.html"
try:
    brow = webdriver.Chrome()
    brow.get(lin)
    a = brow.find_element_by_xpath('/html/body/form/div/div/button').click()
    win2 = brow.window_handles[1]
    brow.switch_to.window(win2)
    a2 = brow.find_element_by_xpath('//*[@id="input_value"]')
    a2 = a2.text
    a2 = calc(a2)
    a3 = brow.find_element_by_xpath('//*[@id="answer"]')
    a3.send_keys(a2)
    a4 = brow.find_element_by_xpath('/html/body/form/div/div/button').click()



finally:
    time.sleep(5)
    brow.quit()
