from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from config import *
import pymongo
#建立数据库连接
client = pymongo.MongoClient(MONGO_URL, 27017)
db = client[MONGO_DB]
def get_phu_detail(personal_homepage_url):
    """
    以下函数用于获取浙江大学每个教师的详细个人信息
    :param personal_homepage_url:
    """
    browser = webdriver.Chrome()
    try:
        browser.get(personal_homepage_url)

    except TimeoutException:
        print(personal_homepage_url + '的个人主页请求超时')
    # except:
    #     # 建立表格Different_homepag_Url存储网页结构不同的教师homepage
    #     another_homepage = {
    #         'homepage_url': personal_homepage_url,
    #     }
    #     save_to_mongodb3(another_homepage)
    time.sleep(1)
    wait = WebDriverWait(browser, 10)

    #建立空字典，用于存放教师个人主页上详细信息
    child = ( 'child1', 'child2', 'child3', 'child4', 'child5', 'child6', 'child7', 'child8',
        'child9', 'child10', 'child11', 'child12', 'child13', 'child14', 'child15', 'child16',
        'child17', 'child18', 'child19', 'child20', 'child21', 'child22', 'child23', 'child24')
    dic={
        'Teacher_name': None,
        'Research_Fields': None,
        'Subject': None,
        'Department': None,
        child[0]:  None,
        child[1]:  None,
        child[2]:  None,
        child[3]:  None,
        child[4]:  None,
        child[5]:  None,
        child[6]:  None,
        child[7]:  None,
        child[8]:  None,
        child[9]:  None,
        child[10]: None,
        child[11]: None,
        child[12]: None,
        child[13]: None,
        child[14]: None,
        child[15]: None,
        child[16]: None,
        child[17]: None,
        child[18]: None,
        child[19]: None,
        child[20]: None,
        child[21]: None,
        child[22]: None,
        child[23]: None,
    }
    all_labels1 = {
        'child1': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(1)',
        'child2': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(2)',
        'child3': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(3)',
        'child4': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(4)',
        'child5': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(5)',
        'child6': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(6)',
        'child7': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(7)',
        'child8': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(8)',

    }
    all_labels2 = {
        'child9': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(9)',
        'child10': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(10)',
        'child11': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(11)',
        'child12': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(12)',
        'child13': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(13)',
        'child14': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(14)',
        'child15': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(15)',
        'child16': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(16)',

    }
    all_labels3 = {
        'child17': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(17)',
        'child18': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(18)',
        'child19': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(19)',
        'child20': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(20)',
        'child21': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(21)',
        'child22': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(22)',
        'child23': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(23)',
        'child24': 'body > div > div > div.person-left > div.person-list > ul > li:nth-child(24)',
    }
    try:
        try:
            teacher_name = browser.find_element_by_css_selector('body > div > div > div.person-left > '
                                                                'div.person-message > div.teacher-message > '
                                                                'div.teacher-introduction.clearfixa')
            dic['Teacher_name'] = str(teacher_name.text)
        except NoSuchElementException:
            #建立表格Different_homepag_Url存储网页结构不同的教师homepage
            another_homepage = {
                'homepage_url':personal_homepage_url,
            }
            save_to_mongodb3(another_homepage)
        try:
            research_fields = browser.find_element_by_css_selector('body > div > div > div.person-left > '
                                                                   'div.person-message > div.teacher-message > '
                                                                   'div.teacher-introductions > ul > '
                                                                   'li:nth-child(5) > ul')
            dic['Research_Fields'] = str(research_fields.text)
        except NoSuchElementException:
            print(personal_homepage_url + '中不存在元素Research_Fields')
        try:
            subject = browser.find_element_by_css_selector('body > div > div > div.person-left > '
                                                           'div.person-message > div.teacher-message > '
                                                           'div.teacher-introductions > ul > li:nth-child(1) > a')
            dic['Subject'] = str(subject.text)
        except NoSuchElementException:
            print(personal_homepage_url + '中不存在元素Subject')
        try:
            department = browser.find_element_by_css_selector('body > div > div > div.person-left > '
                                                              'div.person-message > div.teacher-message > '
                                                              'div.teacher-introductions > ul > li:nth-child(2) > a')
            dic['Department'] = str(department.text)
        except NoSuchElementException:
            print(personal_homepage_url + '中不存在元素Department')


        COUNT = 0
        # 遍历第一个字典
        for key in all_labels1:
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, all_labels1[key])))
            if submit:
                submit.click()
                time.sleep(3)
                input2 = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[2]')
                if input2.is_displayed():
                    dic[child[COUNT]] = str(submit.text)  + ':\n' + str(input2.text).replace(' ', '')
                COUNT = COUNT + 1

        # # 判断是否点击加载更多选项卡，避免应selenium找不到对应视窗点击项而报错
        # try:
        #     move = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.btn.rightBtn')))
        #     for i in range(4):
        #         if move:
        #             move.click()
        # except:
        #     time.sleep(0.001)

        # 遍历第二个字典
        for key in all_labels2:
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, all_labels2[key])))
            if submit:
                submit.click()
                time.sleep(3)
                input2 = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[2]')
                if input2.is_displayed():
                    dic[child[COUNT]] = str(submit.text)  + ':\n' + str(input2.text).replace(' ', '')
                COUNT = COUNT + 1

        # # 判断是否点击加载更多选项卡，避免应selenium找不到对应视窗点击项而报错
        # try:
        #     move = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.btn.rightBtn')))
        #     for i in range(4):
        #         if move:
        #             move.click()
        # except:
        #     time.sleep(0.001)

        # 遍历第三个字典
        for key in all_labels3:
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, all_labels3[key])))
            if submit:
                submit.click()
                time.sleep(3)
                input2 = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[2]')
                if input2.is_displayed():
                    dic[child[COUNT]] = str(submit.text)  + ':\n' + str(input2.text).replace(' ', '')
                COUNT = COUNT + 1

    except Exception:
        print(personal_homepage_url + '的个人主页信息加载完毕')
    finally:
        #建立表格Teacher_detail_Iofo存储ZJU所有教师的详细信息
        save_to_mongodb4(dic)
        browser.close()
def save_to_mongodb3(another_url):
    """
    存储Different_homepag_Url表到mongodb
    :param another_url:
    """
    try:
        db[Different_homepag_Url].insert(another_url)
    except Exception:
        print('Different_homepag_Url表存储失败')
def save_to_mongodb4(what):
    """
    存储Teacher_detail_Iofo表到mongodb
    :param what:
    """
    try:
        db[Teacher_detail_Iofo].insert(what)
    except Exception:
        print('Teacher_detail_Iofo表存储失败')

if __name__ == "__main__":
    # queryArgs = {}
    # projectionFields = ['homepage_url']
    # searchRes = db['Different_homepag_Url'].find(queryArgs, projection=projectionFields)
    # #print(searchRes)
    # for value in searchRes:
    #     print(value['homepage_url'])
    path = "E:/WorkSpace/PycharmProject/test/another_url.txt"
    homepage_list = []
    with open(path, 'r') as f:
        lines = f.readlines()
        # print(lines)
    for li in lines:
        homepage_list.append(li.replace('\n', ''))
    # print(homepage_list)
    POOL = Pool(processes=6)
    POOL.map(get_phu_detail, homepage_list)
    POOL.close()  # 关闭进程池，不再接受新的进程
    POOL.join()  # 主进程阻塞等待子进程的退出

