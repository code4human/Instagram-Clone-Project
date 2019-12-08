#Python Built-in Functions 내장함수

#sorted(), reversed()
x = [5,6,7,1,2,3]
print(sorted(x))               #[1, 2, 3, 5, 6, 7]
print(reversed(x))             #<list_reverseiterator object at 0x00000259A4BC4DA0>
print(list(reversed(x)))       #[3, 2, 1, 7, 6, 5]
print(sorted(x, reverse=True)) #[7, 6, 5, 3, 2, 1]

## sort() : list의 내장함수 
x.sort()

#max(), min(), sum()
x = [100, 200, 300, 400]
print(max(x))
print(min(x))
print(sum(x))

#zip()
a = 'ABC'
b = 'DEF'
c = 'GHI'
d = [1,2,3]
print(list(zip(a, b, c)))  #[('A', 'D', 'G'), ('B', 'E', 'H'), ('C', 'F', 'I')]
print(list(zip(a, b)))     #[('A', 'D'), ('B', 'E'), ('C', 'F')]
print(list(zip(a, d)))     #[('A', 1), ('B', 2), ('C', 3)]

print(zip(a,d))            #<zip object at 0x000001CD10799948>  그냥 출력하면 object로만 나옴. 리스트든 튜플이든 형 변환을 해줘야 한다.
##zip은 순회 가능
for i in zip(a,d):         #('A', 1)
    print(i)               #('B', 2) 
                           #('C', 3)

#map(funtion, iterable object)
def taeeun(x):
    return x*2

print(list(map(taeeun, [1,2,3])))   #[1, 4, 9]  map()을 list() 안에 넣지 않으면 object로만 나옴.
print(list(map(taeeun, 'abc')))     #['aa', 'bb', 'cc']
print(list(map(lambda x: x*2, 'abc')))     #보통은 람다를 많이 씀 ['aa', 'bb', 'cc']



