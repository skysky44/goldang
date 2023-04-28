from django import template

register = template.Library()


def get_rating(obj):
    return obj.review_set.aggregate(Avg('rating')).get('rating__avg')