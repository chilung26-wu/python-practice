# iT 邦幫忙 - iThome
import urllib.request as req
url="https://ithelp.ithome.com.tw/m/api/list?type=latest"
#建立一個Request物件， 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") #f根據觀察，取得資料為 JSON 格式

# 解析JSON 格式資料 取得每篇文章標題  
import json
data=json.loads(data) # 把原始的JSON 資料解析成字典/列表的表現形式
#取得 JSON 資料中的文章標題
posts=data["data"]
for key in posts:
    post=key["subject"]
    print(post)

# 無法執行 因為 list indices must be integers or slices, not dict
# posts=data["data"]
# for key in posts:
#     post=posts[key]
#     print(post["subject"])