from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments, name='comments'),
    path('post_comment/', views.post_comment, name='post_comment'),
]
