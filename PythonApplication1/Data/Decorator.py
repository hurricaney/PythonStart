# 带参数的装饰器
def AddCheck1(func1):
    def check1(*args,**kw):
        print('真的要操作数据吗？')
        return func1(*args,**kw)
    return check1

@AddCheck1
def f4(arg1):
    print('增加数据'+arg1)
@AddCheck1
def f5(arg1,arg2):
    print('删除数据'+arg1+arg2)
@AddCheck1
def f6(arg1,arg2,arg3):
    print('修改数据'+arg1+arg2+arg3)

f4('100')
f5('100/','200')
f6('100/','200/','300')

# 多个装饰器装饰一个函数
def d1(func):
    def check(*args,**kw):
        print('真的要操作数据吗？')
        return func(*args,**kw)
    return check
def d2(func):
    def check2(*args,**kw):
        print('真的是该部门吗？')
        return func(*args,**kw)
    return check2

@d1
@d2
def f1(arg1):
    print('增加数据'+arg1)

f1('部门1')