from allauth.socialaccount.models import SocialAccount
from django.db.models.signals import post_save
from django.contrib.auth.models import User

def create_user_profile(sender, instance, **kwargs):
    if kwargs['created']:
        social_account = SocialAccount.objects.get(provider='kakao', user=instance)
        extra_data = social_account.extra_data
        
        # 카카오에서 제공하는 유저 정보 중에서 필요한 정보를 가져옴
        nickname = extra_data.get('properties', {}).get('nickname')
        profile_image_url = extra_data.get('properties', {}).get('profileImageURL')
        email = extra_data.get('kakao_account', {}).get('email')
        
        # 가져온 정보를 User 모델의 필드에 저장
        if nickname:
            instance.nickname = nickname
        if profile_image_url:
            instance.profile_image_url = profile_image_url
        if email:
            instance.email = email
        instance.save()

# User 모델이 생성될 때, 위에서 정의한 create_user_profile 함수를 실행
post_save.connect(create_user_profile, sender=User)
