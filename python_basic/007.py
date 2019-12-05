#함수
##이름으로 코드를 묶은 것
##관리 쉽고 재사용 가능


#사용자 정의함수 실행순서
def plus (x, y):   #1
    z = x + y      #3
    return z       #4

print(plus(3,7))   #2


#인자가 없는 함수
def printNum():
    print('one')
    print('two')

printNum()  #실행하면 printNum() 함수 내의 print문들이 실행된다.
print(printNum()) #실행하면 print문 출력과 함께 None을 반환한다. 함수에 return문이 없으면 return None이 자동으로 들어간다.


#함수 선언해두고 나중에 채우고 싶을 때 
def empty():
    pass     #pass채우면 아무것도 실행하지 않고 넘어감
