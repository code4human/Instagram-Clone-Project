#형 변환

#문자 -> 정수
x = '10'
print(x+x)     #1010
x = int(x)
print(x+x)     #20

#다른 타입 간의 연산은 정수&소수 타입만 가능
y = 10
z = 10.1
print(type(y+z))  #<class 'float'>


#유니코드 -> 문자
print(chr(65))    #A
print(chr(97))    #a  #알파벳 대문자 A~Z 26개 뒤에 특수문자 존재. 소문자 a~z는 97부터 시작.

#문자 -> 유니코드
print(ord('A'))   #65
print(ord('가'))  #44032 
print(chr(ord('A')+1))   #B
###ASCII 코드, 유니코드 표 참고하기


#10진수 -> 2진수, 8진수, 16진수
a = 13
print(bin(a))  #0b1101 
print(oct(a))  #0o15
print(hex(a))  #0xd

print(type(bin(a)))  #<class 'str'>
print(type(oct(a)))  #<class 'str'>
print(type(hex(a)))  #<class 'str'>

x = 0b1101
y = 0o15
x = 0xd
print(x, y, z)  #13 13 13  #10진법으로 출력
print(type(x), type(y), type(z))  #<class 'int'>
###10진수에 bin(), oct(), hex()를 적용하면 str로 변환됨
###직접 2진수, 8진수, 16진수를 대입하면 int형이다.


##딱 2진수만 출력하고 싶을 때
print(bin(a)[2:])

##1을 #으로, 0을 !으로 변환하고 싶을 때 (알고리즘 문제에 많이 출제)
print(bin(a)[2:].replace('1','#').replace('0', '!'))
