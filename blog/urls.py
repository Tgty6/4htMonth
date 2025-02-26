"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from posts.views import (
    test_view, html_view,
    post_list_view,
    post_detail_view,
    cookies_view, video,
    post_create_view)
from users.views import register_view, login_view
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path("test/", test_view),
    path("html/", html_view),
    path('posts/', post_list_view),
    path("posts/<int:post_id>/", post_detail_view),
    path("cookies/", cookies_view),
    path("video/", video),
    path('', post_list_view, name='home'),
    path("posts/create/", post_create_view),
    path("register/", register_view),
    path("login/", login_view),
    path("logout/", login_view),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)