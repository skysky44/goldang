from django.contrib import admin
from .models import *


admin.site.register(Comment)
# admin.site.register(Picture)
admin.site.register(Post)
admin.site.register(QuestionAndAnswer)
admin.site.register(Review)