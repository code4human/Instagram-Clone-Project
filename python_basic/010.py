#함수의 클로저
##함수와 함께 독립적인 공간을 제공한다.
def f():
    x = 10
    def xPlus():
        nonlocal x
        x += 10
        return x
    return xPlus

fl = f() 
f2 = f()
print(f1())   #20
print(f1())   #30
print(f1())   #40
print(f2())   #20
'''
같은 함수를 할당 받아도 함수마다 독립적인 이론공간을 제공한다.
마치 별도로 동작하는 함수처럼 간섭이 없다.
'''