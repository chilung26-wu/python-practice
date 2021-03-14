import pandas as pd
#read data
data=pd.read_csv("googleplaystore.csv") # 把csv 讀成一個 dataframe
#觀察資料
print("資料數量", data.shape)
print("資料欄位", data.columns)
print("========================")
# 分析資料:評分的各種統計數據

# 篩選錯誤/異常/不乾淨資料!!!!!!!!!!!!!!!!!!!!!!!
# condition=data["Rating"]>5 
# data=data[condition]
# print(data)
# condition=data["Rating"]<=5 
# data=data[condition]
# print("平均數", data["Rating"].mean())
# print("中位數", data["Rating"].median())
# print("前一千個應用程式平均", data["Rating"].nlargest(1000).mean())

#分析資料: 安裝數量的各種統計數據
#Installs 欄位是字串  不是數字  無法直接取平均數  要先轉換
#print(data["Installs"][10472])  #不乾淨資料"Free"  處理掉  
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","",regex=True).replace("Free",""))
# #print(data["Installs"])
# print("平均數", data["Installs"].mean())
# condition=data["Installs"]>100000
# print("安裝數量大於100000 的應用程式有幾個", data[condition].shape[0])

#基於資料的應用: 關鍵字搜尋應用程式
keyboard=input("請輸入關鍵字:")
condition=data["App"].str.contains(keyboard, case=False)  #case 忽略大小寫
print(data[condition]["App"])
print("包含關鍵字的應用程式數量", data[condition].shape[0])
