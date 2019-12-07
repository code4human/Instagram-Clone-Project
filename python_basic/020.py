#클래스 변수 & 인스턴스 변수

#클래스 변수 
##모든 클래스에서 공유되는 멤버
class Car(object):
    kinds = []
    def addkinds(self, name):
        self.kinds.append(name)                               
    maxSpeed = 300                                
    maxPeople = 5                                
    def move(self, x):                            
        print(x, '의 스피드로 움직이고 있습니다.')
    def stop(self):                              
        print('멈췄습니다.')

k5 = Car() 
k5.addkinds('k5')
print(k5.kinds)    #['k5']

k5 = Car() 
k3 = Car()
k5.addkinds('k5')
k3.addkinds('k3')
print(k5.kinds)    #['k5', 'k3']
print(k3.kinds)    #['k5', 'k3']   

'''---------------------------------------------------------------------------------------------'''

#인스턴스 변수
##인스턴스에만 가지고 있는 요소
class Car(object):
    def addkinds(self, name):
        self.kinds = []
        self.kinds.append(name)                               
    maxSpeed = 300                                
    maxPeople = 5                                
    def move(self, x):                            
        print(x, '의 스피드로 움직이고 있습니다.')
    def stop(self):                              
        print('멈췄습니다.')

k5 = Car() 
k3 = Car()
k5.addkinds('k5')
k3.addkinds('k3')
print(k5.kinds)    #['k5']   
print(k3.kinds)    #['k3']   # 함수가 define될 때마다 초기화되니까 자기자신만 가진다.
### self의 역할 : 인스턴스와 클래스를 구분짓는다.
### def addkinds(self, name) 에서 self 말고 이름을 바꿔도 작동하지만 관습적으로 self라고 쓴다. 
