#셋 기초
##셋(집합)은 순서가 없고 중복을 허락하지 않는다.

s = {100, 200, 300, 400, 400, 400} 
print(s)  #{200, 100, 400, 300}
ss = {10}
sss = {400, 500}
#연산기호로는 덧셈, 뺄셈, 나눗셈, 곱셈 중 뺄셈만 가능하다.
print(s-sss)  #{200, 100, 300}


#내장 메소드
print(type(s))
print(dir(s))
##1. 교집합
print(s & sss)               #{400}
print(s.intersection(sss))   #{400}

##2. 합집합
print(s | sss)               #{400, 200, 500, 100, 300}
print(s.union(sss))          #{400, 200, 500, 100, 300}

##3. 차집합
print(s - sss)               #{200, 100, 300}
print(s.difference(sss))     #{200, 100, 300}

##값의 추가
s.add(1000)                  #{100, 200, 1000, 300, 400}
##값의 삭제
s.remove(100)                #{200, 1000, 300, 400} 리스트의 remove는 처음 만나는 값을 지운다.
##여러개의 값을 추가
s.update({1,2,3})            #{400, 1, 2, 3, 200, 1000, 300} 

#문자열에서 중복 허락하지 않는 문자들이 뭔지 추출가능
##set으로 형변환 한 뒤 연산하면 됨
string = 'ag;dksl;dOAJAGDKSFKXZdskfjakv'
print(set(string))      #{'O', 'G', 'd', 'l', 'k', 'D', 'f', 's', 'Z', 'g', 'J', 'v', 'A', 'K', 'X', 'S', 'a', 'F', ';', 'j'}
print(len(set(string))) #20