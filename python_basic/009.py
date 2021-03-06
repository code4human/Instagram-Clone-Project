# 재귀함수
##재귀함수로 표현할 수 있는 것을 반복문으로 표현 가능
##반복문으로 표현할 수 있는 것을 재귀함수로 표현 가능
def f(n):  #f()는 팩토리얼 함수로 사용자 정의
    if n > 1:
        return n*f(n-1)
    else:
        return 1

print(f(5))

'''
f(5) -> 리턴값 5*f(4)
f(4) -> 리턴값 4*f(3)
f(3) -> 리턴값 3*f(2)
f(2) -> 리턴값 2*f(1)
f(1) -> 리턴값 1*f(0)
'''
