#연산자 오버로딩
#클래스 안에 원래 존재하는 것을 재정의하는 것

class Test:
    def __init__(self, testdata):
        self.data = testdata
    def __sub__(self, other):
        return Test(self.data + other)   ##sub는 -연산이지만 + 해봄

x = Test(5)
y = x-2
print(y.data)  #7 


#클래스의 상속
class Car(object):        #부모 클래스, 슈퍼 클래스                    
    maxSpeed = 300                                
    maxPeople = 5                                
    def move(self, x):                            
        print(x, '의 스피드로 움직이고 있습니다.')
    def stop(self):                              
        print('멈췄습니다.')

class HybridCar(Car):     #자식 클래스
    battery = 300
    batteryKM = 300

k5 = Car()
hyk5 = HybridCar()

print(hyk5.maxSpeed)   #300


##상속은 다중으로도 가능
class C1:
    pass
class C2:
    pass

class HybridCar(Car, C1, C2):     #자식 클래스
    battery = 300
    batteryKM = 300