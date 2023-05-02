from django import template
from django.db.models import Avg
register = template.Library()

@register.filter
def get_rating(obj):
    if obj.review_set.exists():
        rating = obj.review_set.aggregate(Avg('rating')).get('rating__avg')
    else:
        rating = 0.0
    return round(rating, 1)