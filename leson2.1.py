from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"


def calcl(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    brow = webdriver.Chrome()
    brow.get(link)

    a1 = brow.find_element_by_xpath('//*[@id="input_value"]')
    a1 = a1.text
    r = calcl(a1)
    a2 = brow.find_element_by_xpath('//*[@id="answer"]')
    a2.send_keys(r)
    a3 = brow.find_element_by_xpath('//*[@id="robotCheckbox"]')
    a3.click()
    a4 = brow.find_element_by_xpath('//*[@id="robotsRule"]')
    a4.click()
    a5 = brow.find_element_by_xpath('/html/body/div/form/button')
    a5.click()
finally:
    time.sleep(5)
    brow.quit()
