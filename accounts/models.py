from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    def get_image_path(instance, filename):
        return f'profile/{instance.username}/{filename}'
    nickname = models.CharField('닉네임', max_length=150)
    email = models.EmailField('이메일', max_length=150)
    profile_image_url = models.URLField(blank=True, null=True)
    picture = ProcessedImageField(
        upload_to=get_image_path,
        processors=[ResizeToFill(230, 230)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )
    address = models.CharField('집주소', max_length=150, blank=True)
    company_address = models.CharField('회사 위치', max_length=150, blank=True)
    followers = models.ManyToManyField('self', related_name='followings', symmetrical=False, blank=True)