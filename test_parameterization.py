from selenium import webdriver
import time
import unittest
import math
import pytest


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser

    browser.quit()


@pytest.mark.parametrize("number", ["236895",
                                    "236896",
                                    "236897",
                                    "236898",
                                    "236899",
                                    "236903",
                                    "236904",
                                    "236905"])
def test_abs1(browser, number):
    browser.implicitly_wait(5)
    link = f"https://stepik.org/lesson/{number}/step/1"
    answer = str(math.log(int(time.time())))
    browser.get(link)
    browser.find_element_by_tag_name('textarea').send_keys(answer)
    browser.find_element_by_tag_name('button').click()
    answer = browser.find_element_by_tag_name('pre')
    assert answer.text == 'Correct!', 'Not correct!'
    time.sleep(3)


if __name__ == "__main__":
    unittest.main()