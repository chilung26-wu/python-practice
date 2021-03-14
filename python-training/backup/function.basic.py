# #定義函式
# def multiply(n1,n2):
#     print(n1*n2)
#     return n1*n2
# #呼叫函式
# multiply(3,4)
# value=multiply(3,4)
# print(value)
# multiply(10,8)

def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

calculate(10)
calculate(20)