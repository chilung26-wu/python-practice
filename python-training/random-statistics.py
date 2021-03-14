# #隨機模組
import random
# #隨機選取
# data=random.choice([1,5,6,10,20])
# print(data)

# data=random.sample([1,5,6,10,20], 3)
# print(data)

#洗牌
# data=([1,5,7,30])
# random.shuffle(data)
# print(data)

# # 0 ~ 1 隨機亂數
# data=random.random()
# print(data)

# # 0 ~ 1 隨機亂數
# # data=random.uniform(60, 100)  #60~100隨機亂數
# # print(data)

# #取得常態分配亂數 平均數100 標準差10
# data=random.normalvariate(100, 10)
# print(data)


#統計模組
import statistics as stat
# data=stat.median([1,2,3,4,5,8,100])
# print(data)

data=stat.stdev([1,2,3,4,5,8,10]) #標準差
print(data)