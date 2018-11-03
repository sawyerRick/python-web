from django.urls import path, include, re_path
from . import views 

urlpatterns = [
	path('', views.index, name='home'),
	path('article/<int:article_id>/', views.article_page, name='article_page'),
	path('edit/<int:article_id>/', views.edit_page, name='edit_page'),
	path('edit_action/', views.edit_action, name='edit_action'),
	path('about_me/', views.about, name='about'),
    path('tag/', views.tag, name='tag'),
    path('tag/<str:tag>/', views.tag_articles, name='tag_articles')
]