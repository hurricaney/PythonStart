class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._registry={
            'name':name,
            'age':age
            }


    def __getitem__(self,key):
        if key not in self._registry.keys():
            raise Exception('Please registry the key:%s first !' %(key,))
        return self._registry[key]
    def __setitem__(self,key,value):
        if key not in self._registry.keys():
            raise Exception('Please registry the key:%s first !' %(key,))
        self._registry[key]=value


# p=Person('moyuer','25')
# print(p['name'],p['age'])
# p['age']=30
# print(p['name'],p['age'])

class Person1:
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def __getattribute__(self, item):
        return super(Person1,self).__getattribute__(item)
    def __setattr__(self, item,value):
        super(Person1,self).__setattr__(item, value)
    def __delattr__(self, item):
        print('属性被删除了！！！')

p=Person1('moyuer',30)
print(p.name,p.age)
p.addr='shanghai'
print(p.addr)
del p.addr