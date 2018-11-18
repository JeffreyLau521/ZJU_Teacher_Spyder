import pymongo
client = pymongo.MongoClient('localhost',27017)
ZJU_Teacher_Information= client['ZJU_Teacher_Information']
Teacher_homepage_Info = ZJU_Teacher_Information['Teacher_homepage_Info']
Different_homepag_Url = ZJU_Teacher_Information['Different_homepag_Url']
queryArgs = {}
projectionFields = ['homepage_url']
#searchRes = Teacher_homepage_Info.find(queryArgs, projection = projectionFields)
searchRes = Different_homepag_Url.find(queryArgs, projection = projectionFields)

print(searchRes)
for value in searchRes:
    print(value)




