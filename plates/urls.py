from django.urls import path

from . import views


app_name = 'plates'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/update/', views.update, name='update'),
    path('<int:post_pk>/reviews/', views.review_create, name='review_create'),
    path('<int:post_pk>/reviews/<int:review_pk>/update/', views.review_update, name='review_update'), 
    path('<int:post_pk>/reviews/<int:review_pk>/delete/', views.review_delete,
    name='review_delete'),
    path('<int:post_pk>/likes/', views.likes, name='likes'),
    path('<int:post_pk>/reviews/<int:review_pk>/comments/', views.comment_create, name='review_comment_create'),
    path('<int:post_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='review_comment_update'),
    path('<int:post_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='review_comment_delete'),


    path('<int:post_pk>/reviews/<int:review_pk>/', views.review_detail, name='review_detail'),
]