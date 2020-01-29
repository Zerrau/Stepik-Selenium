import time
import math
from selenium import webdriver
import unittest
import pytest


@pytest.mark.parametrize('link',
                         ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                          "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                          "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                          "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class SubclassesTest(unittest.TestCase):

    def test_One(link):
        browser = webdriver.Chrome()
        browser.get(link)
        answer = str(math.log(int(time.time())))

        browser.implicitly_wait(5)
        try:
            browser.get(link)
            browser.find_element_by_xpath(
                '/html/body/div/div/div[2]/main/div/div[3]/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/textarea').send_keys(
                answer)
            browser.find_element_by_xpath(
                '/html/body/div/div/div[2]/main/div/div[3]/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[2]/div[4]/button').click()
            correct_1 = browser.find_element_by_xpath('//pre[text()="Correct!"]')

            assert correct_1.text != ' Not Correct!'
        finally:
            time.sleep(1)
            browser.quit()


if __name__ == '__main__':
    unittest.main()

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")