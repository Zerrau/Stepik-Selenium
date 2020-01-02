import time
import unittest
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link1)
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input').send_keys('Иван')
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input').send_keys('Иванов')
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input').send_keys('ivan@iv.com')
        browser.find_element_by_xpath('/html/body/div/form/button').click()
        time.sleep(1)

        welcome_text_elt = browser.find_element_by_xpath('/html/body/div/h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')

    def test_abs2(self):
        link2 = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link2)
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input').send_keys('Иван')
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input').send_keys('Иванов')
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input').send_keys('ivan@iv.com')
        browser.find_element_by_xpath('/html/body/div/form/button').click()
        time.sleep(1)

        welcome_text_elt = browser.find_element_by_xpath('/html/body/div/h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text, 'Congratulations! You have successfully registered!')


if __name__ == "__main__":
    unittest.main()
