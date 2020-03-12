from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
def photo_path(instance, filename):
    from time import strftime
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '{}/{}/{}.{}'.format(strftime('post/%Y/%m/%d'), instance.author.username, pid, extension)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #user모델의 내용을 외래키로 받는다
    photo = ProcessedImageField(upload_to=photo_path,
                                processors=[ResizeToFill(600,600)],
                                format='JPEG',
                                options={'quality':90}
                                )
    content = models.CharField(max_length=140, help_text="최대 길이 140자 입력 가능합니다.")
    
    #다대다관계
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                         blank=True,    #like는 필수값이 아님
                                         related_name='like_user_set',
                                         through='Like') #Like 모델과 연결시킴(post.like_set으로 접근이 가능해짐)

    bookmark_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                         blank=True,          #bookmark는 필수값이 아님
                                         related_name='bookmark_user_set',
                                         through='Bookmark')  #post.bookmark_set으로 접근이 가능해짐

    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add는 최초 생성될 때 
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']  #배열 기준

    @property
    def like_count(self):
        return self.like_user_set.count()

    @property
    def bookmark_count(self):
        return self.bookmark_user_set.count()

    def __str__(self):
        return self.content

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #포스트가 삭제되면 딸려있는 like도 삭제
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        #user와 post가 유니크한 관계를 갖게 한다
        unique_together = (
            ('user', 'post')
        )

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #포스트가 삭제되면 딸려있는 like도 삭제
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        #user와 post가 유니크한 관계를 갖게 한다
        unique_together = (
            ('user', 'post')
        )

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content
