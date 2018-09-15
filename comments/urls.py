from django.urls import path
from .views import index, post_comment

urlpatterns = [
    path('', index),
    path('post_comment/', post_comment),
]
