from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<int:isSuccess>', views.result, name='result'),
    path('upload_file/', views.upload_file, name='upload'),
]