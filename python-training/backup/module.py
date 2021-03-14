# import sys as system
# print(system.platform)
# print(system.maxsize)

# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# result=geometry.slope(1,2,5,6)
# print(result)

#模組搜尋路徑
import sys
print(sys.path)
sys.path.append("modules")
print("----------------------------")
import geometry
print(geometry.distance(1,1,5,5)) 