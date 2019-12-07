#클래스의 매직 메소드

class Car(object):
    def __init__(self):
        print('인스턴스가 생성되었습니다.')
    def addkinds(self, name):
        self.kinds = []
        self.kinds.append(name)                               
    maxSpeed = 300                                
    maxPeople = 5                                
    def move(self, x):                            
        print(x, '의 스피드로 움직이고 있습니다.')
    def stop(self):                              
        print('멈췄습니다.')


k3 = Car()  #인스턴스가 생성되었습니다.
print(dir(k3))
'''
init : 생성자. 인스턴스가 생성됐을 때 실행
del : 소멸자. 인스턴스가 소멸될 때 실행
add : + 연산
sub : - 연산 
or : 비트단위 or연산
repr, str : 클래스를 프린트 했을 경우 출력해주는 문자열. repr을 더 권장.
call : 함수를 호출했을 때 실행
getattr : 속성 가져올 때 실행
setattr : 속성 할당할 때 실행
delattr : 속성 제거할 때 실행
dataattribute : 속성 가져올 때 실행
getitem : 인덱싱, 슬라이싱, 반복을 위해 사용
setitem : 인덱스, 슬라이스된 값을 가져오기 위해 사용
delitem : 인덱스와 슬라이스된 값을 삭제하기 위해 사용
bool : bool()을 출력해주기 위한 매직 메소드
len : len()을 출력해주기 위한 매직 메소드
lt, gt, le, ge, eq, ne : >, <, <=, >=, ==, !=
radd : 오른쪽 기준 연산자
iadd : 할당 연산 +=, -=
iter, next : 반복을 위해 사용
contains : in 연산자(True, False 반환)
index : 정숫값을 나타낸다. (순서의 의미 x)
enter, exit : 컨텐츠 매니저. with에 사용됨
get, set, delete : 디스크립터 속성. .을 찍고 사용
new : init 이전에 객체를 생성할 때 사용
'''
