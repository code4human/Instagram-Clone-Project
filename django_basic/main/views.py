from django.shortcuts import render
from .models import Cafe
import datetime 
#from main.forms import *

def index(request):  #사용자가 url을 치거나 어떤걸 클릭하면 서버로는 request가 날아감. 그리고 서버에서는 우리한테 값을 주는데 그걸 response라고 한다.
    return render(request, 'main/index.html') #django.shortcuts에서 불러온 render함수를 이용한다. index.html에서는 공백을 병합한다. 정확히는 템플릿 태그라고 얘기한다.
                                              #브라우저에서는 템플릿 문법을 볼 수 없다. html, css, javascript만 볼 수 있다.
                                              #render는 index.html에 담긴 템플릿 문법을 해석해서 사용자에게 사용자에게 response를 던져주게 된다. 
                                              #main폴더 바로 안에 index.html을 넣는 것은 아니다.
                                              #약속한 바에 의하면 main 안에 templates폴더를 만들고 templates폴더 안에 다시 main이라는 폴더를 만든다.
                                              #그리고 그 곳에 index.html을 만들어 준다.
                                              #앱main>templates>main>index.html
                                              #복잡한 이유 : index.html이 main 앱에만 있지 않을 수 있다. 
                                              # 만약 about이라는 상세페이지 앱을 만든다면 앱about>templates>about>index.html로 된다.
                                              #파일이름이 같기 때문에 트리를 하나 더 만든거다.

def cafelist(request):
    cafelistobj = Cafe.objects.all() #cafelistobj에 카페 리스트 전체가 넘어간다.
    return render(request, 'main/cafelist.html', {'cafelistobj': cafelistobj}) 


def cafedetails(request, pk):
    cafeobj = Cafe.objects.get(pk=pk) #pk에 해당되는 번호를 가져오겠다.
    return render(request, 'main/cafedetails.html', {'cafeobj': cafeobj}) 

def sample(request):
    value = [100, 200, 300]
    value2 = {'seoul':'work', 'jeju':'nature'}
    value3 = 'kim'
    dateT = datetime.datetime.now()
    sampleText = '''kimtaeeun
                 tena kim
                 student'''
    l = [1, 2, 3]
    return render(request, 'main/sample.html', {'value': value, 'value2': value2, 'value3': value3, 
    'dateT': dateT, 'sampleText':sampleText, 'l':l}) 

