import pymongo
from io import StringIO
import bson.binary

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

#访问指定的数据库
databaseName='local'
mydb=myclient[databaseName]

colName='wordVocab'
#判断当前的集合是否存在
collist=mydb.list_collection_names()
if colName in collist:
    print('collction has contained!')

col_wordVocab=mydb[colName]
    
#add new data in collection
word_ancestor = { "wordName": "ancestor", "cnName": "祖宗;祖先;(动物的)原种;(机器的)原型", "memorySkill": "an 加强 + cest〔= cess〕行走，前进 + or 表人 → 走了很久的人 → 祖先" }
x = col_wordVocab.insert_one(word_ancestor) 

print(x)


#create Images  collections 
colImagesTiltle='images'
col_images=mydb[colImagesTiltle]

#/Users/macroxu/Desktop/logo_40c4f13.svg
fileName='/Users/macroxu/Desktop/logo_40c4f13.svg'
with open (fileName,'rb') as myimage:
        col_images.save(dict(
        content= bson.binary.Binary(myimage.read()),
        filename = 'logo_40c4f13.svg'
      ))

# read binary data from mongoDB
data = col_images.find_one({'filename':'logo_40c4f13.svg'})
with open('/Users/macroxu/Desktop/logo_dom','wb') as outfile:
    outfile.write(data['content'])


