import urllib.request
import json

url = "https://data.tycg.gov.tw/api/v1/rest/datastore/f4ece141-4044-45bf-8a2d-2d1f1171dd74?format=json%22"
response = urllib.request.urlopen(url)
contents = response.read().decode('utf-8-sig')
response.close()
#print(contents)    #要decode("utf-8")!!
books = json.loads(contents)      #str 轉 dic
# print(books)
# print("共有: ", len(books), "本書")
clist=books["result"]["records"]       #!!!!!!!!!資料的層次感!!!!!!!!!!!!  比較乾淨   只有一個中括號
# print(clist)
#print(json.dumps(clist, indent=4, ensure_ascii=False))     ######ensure_ascii=False########
for book in clist:
    print("第"+str(book["_id"]-1)+"個", end="  ")
    print("機關名稱:", book["機關名稱"], end="    ")
    print("傳真:", book["傳真"])
    # print("機關名稱:", book["機關名稱"], "傳真:", book["傳真"], sep="&")
    # print("傳真:", book["傳真"])
