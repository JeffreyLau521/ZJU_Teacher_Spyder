# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
url = 'http://finance.huanqiu.com/'
browser.get(url)
time.sleep(3)
input = browser.find_element_by_css_selector('body > div.finance-page > div > div:nth-child(2) > div.finance-leftTxt > h4 > a')
input.click()
time.sleep(3)
print(input.is_displayed())
print(input.text)
windows = browser.window_handles
browser.switch_to_window(windows[1])
input2 = browser.find_element_by_css_selector('body > div.box > div > div.fallsFlow > ul > li:nth-child(1) > h3')
print(input2.is_displayed())
print(input2.text)
input2.click()
browser.close()




