from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    #instagram\urls.py에서 이미 accounts 경로를 설정해줬으므로 accounts/signup/이 아님
    path('signup/', signup, name='signup'),  
    path('login/', login_check, name='login'),
    path('logout/', logout, name='logout'),

    path('follow/', follow, name='follow'),
]
