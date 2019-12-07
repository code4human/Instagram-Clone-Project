#형 변환

#bool의 형 변환
print(bool([]))  #False   
bool(())         #False
bool({})         #False
bool(0)          #False
bool(0.0)        #False
bool('')         #False
bool(' ')        #True
bool(1)          #True
bool(-1)         #True
bool(('a'))      #True


#all()
a = [True, False, False]
b = [True, True, True]
c = [False, False, False]
d = ['  ', 0, 0.0]
print(all(a), all(b), all(c), all(d))  #False True False False
### all()은 모든 게 True인지를 판단한다.


#any()
print(any(a), any(b), any(c), any(d))   #True True False True
### any()는 하나라도 True가 있는지를 판단한다.

