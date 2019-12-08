#Python Built-in Functions 내장함수

#enumerate()
##리스트, 딕셔너리, 셋 같은 자료의 index를 붙이고 싶을 때 사용
name = ['a', 'b', 'c']
for i in enumerate(name):    #(0, 'a')
    print(i)                 #(1, 'b')
                             #(2, 'c')

for i, j in enumerate(name, 100):   #100 a   시작값 100을 j에 부여
    print(i, j)                     #101 b
                                    #102 c

x = [(1, 2), (3, 4), (5, 6)]        #(1, 2)
for i in x:                         #(3, 4)
    print(i)                        #(5, 6)

for i, j in x:                      #1 2
    print(i, j)                     #3 4
                                    #5 6

xx = [(1, 2, (10, 20)), (3, 4, (30, 40)), (5, 6, (50, 60))]
for (i, j, (k, z)) in xx:           #1 2 10 20
    print(i, j, k, z)               #3 4 30 40
                                    #5 6 50 60
'''
실행 안 됨
for i, j in xx:  형태에 맞춰야 함
    print(i, j)
'''