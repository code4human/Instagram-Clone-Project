#모듈
#임포트 방법 (1)
from people import name, age
#from people import *

print(name, age)    #kimtaeeun 23


#임포트 방법 (2)
import people
print(people.name, people.age)   #kimtaeeun 23

import people as p    #별칭
print(p.name, p.age)


#폴더 안의 모듈 찾기
import dir1.dir2.people

#해당 폴더
from . import name, age

#상위 폴더
from .. import name, age
