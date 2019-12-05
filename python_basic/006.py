result = 0

for i in range(0, 101):  #0~100까지 더하기
    result += i

for i in range(0, 101, 2):  #0~100 사이의 짝수만 더하기
    result += i

for i in range(1, 101, 2):  #0~100 사이의 홀수만 더하기 (1)
    result += i

for i in range(0, 101, 1):  #0~100 사이의 홀수만 더하기 (2)
    if i % 2 != 0:
        result += i

'''
아래 두개는 동일한 결과

x = 1
while x < 10: 
    
for i in range(1,10):
'''
