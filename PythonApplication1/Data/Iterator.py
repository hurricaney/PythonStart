# 迭代器 Iterator

a=[1,2,3,4,5,6,7,8,9,10]

a=iter(a)

# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

for i in a:
     print(i)


# 生成器  包含yield
def count(n):
    x=0
    while x<n:
        yield x
        x+=1

for i in count(6):
     print(i)


# 生成器应用  斐波那契数列

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'done'

fib_generator=fib(20)
print(fib_generator)
# print(fib_generator.__next__())
# print(fib_generator.__next__())

while True:
    try:
        fib_value=fib_generator.__next__()
        print('fib_value:%s'%fib_value)
    except StopIteration as fibs:
        print('Generator return value:%s'%fib_value)
        break
