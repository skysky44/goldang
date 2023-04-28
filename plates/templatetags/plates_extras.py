from django import template
from django.db.models import Avg
register = template.Library()

@register.filter
def get_rating(obj):
    rating = obj.review_set.aggregate(Avg('rating')).get('rating__avg')
    return round(rating, 1)