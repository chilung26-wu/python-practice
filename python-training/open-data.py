#網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") #取得台灣大學網站原始碼(HTML, CSS, JS)
# print(data)

import urllib.request as request
import json
src="https://data.tycg.gov.tw/api/v1/rest/datastore/f4ece141-4044-45bf-8a2d-2d1f1171dd74?format=json%22"
with request.urlopen(src) as response:
    data=json.load(response) #利用 json模組處理 json資料格式
#print(data)

#取得公司名稱列表出來
# clist=data["result"]["records"]
# print(clist)

# clist=data["result"]["records"]
# for company in clist:
#     print(company["機關名稱"])

clist=data["result"]["records"]
with open("data1.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["機關名稱"]+":"+company["傳真"]+"\n")