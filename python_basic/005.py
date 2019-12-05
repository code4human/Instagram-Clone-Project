#range(start:stop:step)
###1. 많은 데이터를 미리 준비하지 않아도 된다.
###2. 필요한 시점에만 데이터를 사용한다. (메모리 낭비 방지)

print(list(range(10))) #0부터 10까지. 시작값 스킵하면 0
print(list(range(10, 20)))  #스텝은 스킵하면 1
print(list(range(1, 100, 1))) #1부터 99까지 리스트 만들어줌
print(list(range(5, -5, -1))) #5부터 -4까지

print(type(range(10))) #출력값 <class 'range'>
###Python 2버전에서 type(range(10))는 list 타입이다.
###Python 3버전에서 range()의 타입은 range다. 

'''
만약 range(1000000)을 하면 많은 메모리가 소모된다. 
그러나 이 데이터를 생성하는 즉시 사용하지 않는다.
필요한 시점에만 사용하기 위해서 Python 3버전에서 range 타입이 생겼다.
그런데 2버전에도 range 타입이 있긴 했다. xrange()라는 이름으로. 

print(type(xrange(100))) #2버전 기준 출력값 <type 'xrange'>

for i in xrange(10): #2버전에서 range()처럼 돌아갔다.
    print(i)
'''

x = iter(range(10))  #0~9
print(next(x))   #0
print(next(x))   #1
print(next(x))   #2 

