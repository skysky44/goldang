# Generated by Django 3.2.18 on 2023-04-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='closed_days',
            field=models.CharField(blank=True, max_length=50, verbose_name='휴무일'),
        ),
        migrations.AddField(
            model_name='post',
            name='parking',
            field=models.BooleanField(default=False, verbose_name='주차가능'),
        ),
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='전화번호'),
        ),
        migrations.AddField(
            model_name='post',
            name='price_range',
            field=models.IntegerField(default=0, verbose_name='가격대'),
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(blank=True, default=0, verbose_name='평점'),
        ),
        migrations.AddField(
            model_name='review',
            name='taste_evaluation',
            field=models.CharField(blank=True, max_length=50, verbose_name='맛평가'),
        ),
    ]
