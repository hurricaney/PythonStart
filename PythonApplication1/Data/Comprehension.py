names=[['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],
       ['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]

# for循环
"""
temp=[]
for lst in names:
    for name in lst:
        if name.count('e') >= 2 :
            temp.append(name)
print(temp)
"""

# 嵌套推导
T=[name for lst in names for name in lst if name.count('e')>=2]
print(T)