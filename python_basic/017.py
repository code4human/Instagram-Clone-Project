#형 변환

#list, tuple, set, dict
a = 'kimtaeeun'
print(list(a))  #['k', 'i', 'm', 't', 'a', 'e', 'e', 'u', 'n']
print(tuple(a)) #('k', 'i', 'm', 't', 'a', 'e', 'e', 'u', 'n')
print(tuple(list(a)))  #('k', 'i', 'm', 't', 'a', 'e', 'e', 'u', 'n')
print(set(a))   #{'m', 'k', 'n', 't', 'e', 'u', 'a', 'i'}  무순서, 중복 제거된 집합 
#print(dict(a))  #딕셔너리 형 변환 불가 dictionary update sequence element #0 has length 1; 2 is required 


##구글 입사문제)
'''
1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
8이 포함되어 있는 숫자의 개수를 카운팅하는 것이 아니라
8이라는 숫자를 모두 카운팅 해야한다.
(*예를 들어 8808은 3, 8888은 4로 카운팅 해야 함)
'''

"""해답 1"""
#0008     # 0이 위치한 자리에 000~999까지 1000개의 숫자 들어갈 수 있다.
#0080
#0800
#8000     # 총 4000개

##0088은 0008에서 카운팅 되고, 0080에서 카운팅 된다. 이때 88은 2로 카운팅 해야하므로 중복을 허락하면 된다.
##따라서 답은 4000개다.

"""해답 2"""
str(list(range(1, 10001)))    #'[1, 2, 3, 4, ..., 10000]' 
print(str(list(range(1, 10001))).count('8'))   #4000
print(list(range(1, 10001)).count(8))          #1 

