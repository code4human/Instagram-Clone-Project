#Python Built-in Functions 내장함수
#공식홈페이지 https://docs.python.org/3/library/functions.html

#내장함수 - 형변환
print(abs(-1)) #1

print(all([1,2,3,4,5,6,7])) #True  ##all()은 안에 있는 모든 값이 True여야 True를 반환
print(all([1,2,3,4,5,6,7,0]))  #False
print(any([0,0,0,1]))  #True
print(any([0,0,0,0]))  #False ##any()는 하나만 True여도 True 반환

print(bool(''))     #False
print(bool(' '))    #True
print(bool(0))      #False
print(bool(1))      #True

print(chr(65))      #A    ##아스키코드 표 참고
print(chr(97))      #a
print(ord('A'))     #65
print(ord('a'))     #97

print(dict([('one', 1), ('two', 2)]))  #{'one': 1, 'two': 2}
#print(dict(('one', 1), ('two', 2)))   불가능
#print(dict(('one', 1)))               불가능
#방법은 많고 공식홈페이지 참고

print(float(10))    #10.0
print(int(10.1))    #10   소수점 버림

print(set('aabbcc'))       #{'c', 'a', 'b'}
print(len(set('aabbcc')))  #3