from django import template
from django.db.models import Avg
register = template.Library()

@register.filter
def get_rating(obj):
    if obj.review_set.exists():
        rating = obj.review_set.aggregate(Avg('taste_evaluation')).get('taste_evaluation__avg')
    else:
        rating = 0.0
    return round(rating, 1)

@register.filter
def count_taste_evaluation(reviews, evaluation):
    return reviews.filter(taste_evaluation=evaluation).count()