#클래스 기본 개념
'''
(현실)     (코드)
숫자   ->  class 'int'
문자   ->  class 'str'
자동차 ->  class Car()
'''

class Car(object):                                #클래스 (이름은 관습적으로 대문자 시작)
    maxSpeed = 300                                #속성 (클래스 안의 변수는 멤버)
    maxPeople = 5                                 #속성 (클래스 안의 변수는 멤버)
    def move(self, x):                            #기능 (클래스 안의 함수는 메소드)
        print(x, '의 스피드로 움직이고 있습니다.')
    def stop(self):                               #기능 (클래스 안의 함수는 메소드)
        print('멈췄습니다.')

k5 = Car()        ## 클래스의 인스턴스 선언
k3 = Car()        ## 클래스의 인스턴스 선언

k5.move(10)          #10 의 스피드로 움직이고 있습니다.   
k3.move(5)           #5 의 스피드로 움직이고 있습니다.
k5.stop()            #멈췄습니다.
k3.stop()            #멈췄습니다.
print(k5.maxSpeed)   #300
print(k3.maxSpeed)   #300
print(type(k5))      #<class '__main__.Car'>
print(type(k3))      #<class '__main__.Car'>
print(dir(k3))

'''
k5.move(10) 멤버접근 연산자.을 통해서 안에 있는 메소드에 접근한다.
리스트.sort() 처럼 선언돼있는 것들을 불러올 때 이렇게 사용한다.
'''
