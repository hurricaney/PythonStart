
class MarkerMember:
    __name=''
    count=600
    def __init__(self, name):
        self.__name=name
        print(self.__name+'当前积分为：'+str(self.count))
    def change(self,count1):
        self.count=self.count+count1
        print(self.__name+'更改后积分为：'+str(self.count))


m=MarkerMember('moyuer')
m.change(1000)
print(m.count)