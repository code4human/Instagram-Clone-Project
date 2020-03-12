from django import forms
from django.contrib import admin
from .models import Post, Like, Bookmark, Comment

# Register your models here.
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = '__all__'

#admin페이지를 표 형식으로 정리하기
class LikeInline(admin.TabularInline):
    model = Like
class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'nickname', 'content', 'created_at']
    list_display_links = ['author', 'nickname', 'content']
    form = PostForm
    inlines = [LikeInline, CommentInline]

    #nickname이라는 부분이 post의 models.py에 들어있지 않으므로 함수 정의
    def nickname(request, post):
        return post.author.profile.nickname

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at'] 
    list_display_links = ['post', 'user'] 

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at'] 
    list_display_links = ['post', 'user'] 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'content', 'author', 'created_at'] 
    list_display_links = ['post', 'content', 'author']  
    
