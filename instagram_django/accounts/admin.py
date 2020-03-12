from django.contrib import admin
from .models import Profile, Follow 

# Register your models here.
class FollowInline(admin.TabularInline): #팔로우 내용 표 형식
    model = Follow
    fk_name = 'from_user'

@admin.register(Profile) #모델 불러옴
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'user'] #id는 장고가 자동생성
    list_display_links = ['nickname', 'user']
    search_fields = ['nickname']
    inlines = [FollowInline]

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'created_at']
    list_display_links = ['from_user', 'to_user', 'created_at']

