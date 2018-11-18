# import pymongo
# #激活本地的mongodb数据库
# client = pymongo.MongoClient('localhost',27017)
# #命名数据库为：ZJU_Teacher_INFO
# ZJU_Teacher_Information = client['ZJU_Teacher_Information']
# #创建表单：teacher_url
# teacher_url = ZJU_Teacher_Information ['teacher_url'] #左边为python中的变量名称，右边为数据库中表单的名称
#
# practice_table =   ZJU_Teacher_Information ['practice_table']
from ZJU_Teacher_crawling import get_phu_detail
from multiprocessing import Pool
def insert_txt(path):
    #path = "E:/WorkSpace/PycharmProject/test/url.txt"
    homepage_list = []
    with open(path,'r') as f:
        lines = f.readlines()
        print(lines)
    for li in lines:
        homepage_list.append(li.replace('\n', ''))
    print(homepage_list)


    n = 0
    m = 2
    print(homepage_list[n: m])
    # homepage_list = []
    # path = "E:/WorkSpace/PycharmProject/test/url.txt"
    # with open(path, 'r') as f:
    #     list = f.readlines() #txt中所有字符串读入data
    # for li in list:
    #     homepage_list.append(li.replace('\n',''))
    while True:
        POOL = Pool(processes=2)
        for homepage in homepage_list[n:m]:
            POOL.apply_async(get_phu_detail, homepage)
        POOL.close()
        POOL.join()
        n = n + 2
        m = m + 2
        if m == 5014:
            break


        # for index,line in enumerate(lines):
        #     data = {
        #         'index': index,
        #         'line': line,
        #         'words': len(line.split())
        #     }
        #     teacher_url.insert(data)
"""
#  $lt/$lte/$gt/$gte/$ne,依次等价于</<=/>/>=/!=,(l表示less,g表示greater,e表示equal,nbiaoshinot )
for item in teacher_url.find():
    print(item['line'])
    
"""
# def main():
#     practice_table.insert({
#         "_id": 5,  # _id若没有自己指定，则mongodb内部会自动生成
#         "username": 'liwei',
#         "password": 123456,
#         "addr": 'ZJUroad',
#
#     })
if __name__ == "__main__":
    path = "E:/WorkSpace/PycharmProject/test/url.txt"
    insert_txt(path)
