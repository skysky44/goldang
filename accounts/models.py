from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    def get_image_path(instance, filename):
        return f'profile/{instance.username}/{filename}'
    
    address = models.CharField('주소', max_length=150)
    picture = ProcessedImageField(
        upload_to=get_image_path,
        processors=[ResizeToFill(230, 230)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )
    company_address = models.CharField('회사 위치', max_length=150)
    followers = models.ManyToManyField('self', related_name='followings', symmetrical=False)