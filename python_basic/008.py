#변수 충돌
x = 10
def xplus():
    x += 10 #지역변수

xplus()   #local variable 문제 발생
print(x) 
### 안에 있는 변수는 밖으로 못 나간다.
### 밖에 있는 변수는 안으로 못 들어간다.


# global 
# 밖에 있는 변수를 사용하고 싶을 때 사용
# 일부로 만든 규칙을 깨는 것이므로 실무에서 잘 사용하지 않음
x = 10
def xplus():
    global x
    x += 10
xplus()
print(x)


# 일반적인 방법
x = 10
def xplus(y):
    y += 10
    return y
x = xplus(x)
print(x)