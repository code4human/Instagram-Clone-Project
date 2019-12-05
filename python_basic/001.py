#format
name = input('이름을 입력하세요:')
age = input('나이를 입력하세요:')

print('제 이름은', name, '입니다.' '제 나이는', age, '입니다.')  #콤마로 연결하면 space가 자동으로 들어감
print('제 이름은 %s입니다. 제 나이는 %s입니다.'%(name, age))
print('제 이름은 {}입니다. 제 나이는 {}입니다.'.format(name, age))
print('제 이름은 {0}입니다. 제 나이는 {0}입니다.'.format(name, age)) #뒤에서 넣을 것의 index로 넣음.

s =  '제 이름은 {name}입니다. 제 나이는 {age}입니다.'
print(s.format(name='Taeeun', age=23))


#format의 자리차지
##오른쪽 정렬
print('{0:4} x {1:4} = {2:4}'.format(2, 3, 6))     #4자리에 맞춰서 오른쪽
##왼쪽 정렬
print('{0:<4} x {1:<4} = {2:<4}'.format(2, 3, 6))  #4자리에 맞춰서 왼쪽
##중앙정렬
print('{0:^4} x {1:^4} = {2:^4}'.format(2, 3, 6))  #4자리에 맞춰서 중앙

print('{0:#>4} x {1:#>4} = {2:#>4}'.format(2, 3, 6))  
print('{0:#<4} x {1:#<4} = {2:#<4}'.format(2, 3, 6))
print('{0:#^4} x {1:#^4} = {2:#^4}'.format(2, 3, 6))   #나머지공간을 #으로 채워넣어라

##소수점 출력
print('{0:.3f}'.format(1/4)) #소수점 세 번째 자리
print('{0:,.3f}'.format(8888888888))

#파이썬 3.6버전부터 f문자열로 format 가능
print(f'제 이름은 {name}입니다. 제 나이는 {age}입니다.')
