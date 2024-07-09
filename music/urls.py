"""
URL configuration for music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
     path("admin/", admin.site.urls),

    path("index", views.index, name="index"),
    path("about",views.about,name="about"),
    path("blog",views.blog,name="blog"),
    path("contact",views.contact,name="contact"),
    path("elements",views.elements,name="elements"),
    path("gopi",views.gopi,name="gopi"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logout,name="logout"),
    path("",views.welcome,name="welcome"),
    path("music",views.music,name="music"),
    path("new",views.new,name="new"),
    path("playlist",views.playlist,name="playlist"),
    
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
