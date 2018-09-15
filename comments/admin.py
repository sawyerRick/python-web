from django.contrib import admin
from . import models

# Register your models here.
class comment_admin(admin.ModelAdmin):
	list_display = ('name', 'email', 'text', 'created_time')

admin.site.register(models.Comment, comment_admin)