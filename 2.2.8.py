# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    a1 = browser.find_element_by_xpath('/html/body/div/form/div/input[1]')
    a1.send_keys('asd')
    a2 = browser.find_element_by_xpath('/html/body/div/form/div/input[2]')
    a2.send_keys('asd')
    a3 = browser.find_element_by_xpath('/ html / body / div / form / div / input[3]')
    a3.send_keys('asd@asd.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла # не забыть создать файл
    browser.find_element_by_xpath('//*[@id="file"]').send_keys(file_path)

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    a5 = browser.find_element_by_xpath('/html/body/div/form/button').click()

finally:
    time.sleep(6)
    browser.quit()
