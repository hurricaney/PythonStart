def TestError(d):
    try:
        print('正常结果：',8/d)
    except:
        print('这是异常！！！')
    else:
        print('其他异常！')
    finally:
        print('这是finally')

i=4
while(i>=0):
    TestError(i)
    i-=2


while True:
    s=input('请输入一个整数：')
    try:
        i=int(s)
        i=8/i

    except ValueError:
        print('确认输入的是数字！')
    except ZeroDivisionError:
        print('不能输入0！')

#   except(ValueError,ZeroDivisionError) as err:
#       print(err)
    else:
        print('正确！')