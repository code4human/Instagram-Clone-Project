from django.db import models
from taggit.managers import TaggableManager

class Cafe(models.Model): #대소문자 구분됨 주의
    name = models.CharField(max_length = 50)
    mainphoto = models.ImageField(blank=True, null=True)
    content = models.TextField() 
    subphoto = models.ImageField(blank=True, null=True) #슬라이드를 넘어가게 하는 포토
    lat = models.FloatField(null=True) #경도
    lng = models.FloatField(null=True) #위도
    publishedDate = models.DateTimeField(blank=True, null=True) #발행된 날짜
    modifiedDate = models.DateTimeField(blank=True, null=True)  #수정된 날짜
    locate = models.TextField(null=True) #장소
    phone = models.TextField(null=True)
    insta = models.TextField(null=True)  #인스타그램
    tag = TaggableManager(blank=True)

    def __str__(self):
        return self.name  #대표값을 name으로 지정 