#for문의 원리
x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]
for i in x:
    print(i)
## in 뒤에는 순회 가능한 객체가 위치한다. 순회를 다 하면 반복문을 나온다.
## x에 있는 것 하나씩 i로 들어온다.

print(1 in x)  #True
print(7 in x)  #True

for i in 'kimtaeeun':  # 문자열도 순회 가능한 객체
    print(i)

'''
for i in 15:  #순회 불가능
    print(i)
'''

for i in x:
    for j in y:
        print('{} x {} = {}'.format(i, j, i*j))


