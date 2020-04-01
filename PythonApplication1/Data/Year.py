# 判断闰年
num1=int(input("请输入一个年份："))

if num1%100 ==0:
    if num1%400==0:
        print("是闰年！")
    else:
        print("不是闰年！")
else:
    if num1%4==0:
        if num1%100 !=0:
            print("是闰年！")
    else:
         print("不是闰年！")