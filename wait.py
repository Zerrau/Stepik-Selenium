from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

#browser.implicitly_wait(5)
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
a = browser.find_element_by_xpath('//*[@id="book"]').click()
a2 = browser.find_element_by_xpath('//*[@id="input_value"]')
a2 = a2.text
a2 = calc(a2)
a3 = browser.find_element_by_xpath('//*[@id="answer"]')
a3.send_keys(a2)
a4 = browser.find_element_by_xpath('//*[@id="solve"]').click()
