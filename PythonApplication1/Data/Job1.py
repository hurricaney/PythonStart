str1="请选择你目前的开发工作："
str2="1.Windows桌面应用程序"
str3="2.Web应用程序"
str4="3.Web服务"

print(str1)
print(str2)
print(str3)
print(str4)

while(True):
    # 读取用户输入的字符串
    num1=int(input("请输入你的选择："))

    # 判断用户输入
    str5="你目前的开发工作是："
    if num1==1:
        print(str5+str2)
    elif num1==2:
        print(str5+str3)
    elif num1==3:
        print(str5+str4)
    else:
        print("对不起你选择错误，下次请输入1-3之间的整数！")
