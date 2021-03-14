s1={3,4,5}
print(10 not in s1)
s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 #交集
print(s3)
s4=s1|s2 #聯集
print(s4)
s5=s1-s2 #差集
print(s5)
s6=s1^s2 #反交集  不重疊部分
print(s6)
s=set("Hello")
print("A" in s)

dic={"apple":"蘋果","bug":"蟲蟲"}
dic["apple"]="小蘋果"
print(dic["apple"])
dic={"apple":"蘋果","bug":"蟲蟲"}
print("test" not in dic)  #key 是否存在
del dic["apple"]
print(dic)
dic={x:x*2 for x in [3,4,5]}  #從列表產生字典
print(dic)

