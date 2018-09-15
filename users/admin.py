from django.contrib import admin
from .models import User

admin.site.unregister(User)
admin.site.register(User)