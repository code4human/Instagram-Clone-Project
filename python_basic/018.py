#형 변환

#dict
a = dict(one=1, two=2, three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1,2,3]))
d = dict([('two',2), ('one',1), ('three',3)])
e = dict({'three':3, 'one':1, 'two':2})
print(a == b == c == d == e)    #True
print(a, b, c, d, e)            #{'one': 1, 'two': 2, 'three': 3}가  5번 출력됨



## zip()
### zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
### 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.

print(list(zip([1, 2, 3], [4, 5, 6])))    # [(1, 4), (2, 5), (3, 6)]
print(dict(zip([1, 2, 3], [4, 5, 6])))    # {1: 4, 2: 5, 3: 6}

print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))   # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
#print(dict(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))  # dictionary update sequence element #0 has length 3; 2 is required

print(list(zip("abc", "def")))   # [('a', 'd'), ('b', 'e'), ('c', 'f')]
print(dict(zip("abc", "def")))   # {'a': 'd', 'b': 'e', 'c': 'f'}



## map()
### map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. 
### map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

### 예제 1 - map() 미활용
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)                          # [2, 4, 6, 8]


### 예제 2 - map() 활용
def two_times_2(x): 
    return x*2

list(map(two_times_2, [1, 2, 3, 4]))   # [2, 4, 6, 8]


### 예제 3 - lambda 활용
list(map(lambda a: a*2, [1, 2, 3, 4])) # [2, 4, 6, 8]



## lambda 인자 : 표현식
def hap(x, y):
    return x + y
hap(10, 20)                         #30

(lambda x,y: x + y)(10, 20)         #30



map(lambda x: x ** 2, range(5))         #[0, 1, 4, 9, 16]    ## python 2   #python3에서 <map object at 0x00000267E23F3F28> 라고 출력됨

list(map(lambda x: x ** 2, range(5)))   #[0, 1, 4, 9, 16]    ## python 2 및 python 3