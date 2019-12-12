from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

lin = 'http://suninjuly.github.io/selects1.html'
brow = webdriver.Chrome()
brow.get(lin)
try:
    a1 = brow.find_element_by_xpath('//*[@id="num1"]')
    a1 = a1.text
    a2 = brow.find_element_by_xpath('//*[@id="num2"]')
    a2 = a2.text
    a11 = int(a1)
    a22 = int(a2)
    sum = int(a11) + int(a22)
    sum = str(sum)
    a4 = brow.find_element_by_xpath('//*[@id="dropdown"]').click()
    a5 = Select(brow.find_element_by_xpath('//*[@id="dropdown"]'))
    a5.select_by_visible_text(sum)
    b = brow.find_element_by_xpath('/html/body/div/form/button').click()
finally:
    time.sleep(5)
    brow.quit()
