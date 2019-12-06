#딕셔너리 기초
#딕셔너리는 순서가 없고 다른 자료형을 담을 수 있다. 

#호출
d = {'one':1, 'two':2, 'three':3}
print(d['one'])  #key로 호출

#값의 추가와 삭제
d['four'] = 4
del d['four'] 
print(d)


#딕셔너리 메소드
##copy()를 쓰지 않는 다면 발생하는 문제
##같은 id (같은 object를 가리킨다)
jeju = {'banana':4000}
seoul = jeju
jeju['banana'] = 6000
print(seoul)    #seoul 딕셔너리의 value도 바뀜
print(id(seoul)) #3003708799016
print(id(jeju))  #3003708799016
## 이런 식으로 가리키고 있는 상태 
## seoul -> jeju -> {'banana':6000}

##copy()
jeju = {'banana':4000}  
busan = jeju.copy()   #jeju와 busan은 다른 object를 가리킴 (id가 다름)
jeju['banana'] = 6000
print(busan)          #busan 딕셔너리의 value는 그대로다.


##items()
print(d.items())      #dict_items([('one', 1), ('two', 2), ('three', 3)])
##keys()
print(d.keys())       #dict_keys(['one', 'two', 'three'])
##values()
print(d.values())     #dict_values([1, 2, 3])

##pop(키)
d.pop('one')          #{'two':2, 'three':3}

##update(딕셔너리)
d.update({'four':5})  #{'two':2, 'three':3, 'four':5}
###d['four'] = 4 와 동일한 결과. 그러나 이렇게 넣으면 하나의 키 값에 대응되는 하나의 value를 추가한다는 의미다.
###update()는 object를 추가한다는 의미다.


#switch 함수 
#다른 언어에는 있지만 파이썬에는 없다.

def s(key):
    return {
        'one':1,
        'two':2,
        'three':3,
        'four':4
    }.get(key, 'Not Found')

print(s('one'))  #1 
print(s('five')) #Not Found