from selenium import webdriver
import time
import unittest
import math

answer = math.log(int(time.time()))
link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
browser.implicitly_wait(5)


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        try:
            browser.get(link)
            browser.find_element_by_xpath(
                '/html/body/div/div/div[2]/main/div/div[3]/div[3]/div[1]/div/article/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/textarea').send_keys(
                answer)
            browser.find_element_by_xpath(
                '/html/body/div/div/div[2]/main/div/div[3]/div[3]/div[1]/div/article/div/div/div[2]/div/section/div/div[2]/div[4]/button').clear()
        finally:
            time.sleep(300)
            browser.quit()


if __name__ == "__main__":
    unittest.main()

# https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1
