#튜플 기초
##튜플은 변화하지 않지만 이렇게 출력 가능
t = (100, 200, 300, 400)
print(t+t)      #(100, 200, 300, 400, 100, 200, 300, 400)
print(t*3)      #(100, 200, 300, 400, 100, 200, 300, 400, 100, 200, 300, 400)
print(t[0])     #100
print(t[1:3])   #(200, 300)

##dir(t) 해보면 튜플은 리스트와 다르게 메소드가 count()와 index()밖에 없다.
print(t.count(100))  #1
print(t.index(200))  #1


#리스트와 튜플의 차이
#리스트 - 변경 가능한 데이터 
l = [100, 200, 300]
t = (100, 200, 300)
print(id(l))        #1275560100424
def change(i):
    print(id(i))    #1275560100424
    i[0] = 10000    #똑같은 id값을 가져오기 때문에(object가 같다) 지역변수가 바뀐다.
change(l)           
print(l)            #[10000, 200, 300]


##튜플 - 변경 불가능한 데이터
print(id(t))
def change(i):
    print(id(i))
    i[0] = 10000  
change(t)           #튜플은 할당이 허락되지 않는다. id값도 다르다.
print(t)
##튜플이 함수로 들어가서 인자값으로 쓰인다는 것은 그 값이 변화되지 않음을 보장할 수 있다는 얘기.
##튜플의 무결성 보장

