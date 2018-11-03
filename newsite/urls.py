"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    # include((pattern_list, app_namespace), namespace=None)
    # app_namespase:app名称 namespace: app实例名称
    # 模板里调用实例: {% url 'app_name:path_name' %}
	path('', include(('blog.urls', 'blog'), namespace='blog')),
    path('register/', include(('users.urls', 'register'), namespace='register')),
    path('message_board/', include(('comments.urls', 'message_board'), namespace='comments')),
]