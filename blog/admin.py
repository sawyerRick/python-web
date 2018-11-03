from django.contrib import admin
from . import models

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'pub_time', 'author', 'views', 'isTop', 'id')

admin.site.register(models.article, ArticleAdmin)