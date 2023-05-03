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
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('최종수정일', auto_now=True)

    # post 추가 필드
    parking = models.BooleanField('주차가능', default=False)
    price_range = models.IntegerField('가격대', default=0)
    phone_number = models.CharField('전화번호', max_length=20, blank=True)
    closed_days = models.CharField('휴무일',blank=True, max_length=50)




    def save(self, *args, **kwargs):
        # 주소에서 시군구 정보 추출해서 address_city 필드에 저장
        if self.address:
            address_list = self.address.split(' ')
            if len(address_list) >= 2:
                self.address_city = ' '.join(address_list[:2])
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title

class PostImage(models.Model):
    def default_image():
        return "default_image_path.jpg"
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post_images')
    image = ProcessedImageField(
        upload_to='posts/images',
        processors=[ResizeToFill(800, 800)],
        format='JPEG',
        options={'quality': 90},
        default=default_image,
    )
    
    def __str__(self):
        return f'{self.post.title} - {self.id}'



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
    created_at = models.DateTimeField('업로드 날짜', auto_now_add=True,)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True,)
    TASTE_EVALUATION_CHOICES = (
        (5, '맛있다'),
        (3, '괜찮다'),
        (1, '별로'),
    )
    taste_evaluation= models.IntegerField(choices=TASTE_EVALUATION_CHOICES)
    
    def post_image_path(instance, filename):
        return f'posts/{instance.user}/{filename}'


    def __str__(self):
        return self.content

class ReviewImage(models.Model):
    def default_image():
        return "default_image_path.jpg"
    review = models.ForeignKey(to='plates.Review', on_delete=models.CASCADE, related_name='review_images')
    image = ProcessedImageField(
        upload_to='posts/images',
        processors=[ResizeToFill(800, 800)],
        format='JPEG',
        options={'quality': 90},
        default=default_image,
        blank=True,
        null=True,
        )



class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(to='plates.Review', on_delete=models.CASCADE)
    content = models.TextField('내용')
    created_at = models.DateTimeField('업로드 날짜', auto_now_add=False)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)
    
    def __str__(self):
        return self.title
