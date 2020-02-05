from selenium import webdriver
import time
import unittest
import math
import pytest

browser = webdriver.Chrome()
browser.implicitly_wait(5)


@pytest.mark.parametrize('number', ["236895",
                                       "236896",
                                       "236897",
                                       "236898",
                                       "236899",
                                       "236903",
                                       "236904",
                                       "236905"])
class TestAbs(unittest.TestCase):

    def test_abs1(self, number):
        try:
            link = f"https://stepik.org/lesson/{number}/step/1"
            answer = str(math.log(int(time.time())))
            browser.get(link)
            browser.find_element_by_tag_name('textarea').send_keys(answer)
            browser.find_element_by_tag_name('button').click()
            answer = browser.find_element_by_tag_name('pre')
            assert answer.text == 'Correct!', 'Not correct!'
        finally:
            time.sleep(3)
            browser.quit()


if __name__ == "__main__":
    unittest.main()

# "https://stepik.org/lesson/236895/step/1",
# "https://stepik.org/lesson/236896/step/1",
# "https://stepik.org/lesson/236897/step/1",
# "https://stepik.org/lesson/236898/step/1",
# "https://stepik.org/lesson/236899/step/1",
# "https://stepik.org/lesson/236903/step/1",
# "https://stepik.org/lesson/236904/step/1",
# "https://stepik.org/lesson/236905/step/1"
