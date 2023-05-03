from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Post(models.Model):
    def post_image_path(instance, filename):
        return f'posts/{instance.title}/{filename}'
    
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='like_posts')

    title = models.CharField('식당 이름', max_length=100)
    description = models.TextField('설명')
    address = models.CharField('주소', max_length=200)
    address_city = models.CharField('시군구', max_length=50, blank=True)
    restaurant_type = models.CharField('식당 종류', max_length=50)
    loc = models.CharField('위치', max_length=50)
    image = ProcessedImageField(
        upload_to=post_image_path,
        processors=[ResizeToFill(230, 230)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )
    
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('최종수정일', auto_now=True)

    # post 추가 필드
    parking = models.BooleanField('주차가능', default=False)
    price_range = models.IntegerField('가격대', default=0)
    phone_number = models.CharField('전화번호', max_length=20, blank=True)
    closed_days = models.CharField('휴무일',blank=True, max_length=50)
    rating = models.IntegerField('평점', default=0, blank=True)


    def save(self, *args, **kwargs):
        # 주소에서 시군구 정보 추출해서 address_city 필드에 저장
        if self.address:
            address_list = self.address.split(' ')
            if len(address_list) >= 2:
                self.address_city = ' '.join(address_list[:2])
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


# class Picture(models.Model):
#     def post_image_path(instance, filename):
#         return f'posts/{instance.title}/{filename}'
    
#     image = ProcessedImageField(
#         upload_to=post_image_path,
#         processors=[ResizeToFill(230, 230)],
#         format='JPEG',
#         options={'quality': 100},
#         blank=True,
#         null=True,
#     )

#     post = models.ForeignKey(to='plates.Post', on_delete=models.CASCADE, blank=True)
#     review = models.ForeignKey(to='plates.Review', on_delete=models.CASCADE, blank=True)   # 순서 확인
#     created_at = models.DateTimeField('업로드 날짜', auto_now_add=False)
#     updated_at = models.DateTimeField('수정 날짜', auto_now=True)

#     def __str__(self):
#         return self.title


class QuestionAndAnswer(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(to='plates.Post', on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=50)
    content = models.TextField('내용')
    created_at = models.DateTimeField('업로드 날짜', auto_now_add=False)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)
    

    def __str__(self):
        return self.title


class Review(models.Model):

    
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(to='plates.Post', on_delete=models.CASCADE)
    content = models.TextField('내용')
    rating = models.IntegerField('평점') # 활용하기
    created_at = models.DateTimeField('업로드 날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)
    TASTE_EVALUATION_CHOICES = (
        ('맛있다', '맛있다'),
        ('괜찮다', '괜찮다'),
        ('별로', '별로'),
    )
    taste_evaluation= models.CharField(max_length=10, choices=TASTE_EVALUATION_CHOICES)
    
    def post_image_path(instance, filename):
        return f'posts/{instance.user}/{filename}'

    image = ProcessedImageField(
        upload_to=post_image_path,
        processors=[ResizeToFill(230, 230)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )


    def __str__(self):
        return self.content


class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(to='plates.Review', on_delete=models.CASCADE)
    content = models.TextField('내용')
    created_at = models.DateTimeField('업로드 날짜', auto_now_add=False)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)
    
    def __str__(self):
        return self.title
