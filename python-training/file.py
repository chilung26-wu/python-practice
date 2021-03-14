# #儲存檔案
# file=open("data.txt", mode="w", encoding="utf-8")
# file.write("測試中文\n好棒棒")
# file.close()

# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("測試中文啦\n好棒棒")
# #讀取檔案
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     data=file.read()
# print(data)

# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("5\n3")
# sum=0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     for line in file:
#         sum+=int(line)
# print(sum)

# import json
# with open("config.json", mode="r") as file:
#     data=json.load(file)
# print(data) #data 是一個字典 
# print("name: ", data["name"])
# print("version: ", data["version"])

#從檔案中讀取 JSON 資料，放入變數 data 裡面
import json
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) #data 是一個字典
data["name"]="New Name" #修改變數的資料 
#寫入最新資料
with open("config.json", mode="w") as file:
    json.dump(data,file)
