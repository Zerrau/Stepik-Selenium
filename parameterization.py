from selenium import webdriver
import time
import unittest

link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        try:
            browser.get(link)
            browser.find_element
        finally:
            time.sleep(3)
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
