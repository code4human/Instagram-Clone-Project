from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField  #이미지 처리 기능
from imagekit.processors import ResizeToFill  #업로드된 이미지 사이즈 바꾸는 기능 

# Create your models here.
def user_path(instance, filename): #매개변수(포토의 모델, 사용자가 업로드한 파일 이름)
    from random import choice #난수 발생 기능
    import string #대소문자 포함한 알파벳 불러옴
    arr = [choice(string.ascii_letters) for _ in range(8)]  #대소문자 관계없이 문자를 불러옴, 8번 반복
    pid = ''.join(arr) #8개의 알파벳을 붙인다.
    extension = filename.split('.')[-1] #파일 이름을 .을 기준으로 배열에 담고 마지막 부분(확장자)을 불러옴
    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension)  #accounts\사용자 폴더\무작위단어.확장자

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('별명', max_length=20, unique=True)

    follow_set = models.ManyToManyField('self',
                                        blank=True,
                                        through='Follow',
                                        symmetrical=False,
                                        )

    picture = ProcessedImageField(upload_to=user_path,
                                processors=[ResizeToFill(150,150)],
                                format='JPEG',
                                options={'quality':90},
                                blank=True,
                                )

    about = models.CharField(max_length=300, blank=True)
    GENDER = (
        ('선택안함', '선택안함'),
        ('여성', '여성'),
        ('남성', '남성'),
    )

    gender = models.CharField('성별(선택사항)',
                            max_length=10,
                            choices=GENDER,
                            default='N')

    #외래키 설정                        
    def __str__(self): 
        return self.nickname

    #나를 팔로우한 유저들
    @property
    def get_follower(self):
        return [i.from_user for i in self.follower_user.all()]
    #내가 팔로우한 유저들
    @property
    def get_following(self):
        return [i.to_user for i in self.follow_user.all()]

    #숫자
    @property 
    def follower_count(self):
        return len(self.get_follower) #나를 팔로우한 사람들이 get_follower에 담김
    @property 
    def following_count(self):
        return len(self.get_following)
    
    #나를 팔로우한 사람 한명
    def is_follower(self, user):
        return user in self.get_follower
    def is_following(self, user):
        return user in self.get_following

class Follow(models.Model):
    from_user = models.ForeignKey(Profile, 
                                related_name='follow_user',
                                on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile,
                                related_name='follower_user',
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} -> {}".format(self.from_user, self.to_user)
    class Meta:
        unique_together = (
            ('from_user', 'to_user')
        )

