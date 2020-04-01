
# def myprint(x,*y):
#     for i in y:
#         print(i)
#     print(x)
# myprint('end',30,40,50)



# def myprint1(x,*y):
#     for i in y:
#         print(i,end=" ")
#     print(x,end=" ")
# myprint1('end',30,40,50)




def func(a,b,c=10,*args,**kw):
    print('a=', a,'b=', b,'c=', c,'args=', args,'kw=', kw)


func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=26)