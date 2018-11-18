from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
wait = WebDriverWait(browser, 10)


def search():
    browser.get('https://person.zju.edu.cn/index/search')
    # 判断浏览器网页是否加载成功
    # input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
    # input.send_keys('美食')
    total = 0
    submit = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#app > div > article > div > div.right.fr > div > div.searchAdvanced > div")))
    for i in range(2000):
        submit.click()
        time.sleep(5)
        total = total + 1
        print(total)
        # 点击了436下
    """ 
    while submit:
        submit.click()
        i = i+1
        print(i)                                                 
    """
def main():
    search()


if __name__ == "__main__":
    main()
# https://person.zju.edu.cn/server/api/front/psons/search?app_key=cgsoft&timestamp=1539334887000&sign=a2f5e631a6c3dcc795891c9bf1a08b95&size=5040&page=0&lang=cn