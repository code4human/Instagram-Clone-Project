#MRO
#Method Resolution Order
##메소드 검색 순서

class One : x = 1         #멤버 x
class Two(One) : pass     #One을 상속
class Three(One) : x = 2  #One을 상속, 멤버 x를 재정의
class Four(Two, Three) : pass

i = Four()
print(i.x)  #2

''' 탐색순서 (python3) : 옆으로 간다. x 발견하면 탐색 멈춘다.
    One

Two  →  Three
  ↖
    Four
'''


''' 탐색순서 (python2) : 위로 올라간다.
    One
  ↗
Two      Three
  ↖
    Four
'''

